#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
	new_matrix = matrix.copy()
	for i in range(len(new_matrix)):
		for j in range(len(new_matrix[i])):
			new_matrix[i][j] **= 2
	return new_matrix
