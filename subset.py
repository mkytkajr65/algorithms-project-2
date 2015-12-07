import random
import sys
sys.setrecursionlimit(10000)

def subgraph(edgeList, subList, key, size):
	for e in edgeList[key]:
		if (e not in edgeList): continue
		if (e not in subList):
			subList.append(e)
			if (len(subList) >= size): return
			subgraph(edgeList, subList, e, size)
		if (len(subList) >= size): return

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
	
	for i in range(0, 10):
		print("running instance " + str(i))
		start = random.randint(0, len(edgeList.keys()))
		key = list(edgeList.keys())[start]
		
		subList = []
		subgraph(edgeList, subList, key, 10000)
		
		file = open('subset' + str(i) + '.txt', 'w')
		
		for v in subList:
			for e in edgeList[v]:
				if (e in subList):
					file.write(str(v) + " " + str(e) + "\n")
		
		file.close()
	
main()