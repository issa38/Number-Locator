# Files are Sequences of Data. Sequences are Ordered Sets.
# Use the file name mbox-short.txt as the file name

# Preparing for Wrong User Input
fname = input("Enter file name: ")

try:
    fh = open(fname)
except:
    print('Incorrect File Syntax or File Not Found')
    quit()

# Initilizing Vars.
count = 0
total = 0
lcount = 0


for line in fh:
    # Measures the number of the lines in the file.
    lcount = lcount + 1
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    # Finds the occurences of the spam confidence lines and strips everything but the float values associated with it.
    count = count + 1
    space = line.find(" ")
    value = float(line[space:].strip())

    total = value + total


avg = total / count

print('There are', lcount, 'lines in the file.')
print('Of those,', lcount, 'lines, there are',
      count, 'occurencese of Spam calculations.')
print("Average spam confidence:", avg)
