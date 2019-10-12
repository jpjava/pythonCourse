#initializing the blockchain list
blockchain = [] #make an array

def getLastValue():
	"""Returns the last value of the current blockchain """
	return blockchain[-1]

def add_value(tranV, last_value=[1]):
	"""Append a new value as as the last blockchain fvalue to the blockchain"""
	blockchain.append([last_value, tranV])

def get_user_input():
	return float(input('Your transaction amount please: '))


tx_amount = get_user_input()
add_value(tx_amount)
#add_value(last_value=getLastValue(),tranV=3)
#add_value(10.98, getLastValue())

while True:
	tx_amount = get_user_input()
	add_value(last_value=getLastValue(),tranV=3)

	#output the blockchain
	for block in blockchain:
		print('Outputting Block')
		print(block)

print('Done!')
