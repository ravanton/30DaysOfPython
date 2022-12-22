import re

txt = 'I love to teach python and javaScript'
# It returns an object with span, and match

match = re.match('I love to teach', txt, re.I)
print(match)

# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span)

# Lets find the start and stop position from the span
start, end = span
print(start, end)



txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It returns an object with span and match
match = re.search('first', txt, re.I)
print(match)  # <re.Match object; span=(100, 105), match='first'>
# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span)     # (100, 105)
# Lets find the start and stop position from the span
start, end = span
print(start, end)  # 100 105
substring = txt[start:end]
print(substring)       # first

# Searching for All Matches Using findall
# findall() returns all the matches as a list
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It return a list
matches = re.findall('language', txt, re.I)
print(matches)  # ['language', 'language']

matches = re.findall('[Pp]ython', txt)
print(matches)  # ['Python', 'python']

# Replacing a Substring
matches_replaced = re.sub('[Pp]ython', 'Javascript', txt)
print(matches_replaced)