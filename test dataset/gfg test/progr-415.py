n=1212112
s = [int(a) for a in str(n)]
evensum=[int(a) for i,a in enumerate(s) if i%2==0]
oddsum=[int(a) for i,a in enumerate(s) if i%2!=0]
if (sum(evensum)-sum(oddsum))==0:
  print("yes")
else:
  print("no")