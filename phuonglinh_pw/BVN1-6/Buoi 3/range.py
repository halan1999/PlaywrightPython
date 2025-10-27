# for i in range(4):
#     print(i)

# for i in range(1, 11, 2):
#     print(i)

#number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for n in range(1,21):
    if n % 3 == 0 and n % 5 == 0 :
        print('FizzBuzz')
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    else:
        print(n)
