import re


x = '1.2.3b3  RELEASE: (foo): (bar)'
x = '1.2.3b3  RELEASE'

res = re.match(r'^(?P<ver>\d+\.\d+\.\d+(?:b\d*)?)[ ]+RELEASE(?P<desc>.*)', x, re.IGNORECASE)
if res is None:
    print('no match')
else:
    ver = res.group('ver')
    desc = re.sub(r'^(?::)?\s+', '', res.group('desc'))
    print(f"ver : {repr(ver)}")
    print(f"desc: {repr(desc)}")
    if 'b' in ver:
        print('prerelease!')