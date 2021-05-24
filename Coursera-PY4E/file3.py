fname = input("Enter file name: ")
count=0;number=0
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count=count+1
    number=float(line[21:27])+number
print("Average spam confidence: ",number/count)