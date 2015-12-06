import time

def SPFA(edgeList, source):
	#Setup
	distance = dict()
	distance[source] = 0
	queue = []
	
	#Add Source
	queue.append(source)
	
	while (len(queue) > 0):
		v = queue.pop()
		if (v not in edgeList): continue
		for e in edgeList[v]:
			if (v not in distance): distance[v] = float('inf')
			if (e not in distance): distance[e] = float('inf')
			if (distance[v] + 1 < distance[e]):
				distance[e] = distance[v] + 1;
				if (e not in queue):
					queue.append(e)
				
	return distance
	
def main():
	#create empty edge list
	edgeList = dict()

	#open file and create edge list
	file = open('twitter_combined.txt', 'r')

	for line in file:
		s = line.split()
		key = int(s[0])
		val = int(s[1])
		if (key not in edgeList): edgeList[key] = []
		edgeList[key].append(val);
		
	file.close()
	
	#choose a source
	source = 398874773
	
	start = time.time()
	distance = SPFA(edgeList, source)
	print(time.time() - start)
	
main()
