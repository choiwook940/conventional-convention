fruits = ['Apple', 'Banana', 'Pineapple', 3]

animals = [
    'Lion',
    'Tiger',
    'Rabbit',
    3
]

Clubs = [
    'ManU',
    'ManC',
    3,
]

for i in range(1,16+1):
    if i%15==0:
        print('fizzbuzz')
    elif i%3==0:
        print('fizz')
    elif i%5==0:
        print('buzz')
    else:
        print(i)
