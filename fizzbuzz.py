fruits = ['Apple', 'Banana', 'Pineapple']

animals = [
    'Lion',
    'Tiger',
    'Rabbit'
]

Clubs = [
    'ManU',
    'ManC',
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
