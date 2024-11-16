kor = 80
eng = 75
math = 55
sum = kor + eng + math
avg = sum / 3

print(avg)

number = 13
isOdd = number / 2 == 0
print(isOdd)

pin = "881120-1068234"
yymmdd = pin[0:6]
num = pin[7:]
print(yymmdd)
print(num)
print(pin[7])

a = "a:b:c:d"
b = a.replace(':', '#')
print(b)

a2 = [1,2,3,4,5]
a2.sort()
a2.reverse()
print(a2)

a3 = ['life', 'is', 'too', 'short']
result = '*'.join(a3)
print(result)

(a,b) = ['asd','asdsadsa']
print(type(a))
print(b)