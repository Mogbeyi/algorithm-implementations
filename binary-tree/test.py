'''
Using 1 as your starting point, you are given an K
You have only two operations. Multiply by 2 and divide by 3
Find the minimum number of steps to get to K using only those two operations
'''

min_step = 0
result = 1
if K != 1:
	while result != K:
		x = result * 2
		y = result / 3
		if x == K:
			min_step++

return min_step

'''
1: 0
2: 2 * 1 => 1
3: 2 * 2 * 2 * 2 / 3 * 2 / 3 => 7
4: 2 * 2 => 2
'''


