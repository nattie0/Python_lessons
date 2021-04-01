def merge_sort(arr):
	if len(arr) <= 1:
		return arr
	index = len(arr) // 2
	left = arr[:index]
	right = arr[index:]
	return merge(merge_sort(left), merge_sort(right))
	
def merge(left, right):
	left_max = len(left)
	right_max = len(right)
	left_cur, right_cur = 0, 0
	result = []
	while left_cur<left_max and right_cur < right_max:
		if left[left_cur] <= right[right_cur]:
			result.append(left[left_cur])
			left_cur += 1
		else:
			result.append(right[right_cur])
			right_cur += 1
	if left_cur < left_max:
		result.extend(left[left_cur:])
	else: result.extend(right[right_cur:])
	return result
