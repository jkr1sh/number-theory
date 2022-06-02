import math

i = 1

squares = []
triangles = []

while i <= 10000:
    tri = ((i*(i+1))/2)
    tri_trunc = math.trunc(tri)
    triangles.append(tri_trunc)
    sq = (i*i)
    squares.append(sq)
    i += 1

common = set(squares).intersection(triangles)
common_sorted = sorted(common)

print(f'{common_sorted}')
