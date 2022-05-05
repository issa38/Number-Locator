# Dictionary Practice.

name = input("Enter file:")

try:
    handle = open(name)
except:
    print('Could not locate file')
    quit()

lst = []

# Creates the original dictarny with the senders name as the key
for line in handle:
    if not line.startswith('From:'):
        continue
    line = line.split()
    lst.append(line[1].capitalize())

repeats = {}
# Increases the number of the value for the given keys above.
for word in lst:
    repeats[word] = repeats.get(word, 0) + 1

# Cycles through the dictionary and updates the biggest username and the amount of times they have showed up.
bigcount = None
emailer = None
for word, reps in repeats.items():
    if bigcount is None or reps > bigcount:
        bigcount = reps
        emailer = word


print('The user who sent the most amount of emails was :',
      emailer, 'and they appeared', bigcount, 'times.')
