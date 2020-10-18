import re

with open('blocklist.xml', 'r') as f:
    data = f.read()

pattern = re.compile(r'<.+\sid="[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+".*>')
result = re.findall(pattern, data)

print('\n'.join(result))
