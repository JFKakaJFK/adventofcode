string = str(input('Enter number:'))
a = 0
for i in range(-1, len(string) -1):
  if string[i] == string[i + 1]:
    a += int(string[i])
print()
print(a)
