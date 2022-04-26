n = int(input())
b = "\n"
while n > 0:
  b = str(n % 10) + "\n" + b
  n = n // 10
print(b.strip())