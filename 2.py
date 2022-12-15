def factorial (number, count = 1):
    for i in range (1, number + 1 ):
     count*=i
    return count 
    
num = int(input('Введите число: '))
print(f'Набор произведений чисел от 1 до {num} = ', end = '')
for i in range(1, num + 1):
    if i == num: 
        print(f'{factorial(i)}')
    else:
        print(f'{factorial(i)}', end = ', ')