print("hello")
import random
import string
# n=random.randint(1,100)
n=50
fileob=open("fxt.txt","w")
fileob.write((str)(n)+"\n");
for i in range(n):
	x=random.randint(1,10000);
	leng=random.randint(3,10);
	str1=''.join(random.choice(string.ascii_letters) for j in range(leng))
	str2=''.join(random.choice(string.ascii_letters) for j in range(leng))
	val=random.randint(1,2)
	if(val==1):
		# print((str)(val)+" "+(str)(x)+" "+str1)
		fstr=(str)(val)+" "+(str)(x)+" "+str1+"\n"
		fileob.write(fstr)

	else:
	    # print((str)(val)+" "+(str)(x)+" "+str1+" "+str2)
	    fstr=(str)(val)+" "+(str)(x)+" "+str1+" "+str2+"\n"
	    fileob.write(fstr)
	    

fileob.close()