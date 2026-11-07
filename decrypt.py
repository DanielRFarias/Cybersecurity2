from cryptography.fernet import Fernet
import os

#From crypt.py
def keyLoad():
	return open("chave.key", "rb").read()

def listing(dir):
	list = []
	for root, _, files in os.walk(dir):
		for name in files:
			pat = os.path.join(root, name)
			#Change name based on this file, this file should not be cryptographed
			#Neither the key
			if name!= "crypt.py" and not name.endswith(".key"):
				list.append(pat)

	return list



#One new function for this file
#Not much diference tough
def decryp(arq, key):
	f = Fernet(key)
	with open(arq, "rb") as file:
		data = file.read()
		restored_data = f.decrypt(data)
	with open(arq, "wb") as file:
		file.write(restored_data)




#Same error as crypt
def main():
	key = keyLoad()
	arqs = listing("Insert current directory")
	for arq in arqs:
		decryp(arq, key)
	print("Code executed successfully")

#First time i saw this but it is interesting
if __name__=="__main__":
    main()
