# --- Day 1: Chronal Calibration ---
import numpy as np

def readfile(filename):
	with open(filename) as f:
		data = f.read().splitlines()
	data1 = np.array(data)
	data2 = data1.astype(np.int)
	return data2

# Part 1
def part1(data):
	print(np.sum(data))

# Part 2
def part2(data):
	occured = [0]
	match = False
	data_len = len(data)
	w = 0
	while match == False:
		n = 0
		print(w)
		for n in range(data_len):
			w += data[n]
			if w in occured:
				match = True
				print("This value has occured twice: {}".format(w))
				break
			occured.append(w)
			n += 1
			
if __name__ == '__main__':
	data = readfile("input.txt")
	#Part 1
	#part1(data)
	# Part 2
	part2(data)


