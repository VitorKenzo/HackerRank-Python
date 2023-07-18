import numpy

# getting the input
n, m = map(int, input().split())
rows = []
for i in range(n):
    rows.append(list(map(int, list(input().split()))))
    
# creating the numpy array from the list of integers rows
mat = numpy.array(rows, int)
# transpose
print(numpy.transpose(mat))
#flatten
print(mat.flatten())