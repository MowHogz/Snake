def matrix_cre(height,width):
    mat = []
    for i in range(height):     #for every row 
        mat.append([])          #add row
        mat[i].append("|")      #add | at the start of the row
        for j in range(width):  #for every unit in the 
            mat[i].append(' ')  #add an empty space 
        mat[i].append("|")      #and another | at the end of every row
    mat.insert(0,[])
    for c in range(width+2):
        mat[0].append("-")
    mat.append([])
    for c in range(width+2):
        mat[height+1].append("-") #this works because really the width should be width-1 but here we added a row after width 
    return mat