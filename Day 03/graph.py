class Graph() :
	def __init__ (self, size) :
		self.SIZE = size
		self.graph = [ [0 for _ in range(size)] for _ in range(size) ]

def print_graph(g) :
	print(' ', end = ' ')
	for v in range(g.SIZE) :
		print(f' {name_ary[v]}', end = ' ')
	print()
	for row in range(g.SIZE) :
		print(name_ary[row], end = ' ')
		for col in range(g.SIZE) :
			print(g.graph[row][col], end= '  ')
		print()
	print()

name_ary = ["A", "B", "C", "D"]
## 전역 변수 선언 부분 ##
G1, G2, G3 = None, None, None

## 메인 코드 부분 ##
G1 = Graph(4)
G1.graph[0][1] = 1; G1.graph[0][2] = 1; G1.graph[0][3] = 1
G1.graph[1][0] = 1; G1.graph[1][2] = 1
G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] = 1
G1.graph[3][0] = 1; G1.graph[3][2] = 1

print('   ** G1 **    ')
for row in range(G1.SIZE) :
	for col in range(G1.SIZE) :
		print(G1.graph[row][col], end=' ')
	print()

G2 = Graph(4)
G2.graph[0][3] = 1;
G2.graph[1][2] = 1; G2.graph[1][3] = 1;
G2.graph[2][1] = 1;
G2.graph[3][0] = 1; G2.graph[3][1] = 1;

print('   ** G2 **   ')
for row in range(G2.SIZE) :
	for col in range(G2.SIZE) :
		print(G2.graph[row][col], end=' ')
	print()

G3 = Graph(4)
G3.graph[0][1] = 1; G3.graph[0][2] = 1
G3.graph[3][0] = 1; G3.graph[3][2] = 1

print('   ** G3 **   ')
print_graph(G3)

