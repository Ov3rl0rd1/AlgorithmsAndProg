#Задача № 6
#На шахматной доске NxN находятся M ладей (ладья бьет клетки по той же вертикали или горизонтали до ближайшей занятой). Определите сколько пар ладей бьют друг друга. Ладьи задаются парой чисел I и J (индексы), обозначающие координаты клетки. Разработайте функцию для решения данной задачи.

def count_attacking_rooks(n, rooks):
    attacking_pairs = 0
    
    for i in range(len(rooks)):
        for j in range(i + 1, len(rooks)):
            row1, col1 = rooks[i]
            row2, col2 = rooks[j]
            
            if row1 == row2:
                min_col, max_col = min(col1, col2), max(col1, col2)
                blocked = False
                
                for k in range(len(rooks)):
                    if k != i and k != j:
                        row_k, col_k = rooks[k]
                        if row_k == row1 and min_col < col_k < max_col:
                            blocked = True
                            break
                
                if not blocked:
                    attacking_pairs += 1
            
            elif col1 == col2:
                min_row, max_row = min(row1, row2), max(row1, row2)
                blocked = False
                
                for k in range(len(rooks)):
                    if k != i and k != j:
                        row_k, col_k = rooks[k]
                        if col_k == col1 and min_row < row_k < max_row:
                            blocked = True
                            break
                
                if not blocked:
                    attacking_pairs += 1
    
    return attacking_pairs

rooks1 = [(0, 0), (3, 0), (3, 2)]
print(f"Пример 1 (доска 5x5, 3 ладьи):")
print(f"Позиции ладей: {rooks1}")
print(f"Пар, бьющих друг друга: {count_attacking_rooks(5, rooks1)}")

rooks2 = [(0, 0), (1, 0), (3, 0), (3, 2), (4, 3), (2, 4)]
print(f"\nПример 2 (доска 5x5, 6 ладей):")
print(f"Позиции ладей: {rooks2}")
print(f"Пар, бьющих друг друга: {count_attacking_rooks(5, rooks2)}")