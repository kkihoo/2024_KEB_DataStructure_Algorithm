
class Graph:
	def __init__ (self, size) :
		self.SIZE = size
		self.graph = [[0 for _ in range(size)] for _ in range(size)]

def print_graph(g) :
	print(' ', end = ' ')
	for v in range(g.SIZE) :
		print(name_ary[v], end = ' ')
	print()
	for row in range(g.SIZE) :
		print(name_ary[row], end = ' ')
		for col in range(g.SIZE) :
			print(f'{g.graph[row][col]}', end = ' ')
		print()
	print()

def find_vertex(g, find_vtx) :
	stack = []
	visited_ary = []	# 방문한 노드

	current = 0	# 시작 정점
	stack.append(current)
	visited_ary.append(current)

	while (len(stack) != 0) :
		next = None
		for vertex in range(gSize) :
			if g.graph[current][vertex] != 0 :
				if vertex in visited_ary :	# 방문한 적이 있는 정점이면 탈락
					pass
				else :			# 방문한 적이 없으면 다음 정점으로 지정
					next = vertex
					break

		if next is not None :				# 다음에 방문할 정점이 있는 경우
			current = next
			stack.append(current)
			visited_ary.append(current)
		else :					# 다음에 방문할 정점이 없는 경우
			current = stack.pop()

	if find_vtx in visited_ary :
		return True
	else :
		return False


## 전역 변수 선언 부분 
G1 = None
name_ary = ['CC', 'SL', 'SC', 'DJ', 'GJ', 'BS' ]
CC, SL, SC, DJ, GJ, BS = 0, 1, 2, 3, 4, 5


## 메인 코드 부분 ##
gSize = 6
G1 = Graph(gSize)
G1.graph[CC][SL] = 10; G1.graph[CC][SC] = 15
G1.graph[SL][CC] = 10; G1.graph[SL][SC] = 40; G1.graph[SL][DJ] = 11; G1.graph[SL][GJ] = 50
G1.graph[SC][CC] = 15; G1.graph[SC][SL] = 40; G1.graph[SC][DJ] = 12
G1.graph[DJ][SL] = 11; G1.graph[DJ][SC] = 12; G1.graph[DJ][GJ] = 20; G1.graph[DJ][BS] = 30
G1.graph[GJ][SL] = 50; G1.graph[GJ][DJ] = 20; G1.graph[GJ][BS] = 25
G1.graph[BS][DJ] = 30; G1.graph[BS][GJ] = 25

print(' 철도 건설을 위한 전체 연결도 ')
print_graph(G1)

# 가중치 목록
edge_ary = []
for i in range(gSize) :
	for k in range(gSize) :
		if G1.graph[i][k] != 0 :
			edge_ary.append([G1.graph[i][k], i, k])

# from operator import itemgetter
# edge_ary = sorted(edge_ary, key = itemgetter(0), reverse = True)
edge_ary.sort(key = lambda data: data[0], reverse = True) #위의 두 줄과 같다.
print(edge_ary)

new_ary = []
for i in range(0,len(edge_ary), 2) :
	new_ary.append(edge_ary[i])

index = 0
while len(new_ary) > gSize - 1 :	# 간선의 개수가 '정점 개수-1'일 때까지 반복
	start = new_ary[index][1]
	end = new_ary[index][2]
	save_cost = new_ary[index][0]

	G1.graph[start][end] = 0
	G1.graph[end][start] = 0

	start_YN = find_vertex(G1, start)
	end_YN = find_vertex(G1, end)

	if start_YN and end_YN : # 제거
		del (new_ary[index])
	else : # 복구
		G1.graph[start][end] = save_cost
		G1.graph[end][start] = save_cost
		index += 1

print(' 최소 비용의 철도 연결도 ')
print_graph(G1)

sum_val = 0
for r in range(G1.SIZE):
    for c in range(G1.SIZE):
        sum_val += G1.graph[r][c]
print("비용 :", sum_val/2)

print("비용 :", sum(sum(row) for row in G1.graph) / 2) # for문으로 더 한것을 한줄로 표현하기