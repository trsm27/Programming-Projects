import random
import json

def make(quote):
	with open('Data.json', 'r')as fp:
		cache = json.load(fp)
		fp.close()

	cache.append(quote)

	with open('Data.json', 'w')as fp:
		json.dump(cache, fp)
		fp.close

	print('saved!')

def read():
	with open('Data.json','r')as fp:
		cache = json.load(fp)
		fp.close()
	print(random.choice(cache))

def start():
	print("what is your choice")
	print("1.write a quote")
	print("2.listen to a quote")
	will = input(">")
	if will == "1":
		quote = input('input your quote in speach marks!')
		make(quote)

	elif will == "2":
		read()

	else:
		print("unknown input!, try again!")
while True:
    start()
