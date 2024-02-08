
class Node:
	def __init__ (self) :
		self.data = None
		self.link = None

def print_nodes(start) :
	current = start
	if current is None :
		return
	print(current.data, end = ' ')
	while current.link != None:
		current = current.link
		print(current.data, end = ' ')
	print()

def insert_node(find_data, insert_data) :
	global memory, head, current, pre

	if head.data == find_data :      
		node = Node()
		node.data = insert_data
		node.link = head
		head = node
		return

	current = head
	while current.link is not None :
		pre = current
		current = current.link
		if current.data == find_data :
			node = Node()
			node.data = insert_data
			node.link = current
			pre.link = node
			return

	node = Node()
	node.data = insert_data
	current.link = node

# 전역 변수
memory = []
head, current, pre = None, None, None
dataArray = ["메시", "펠레", "마라도나", "크루이프", "반바스텐"]

if __name__ == "__main__" :

	node = Node()
	node.data = dataArray[0]
	head = node
	memory.append(node)

	for data in dataArray[1:] :
		pre = node
		node = Node()
		node.data = data
		pre.link = node
		memory.append(node)

	print_nodes(head)

	insert_node("메시", "손흥민")
	print_nodes(head)

	insert_node("마라도나", "황희찬")
	print_nodes(head)

	insert_node("김기훈", "이강인")
	print_nodes(head)


