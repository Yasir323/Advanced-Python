import re


class RegexPattern:
    def __init__(self, pattern):
        self.pattern = pattern

    def match(self, text):
        return bool(re.match(self.pattern, text))


# Usage
pattern1 = RegexPattern(r'^\d{4}$')
pattern2 = RegexPattern(r'^[a-zA-Z]+$')

text1 = '1234'
text2 = 'abcd'
text3 = '12ab'

print(pattern1.match(text1))  # True
print(pattern1.match(text2))  # False

print(pattern2.match(text2))  # True
print(pattern2.match(text3))  # False
