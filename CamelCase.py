import sys

s = str(input().strip())
word=1
for i in range(len(s)):
    if s[i].isupper() :
        word += 1
print(word)