import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	if len(a)==0 or len(a)*len(a[0])!= new_shape[0]*new_shape[1]:
		return []
	
	new_rows, new_cols = new_shape

	new_matrix = [[0] * new_cols for _ in range(new_rows)]


	flat_matrix = [val for row in a for val in row]

	for i in range(new_rows):
		for j in range(new_cols):
			new_matrix[i][j] = flat_matrix[i*new_cols + j]


	return new_matrix