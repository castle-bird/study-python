a = 'life is too short, you need python'

if 'wife' in a : print('wife')
elif 'python' in a and 'you' not in a: print('python')
elif 'shirt' not in a : print('shirt')
elif 'need' in a : print('need')

result = 0
i = 1 
while i < 1000:
    if i % 3 == 0 :
        result += i
    i += 1
    
print(result)

i = 0
while True:
    i += 1
    if i > 5 : break
    print('*' * i)
    
# for i in range(1, 101) :
#     print(i)

A = [70, 60, 55, 75]
total = 0
for score in A :
    total += score

avg = total / len(A)
print(avg)


# numbers = [1,2,3,4,5]
# result = []

# for number in numbers : 
#     if number % 2 == 1 :
#         result.append(number * 2)
        

numbers = [1,2,3,4,5]
result = [number * 2 for number in numbers if number % 2 != 0 ]
print(result)