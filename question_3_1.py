import re

with open('blocklist.xml', 'r') as f:
    data = f.read()

pattern = re.compile(r'<.+\sblockID="[ig].*\d+".*>')
result = re.findall(pattern, data)

print('\n'.join(result))
