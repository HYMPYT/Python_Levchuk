board = []
for i in range(8):
    row = ["EMPTY" for i in range(8)]
    board.append(row)
print(board)

for i in range(8):
    for j in range(8):
        print(board[i][j], end=" ")
    print()





# list_1 = [20, 30, 2, 5, 4, 6, 22, 14]
# to_find = 22
# found = False
# for i in range(len(list_1)):
#     found = list_1[i] == to_find
#     if found:
#         print(f"Your index {i}")
#         break
# else:
#     print("Not found")