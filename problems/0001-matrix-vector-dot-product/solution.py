def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	if len(a)!=len(b):
		return -1
	
	result = []
	for row in a:
		element = sum(m*n for m,n in zip(row,b))
		result.append(element)

	return result
	pass