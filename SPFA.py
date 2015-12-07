import sys
import time

def SPFA(edgeList, source):
	#Setup
	distance = dict()
	distance[source] = 0
	queue = []
	
	#Add Source
	queue.append(source)
	
	#Until the queue is empty
	while (len(queue) > 0):
		#Grab the next vertex
		v = queue.pop()
		#Some vertices don't have any edges from them
		if (v not in edgeList): continue
		#For each edge on the vertex
		for e in edgeList[v]:
			#Initialize unseen vertices
			if (e not in distance): distance[e] = float('inf')
			#If there is a shorter distance, use it
			if (distance[v] + 1 < distance[e]):
				distance[e] = distance[v] + 1;
				#Add the changed vertex back into the queue for reanalysis
				if (e not in queue):
					queue.append(e)
				
	return distance
	
def main():
	#create empty edge list
	edgeList = dict()

	#open file and create edge list
	file = open(sys.argv[1], 'r')

	for line in file:
		s = line.split()
		key = int(s[0])
		val = int(s[1])
		if (key not in edgeList): edgeList[key] = []
		edgeList[key].append(val);
		
	file.close()
	
	#choose a source
	source = list(edgeList.keys())[0]
	
	start = time.time()
	distance = SPFA(edgeList, source)
	print(time.time() - start)
	
main()
