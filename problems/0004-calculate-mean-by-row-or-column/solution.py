def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []
	if mode =='row':
		for i in range(len(matrix)):
			means.append(sum(matrix[i])/len(matrix[i]))
	else:
		for i in range(len(matrix[0])):
			colsum = sum([matrix[j][i] for j in range(len(matrix))])/len(matrix)
			means.append(colsum)
	return means