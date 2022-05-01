import random

# Generating a random list
randomlist = random.sample(range(1, 1000), 500)
# print(randomlist)
while True:
    try:
        item = int(
            input('What number do you want to find between 1 & 1000 \n > '))

        found = False

        while found is False:
            for num in randomlist:
                print('Scanning. Currently on position', randomlist.index(num))
                if num == item:
                    found = True
                    print('Found', num, 'in the random list of numbers at position',
                          randomlist.index(num))
                    break
            if item not in randomlist:
                print(
                    'Could not find', item)
                break
    except ValueError:
        print('Please Enter A Real Number')
        pass
    else:
        break
