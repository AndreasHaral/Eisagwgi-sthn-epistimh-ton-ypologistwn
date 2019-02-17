

open1=open("kapoiofile.py","r")#onomafile
grammes=open1.readlines()
open1.close()


for line in grammes:
	if "#" in line:
		
		k1=line.strip()
		if k1[0]!="#": 
			lsplit=line.split("#")
			a1=lsplit[0].count("'")
			a2=lspit[0].count('"')
			if a1%2==1 or a2%2==1:
				print (line)
			else:
				print (line.split("#")[0])
	else:
		print (line)
