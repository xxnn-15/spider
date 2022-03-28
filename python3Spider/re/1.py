import re
content = 'Hello 123 4567 World_This is a Regex Demo'
result = re.match('^Hello\s(\d{3})\s\d{4}\s\w{10}', content)
print(result.group())
print(result.group(1))