# Simple List Sort

fname = input("Enter file name: ")

try:
    fh = open(fname)
except:
    print('File not found.')
    quit()


lst = []
for line in fh:
    x = line.split()
    for word in x:
        if word in lst:
            continue
        else:
            lst.append(word)
    lst.sort()

print(lst)
