f = open("1.txt","w+")

for i in range(5):
     f.write("This is line %d\n" % (i+1))
f.close()