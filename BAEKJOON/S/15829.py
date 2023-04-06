from string import ascii_lowercase

L = int(input())
strings = list(input())
num = 0
for index, str in enumerate(strings):
    num += ((ascii_lowercase.find(str)+1) * (31**index))

print(num%1234567891)