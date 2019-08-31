import keyboard
import os
import time 
def Printm(matrix):
    text = ""
    for row in matrix:
        for unit in row:
            text += unit
        text += "\n"
    print text
def screen_config(speed,height,width):
    d = ""
    h = 1
    w = 1
    while not 'q' in d:
        d = []
        for i in range(5):
            time.sleep(0.001)
            d = press(d)
        if 'u' in d and h > 1:
            h += -1
        if 'd' in d and h < height:
            h += 1
        if 'l' in d and w > 1:
            w += -1
        if 'r' in d and w < width:
            w += 1
        #now creating a matrix to the sizes of w and h
        matrix = cre_mat(h,w)
        #now 'decorating' the edges with stars
        for row_n in range(h):
            matrix[row_n][w-1] = '*'
        for col_n in range(w):
            matrix[h-1][col_n] = '*'
        os.system("cls")
        Printm(matrix)
    #print w
    #print h
    return w,h
def cre_mat(height,width):#creates a matrix according to height and width
    matrix = []
    for row in range(height):
        row = []
        for column in range(width):
            row.append(' ')
        matrix.append(row)
    return matrix


def press(c_list):#adds to c_list all the directions being pressed 
    if keyboard.is_pressed('w'):
        if 'u' in c_list:
            pass
        else:
            c_list.append('u')
    if keyboard.is_pressed('s'):
        if 'd' in c_list:
            pass
        else:
            c_list.append('d')
    if keyboard.is_pressed('d'):
        if 'r' in c_list:
            pass
        else:
            c_list.append('r')
    if keyboard.is_pressed('a'):
        if 'l' in c_list:
            pass
        else:
            c_list.append('l')
    if keyboard.is_pressed('q'):
        if 'q' in c_list:
            pass
        else:
            c_list.append('q')
    return c_list