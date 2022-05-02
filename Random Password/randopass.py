# Generate a random password. Simple Project
import string
import random
import sys


def pass_generator(size=8, char=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(10))


f = open("output.txt", 'w')
sys.stdout = f
i = 0
while i < 10:
    print('Your password is:', pass_generator())
    i = i + 1

print('\n')
f.close()
