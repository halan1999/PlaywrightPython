# for i in range(1, 11):
#     print(f"2 x {i} = {i*2}")

# for i in range(1,11):
#     print(f"3 x {i} = {i*3}")

#In bảng cửu chương của list sau:
numbers = [2, 5, 8, 11, 14, 17, 20]
for num in numbers:
    print(f'Bảng cửu chương {num}: ')
    for i in range(1,11):
        print(f'{num} x {i} = {num*i}')
    print('-'*20)
