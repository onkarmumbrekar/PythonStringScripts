string=str(input())
words =string.split(" ")
for i in range(len(words)):
       words[i] = words[i].capitalize()
       string=string.replace(words[i].lower(),words[i])
print(string)
