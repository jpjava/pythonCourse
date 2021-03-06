#initializing the blockchain list
blockchain = [] #make an array

def getLastValue():
	"""Returns the last value of the current blockchain """
	if len(blockchain)<1:
		return None
	return blockchain[-1]

def add_value(tranV, last_value=[1]):
	"""Append a new value as as the last blockchain fvalue to the blockchain"""
	blockchain.append([last_value, tranV])

def get_transaction_value():
	user_input= float(input('Your transaction amount please: '))
	return user_input
def get_user_choice():
	user_input = input('Your choice: ')
	return  user_input

def print_blockchain_elements():
	for block in blockchain:
		print('Outputting Block')
		print(block)


while True:
	print('Please choose')
	print('1: Add a new transaction value')
	print('2: Output the transaction block')
	user_choice = get_user_choice()
	if user_choice == 1:
		tx_amount= get_transaction_value()
		add_value(tx_amount, getLastValue())
	elif user_choice == 2:
		print_blockchain_elements()
	elif user_choice == "q":
		break		
	else:
		print('Input was invalid, please pick a value from the list!')
	
	


print('Done!')
