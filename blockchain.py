blockchain = [] #make an array

def getLastValue():
	return blockchain[-1]

def add_value(tranV, last_value=[1]):
	blockchain.append([last_value, tranV])

tx_amount = float(input('Your transaction amount please: '))
add_value(tx_amount)
add_value(last_value=getLastValue(),tranV=3)
add_value(10.98, getLastValue())

print(blockchain)
