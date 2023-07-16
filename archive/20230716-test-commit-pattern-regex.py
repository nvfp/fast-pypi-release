"""
fast-pypi-release (1.4.0)
"""
import re


## Wrong one
# REGEX = r'^(?P<ver>\d+\.\d+\.\d+(?:b\d*)?)[ ]+(?P<mode>RELEASE|TESTING)(?P<desc>.*)'

## Latest/Prerelease
REGEX_RELEASE = r'^(?P<ver>\d+\.\d+\.\d+(?:b\d*)?)[ ]+(?P<mode>RELEASE)(?P<desc>.*)'

## Testing
REGEX_TESTING = r'^(?P<ver>\d+\.\d+\.\d+b\d*)[ ]+(?P<mode>TESTING)(?P<desc>.*)'

## Latest/Prerelease + Testing (Invalid)
# REGEX = r'(^(?P<ver>\d+\.\d+\.\d+(?:b\d*)?)[ ]+(?P<mode>RELEASE)(?P<desc>.*))|(^(?P<ver>\d+\.\d+\.\d+b\d*)[ ]+(?P<mode>TESTING)(?P<desc>.*))'


def result(input_str):
    
    res = re.match(REGEX_RELEASE, input_str, re.IGNORECASE)
    if res is None:
        res = re.match(REGEX_TESTING, input_str, re.IGNORECASE)

    if res is None:
        return False, None, None, None, None  # match, ver, desc, prerelease, testing
    else:
        ver = res.group('ver')
        desc = re.sub(r'^(?::)?\s+', '', res.group('desc'))  # Trim the leading spaces or colon-spaces
        prerelease = True if 'b' in ver else False
        testing = True if res.group('mode').lower() == 'testing' else False
        return True, ver, desc, prerelease, testing


def test(input_str, expected_match, expected_ver=None, expected_desc=None, expected_prerelease=None, expected_testing=None):
    print(repr(input_str))
    match, ver, desc, prerelease, testing = result(input_str)
    assert match == expected_match, f'{match} == {expected_match}'
    assert ver == expected_ver, f'{repr(ver)} == {repr(expected_ver)}'
    assert desc == expected_desc, f'{repr(desc)} == {repr(expected_desc)}'
    assert prerelease == expected_prerelease, f'{prerelease} == {expected_prerelease}'
    assert testing == expected_testing, f'{testing} == {expected_testing}'


## Not the pattern
test(''           , False)
test('foo'        , False)
test('123-foo_xyz', False)
test('Release'    , False)

## Latest
test('1.0.0 Release'   , True, '1.0.0'   , '', False, False)
test('1.0.0  release'  , True, '1.0.0'   , '', False, False)
test('1.0.0   reLeAsE' , True, '1.0.0'   , '', False, False)
test('10.20.30 RELEASE', True, '10.20.30', '', False, False)

## Prerelease
test('1.0.0b release'                      , True, '1.0.0b'  , ''                , True, False)
test('3.2.1b0 RELEASE: foo (bar: baz)'     , True, '3.2.1b0' , 'foo (bar: baz)'  , True, False)
test('3.2.1b10  RELEASE   [foo] (bar: baz)', True, '3.2.1b10', '[foo] (bar: baz)', True, False)

## Testing
test('9.9.9b1   Testing'                 , True, '9.9.9b1'  , ''                , True, True)
test('1.0.0b TESTING: Beta version'      , True, '1.0.0b'   , 'Beta version'    , True, True)
test('1.5.0b123 testing (dev: test only)', True, '1.5.0b123', '(dev: test only)', True, True)

## Invalid Testing (Testing mode can only be used with beta versions)
test('9.9.9 Testing', False)

## Common errors
test(' 1.0.0 release', False)
test('1.0.0release'  , False)
test('1.0.0b3testinG', False)

print('----------------\nAll tests passed.')