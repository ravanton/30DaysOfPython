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

# What is the most frequent word in the following paragraph?

# Python program to find the k most frequent words
# from data set
from collections import Counter
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

split_it = paragraph.split()
Counter = Counter(split_it)

most_occur = Counter.most_common(20)
print(most_occur)