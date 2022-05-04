# Files are Sequences of Data. Sequences are Ordered Sets.
# Use the file name mbox-short.txt as the file name

# Preparing for Wrong User Input
try:
    fname = input("Enter file name: ")
except:
    print('Incorrect File Syntax or File Not Found')
    quit()

# Initilizing Vars.
count = 0
total = 0
lcount = 0

fh = open(fname)
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
