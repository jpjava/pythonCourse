blockchain = [] #make an array

def getLastValue():
	return blockchain[-1]

def add_value(tranV, last_value=[1]):
	blockchain.append([last_value, tranV])

add_value(2)
add_value(last_value=getLastValue(),tranV=3)
add_value(10.98, getLastValue())

print(blockchain)
