"""
Thông tin nhóm
Nguyễn Đăng Khánh, 20001931, K65A3MT&KHTT, MAT2407_2   
Bùi Trung Hiếu, 20001916, K65A3MT&KHTT, MAT2407_2 

Danh sách bài tập
- Bài 1. get_all_pieces(), get_white_pieces(), print_whites_viewpoint()
- Bài 2. get_random_element()
- Bài 3. get_filtered_elements()
- Bài 4. queens_move()

"""


from operator import truediv
import re
import random
import string

def get_all_pieces():
    chessboard = []
    for row_num in range(8, 0, -1):
        rank = row_num
        for col_num in range(0, 8, 1):
            file = chr(col_num + 97)
            chessboard.append(file + str(rank))
    return chessboard

#print(get_all_pieces()) #['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8', 'a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7', 'a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6', 'a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5', 'a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4', 'a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3', 'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2', 'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']

def get_white_pieces():
    whitePieces = []
    for row_num in range(0, 8, 1):
        rank = chr(row_num + 97)
        for col_num in range(0, 8, 1):
            file = col_num + 1
            if ((ord(rank) + col_num) % 2 == 0):
                whitePieces.append(rank + str(file))
    return whitePieces

#print(get_white_pieces()) #['a2', 'a4', 'a6', 'a8', 'b1', 'b3', 'b5', 'b7', 'c2', 'c4', 'c6', 'c8', 'd1', 'd3', 'd5', 'd7', 'e2', 'e4', 'e6', 'e8', 'f1', 'f3', 'f5', 'f7', 'g2', 'g4', 'g6', 'g8', 'h1', 'h3', 'h5', 'h7']

def print_whites_viewpoint():
    checkpoint = 1
    for i in range (0, len(get_all_pieces()), 1):
        print(get_all_pieces()[i], end = " ")
        checkpoint += 1
        if (checkpoint > 8):
            print()
            checkpoint = 1

#print_whites_viewpoint()

def get_random_element(coord: list):
    return random.choice(coord)

#print(get_random_element(get_all_pieces()))

def is_included(list: list, element):
    for i in list:
        if i == element:
            return True
    return False

def get_filtered_elements(A: list, B: list):
    C = []
    for i in A:
        if not is_included(B, i):
            C.append(i)
    return C

#print(get_filtered_elements({}, {1,2,3,4,5,6,7}))
#print(get_filtered_elements({1,2,3,4,5,6,7}, {2,4,6,8,10,12}))
#print(get_filtered_elements({1,2,3,4,5,6,7}, {13,14,15}))

def is_valid(coord):
    regex = '^[a-h][1-8]$'
    if (re.search(regex, coord)):
        return True
    else:
        return False

#print(is_valid("a1"))

def is_aligned(coord1, coord2):
    if (is_valid(coord1) and is_valid(coord2)):
        if (coord1[0] == coord2[0] or coord1[1] == coord2[1]):
            return True
        else:
            return False
    else:
        return False
        
#print(is_aligned("a3", "flexing tren circle k"))

def is_diagonal(coord1, coord2):
    if (is_valid(coord1) and is_valid(coord2)):
        if (abs(ord(coord1[0]) - ord(coord2[0])) == abs(ord(coord1[1]) - ord(coord2[1]))):
            return True
        else:
            return False
    else:
        return False
        
#print(is_diagonal("a3", "c2"))

def queens_move(coord):
    availableMove = []
    for i in range(0, len(get_all_pieces()), 1):
        if (is_diagonal(get_all_pieces()[i], coord) or is_aligned(get_all_pieces()[i], coord)):
            if (get_all_pieces()[i] != coord):
                availableMove.append(get_all_pieces()[i])
    return availableMove

#print(queens_move("a4")) #['a8', 'e8', 'a7', 'd7', 'a6', 'c6', 'a5', 'b5', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4', 'a3', 'b3', 'a2', 'c2', 'a1', 'd1']