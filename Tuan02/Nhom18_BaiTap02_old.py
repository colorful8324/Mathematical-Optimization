"""
-Thông tin
Nguyễn Đăng Khánh  20001931    K65A3MT&KHTT    MAT2407_2   
Bùi Trung Hiếu     20001916    K65A3MT&KHTT    MAT2407_2 

-Các bài tập đã làm được:
+Bài bắt buộc: 1-5
+Câu hỏi thêm: 1-3

"""


from operator import truediv
import re
import string

#Bai 1 + Cau hoi them 1
def is_valid(coord):
    regex = '^[a-h][1-8]$'
    if (re.search(regex, coord)):
        return True
    else:
        return False

#print(is_valid("a1"))

#Bai 2
def print_rooks_start():
    rooksStart = ["a1", "a8", "h1", "h8"]
    print(rooksStart)

#print_rooks_start()

def get_chessboard():
    chessboard = []
    for row_num in range(8, 0, -1):
        rank = row_num
        for col_num in range(0, 8, 1):
            file = chr(col_num + 97)
            chessboard.append(file + str(rank))
    return chessboard

#print(get_chessboard())

def get_white_pieces():
    whitePieces = []
    for row_num in range(0, 8, 1):
        rank = chr(row_num + 97)
        for col_num in range(0, 8, 1):
            file = col_num + 1
            if ((ord(rank) + col_num) % 2 == 0):
                whitePieces.append(rank + str(file))
    return whitePieces

#print(get_white_pieces())

#Cau hoi them 2
def print_whites_viewpoint():
    checkpoint = 1
    for i in range (0, len(get_chessboard()), 1):
        print(get_chessboard()[i], end = " ")
        checkpoint += 1
        if (checkpoint > 8):
            print()
            checkpoint = 1

#print_whites_viewpoint()

#Bai 3 + Cau hoi them 3
def is_aligned(coord1, coord2):
    if (is_valid(coord1) and is_valid(coord2)):
        if (coord1[0] == coord2[0] or coord1[1] == coord2[1]):
            return True
        else:
            return False
    else:
        return "Invalid input"
        
#print(is_aligned("a3", "Xin em dung nghi la anh khong yeu em, khi anh chang hua tuong lai minh toi dau"))

#Bai 4
def rooks_move(coordR):
    coord = coordR[1] + coordR[2]
    availableMove = []
    for i in range(0, len(get_chessboard()), 1):
        if (is_aligned(get_chessboard()[i], coord)):
            if (get_chessboard()[i] != coord):
                availableMove.append(get_chessboard()[i])
    return availableMove

#print(rooks_move("Ra2"))

# def euclidian_sorted_move(coord):
#     unsortedList = rooks_move(coord)
#     unsortedListAltered = []
#     for i in range (0, len(unsortedList), 1):
#         myList = list(unsortedList[i])
#         myList[0] = str(ord(myList[0]) - 96)
#         str1 = "".join(myList)
#         unsortedListAltered[i] = str1
#     return unsortedListAltered

# print(euclidian_sorted_move("Ra2"))

#Bai 5
def is_diagonal(coord1, coord2):
    if (is_valid(coord1) and is_valid(coord2)):
        if (abs(ord(coord1[0]) - ord(coord2[0])) == abs(ord(coord1[1]) - ord(coord2[1]))):
            return True
        else:
            return False
    else:
        return "Invalid input"

#print(is_diagonal("a3", "c2"))

def bishops_move(coordB):
    coord = coordB[1] + coordB[2]
    availableMove = []
    for i in range(0, len(get_chessboard()), 1):
        if (is_diagonal(get_chessboard()[i], coord)):
            if (get_chessboard()[i] != coord):
                availableMove.append(get_chessboard()[i])
    return availableMove

#print(bishops_move("Bb2"))
