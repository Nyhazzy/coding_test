import sys

#text = list(input())
texts = sys.stdin.read().splitlines()
#print(texts)
#N = len(texts)

for text in texts:
    lower, upper, num, space = 0, 0, 0, 0

    for i in text:
        if i.islower():
            lower += 1
        elif i.isupper():
            upper += 1
        elif i.isdigit():
            num += 1
        elif i.isspace():
            space += 1

    print(lower, upper, num, space)