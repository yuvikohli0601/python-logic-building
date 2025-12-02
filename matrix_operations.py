def add_matrices(a,b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def multiply_matrices(a,b):
    res = [[0]*len(b[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                res[i][j] += a[i][k] * b[k][j]
    return res

def transpose(m):
    return [list(row) for row in zip(*m)]

if __name__ == "__main__":
    A = [[1,2,3],[4,5,6]]
    B = [[7,8,9],[10,11,12]]
    print(add_matrices(A,B))
