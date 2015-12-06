def bellmen(edgeList, vertices, edges, source):
	distance = dict()
	for v in vertices: distance[v] = float('inf')
	
	distance[source] = 0
	
	for v in vertices:
		for e in edgeList[v]:
			if (distance[v] + 1 < distance[e]):
				distance[e] = distance[v] + 1;
	
	return distance
	
def main():
	#create empty edge list
	edgeList = dict()

	#open file and create edge list
	file = open('12831.edges', 'r')

	for line in file:
		str = line.split()
		key = int(str[0])
		val = int(str[1])
		if (key not in edgeList): edgeList[key] = []
		edgeList[key].append(val);
		
	file.close()
	
	print(len(edgeList))
	
main()
