def creator(height,width):
    mat = []
    for row in range(height):
        mat.append([])
        for column in range(width):
            mat[row].append(' ')
    return mat