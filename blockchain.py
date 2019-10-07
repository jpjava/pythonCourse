blockchain = [1] #make an array
def getLastValue():
	return blockchain[-1]

def add_value(tranV):
	blockchain.append([getLastValue(),tranV])

add_value(3)

print(blockchain)
