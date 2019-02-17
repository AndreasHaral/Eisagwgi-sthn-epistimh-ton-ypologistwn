open1=open("kapoiofile.py","r")
end=open1.readlines()
open1.close()
for i in end:
	if "#" in i:#an arxizei apo "#"
		k1=i.strip()
		if k1[0]!="#": 
			help1=i.split("#")
			aytakia1=help1[0].count("'")			
			aytakia2=help1[0].count('"')
#elegxoume an to "#"einai se kapoio string h print h genikws se kapoio kommati kodika
#metrame to sunolo gia kathe aytakia kai elexgoume an exoun ypoloipo
			if aytakia1%2==1 or aytakia2%2==1:
				print i
			else:
				print i.split("#")[0]
	else:
		print i
