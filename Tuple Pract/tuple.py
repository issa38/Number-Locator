
name = input("Enter file:")

file = open(name)

# Creating the Tuples of the Hr:M:S of the emails sent.
lst = []
for line in file:
    # Sorts through the file to weed out different types of emails.
    if not line.startswith('From'):
        continue
    if line.startswith('From:'):
        continue
    # This pulls the time out of the lines that are sorted out. Emails always have a set structure so I made it static but i should probably change this.
    splitter = line.split()
    time = splitter[5].split(':')
    hour = time[0]
    lst.append(hour)

# Creating the dictionary that counts the appreances of each hour and histograms it.
counts = dict()
for hour in lst:
    counts[hour] = counts.get(hour, 0) + 1

# This is a shorthand version of sorting using lamdas. Not really sure what they are but its an expression of code basically i think.
sort = sorted(counts.items(), key=lambda x: x[0])

for k, v in sort:
    print('The hour', k, 'shwos up', v, 'times.')
