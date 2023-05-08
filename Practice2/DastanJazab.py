n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))


def determinant(matrix):
  if len(matrix) == 1:
    return matrix[0][0]
  if len(matrix) == 2:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
  det = 0 
  for j in range(len(matrix)):
    det += ((-1)**j) * matrix[0][j] * determinant(get_minor(matrix, 0, j))
  return det 
def get_minor(matrix, i, j):
  return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]


det = determinant(matrix)
print(det)