# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for word in fh:
    line=word.rstrip()
    print(line.upper())