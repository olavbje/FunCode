# --- Day 2: Inventory management system ---
import numpy as np

def readfile(filename):
	"""
	Read file given by filename. 
	
	Return
		array of data from file seperated by lines (each line as str) 
	"""
	with open(filename) as f:
		data = f.read().splitlines()
	data1 = np.array(data)
	data2 = data1.astype(np.str)
	return data2

# Part 1
def checksum(data):
	count2 = 0	#Counter for line with two unique chars
	count3 = 0	#Counter for line with three unique chars
	for line in data:
		count2_list = []	#List for all repeted chars in line
		for i in range(len(line)):
			if line[i] in line[i+1:]:
				count2_list.append(line[i])

		if len(count2_list) > 0:
			count2 += 1
			count3_list = []	#List for all repeted chars in count2_list
			for i in range(len(count2_list)):
				if count2_list[i] in count2_list[i+1:]:
					count3 += 1
					break
	return count2*count3
			
			
# Part 2
def compare_strings(data):
	data_length = len(data)
	line_length = len(data[0])
	for i in range(data_length-1):
		for j in range(i+1, data_length):
			error = 0
			for k in range(line_length):
				if data[i][k] == data[j][k]:
					continue
				else:
					error += 1
					if error == 2:
						break
			if error < 2:
				print("The two similar IDs: {} and {}".format(data[i],data[j]))
		
	
if __name__ == '__main__':
	data = readfile("input.txt")
	
	#Part1
	print(checksum(data))
	
	#Part2
	compare_strings(data)
	
"""
The two similar IDs: tzyvunogzariwkpcbdewsmjhxi and tzyvunogzariwkpcbdewmmjhxi
"""