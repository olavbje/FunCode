# Day 3
import re
import numpy as np

def read_table(filename):
	"""
	Read datafile. Divide raw data with regex.
	"""
	with open(filename) as f:
		raw_data = f.read().splitlines()
	
	r1 = "@([^,]*),"
	r2 = ",([^:]*):"
	r3 = ":([^x]*)x"
	r4 = "x(.*)"
	data = np.zeros((len(raw_data),4), dtype=int)
	for i in range(len(raw_data)):
		data[i][0] = int(re.search(r1,raw_data[i]).group(1))
		data[i][1] = int(re.search(r2,raw_data[i]).group(1))
		data[i][2] = int(re.search(r3,raw_data[i]).group(1))
		data[i][3] = int(re.search(r4,raw_data[i]).group(1))
	
	return data

def find_overlap(data):
	map = [[0 for x in range(1000)] for y in range(1000)]
	overlap_counter = 0
	
	for i in range(len(data)):
		y0 = data[i][0]
		y1 = data[i][0] + data[i][2]
		x0 = data[i][1]
		x1 = data[i][1] + data[i][3]
		for row in range(x0,x1):
			for column in range(y0,y1):
				if map[row][column] == 0:
					map[row][column] = "*"
				elif map[row][column] == "*":
					map[row][column] = "X"
					overlap_counter += 1
				elif map[row][column] == "X":
					continue
				else:
					print(i,row,column)
					
	return map

def find_non_overlap(data,map):
	for i in range(len(data)):
		y0 = data[i][0]
		y1 = data[i][0] + data[i][2]
		x0 = data[i][1]
		x1 = data[i][1] + data[i][3]
		
		single_claim = True
		for row in range(x0,x1):
			for column in range(y0,y1):
				if map[row][column] == "*":
					continue
				elif map[row][column] == "X":
					single_claim = False
					break
		if single_claim == True:
			print("Single claim ID: {}".format(i+1))
	return i+1
	
	
	
if __name__ == '__main__':
	#Part1
	collected_data = read_table("input.txt")
	map = find_overlap(collected_data)
	#Part2
	single = find_non_overlap(collected_data,map)
				
	
	
	
	
	
	
	
	
	
	
	
	