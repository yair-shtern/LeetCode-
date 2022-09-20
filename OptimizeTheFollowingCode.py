# Optimize the following code:
#
# def solution(arr):
# 	result = 0
# 	arr_len = len(arr)
# 	for i in range(arr_len):
# 		for j in range(arr_len):
# 			if arr[i] == arr[j]:
# 				result = max(result, abs(i-j))
# 	return result

# solution:
# def solution(arr):
# 	result = 0
# 	min_dict = {}
# 	for idx, num in enumerate(arr)):
# 		if num not in min_dict:
# 			min_dict[num] = index
# 		else:
# 			result = max(result, idx-min_dict[num])
# 	return result
