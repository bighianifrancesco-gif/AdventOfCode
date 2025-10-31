filename = "input.txt"

try:
    with open(filename, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    raise SystemExit(1)
except Exception as e:
    print("An error occurred while reading the file:", e)
    raise SystemExit(1)

grid = [list(line) for line in lines]
n = len(grid)
m = len(grid[0])

# word = "XMAS"

# directions = [
#     (-1, -1), (-1, 0), (-1, 1),
#     (0, -1),           (0, 1),
#     (1, -1),  (1, 0),  (1, 1)
# ]

# count = 0

# for i in range(n):
#     for j in range(m):
#         if grid[i][j] != word[0]:
#             continue
#         for di, dj in directions:
#             x, y = i, j
#             matched = True
#             for k in range(1, 4):
#                 x += di
#                 y += dj
#                 if not (0 <= x < n and 0 <= y < m and grid[x][y] == word[k]):
#                     matched = False
#                     break
#             if matched:
#                 count += 1

# print(count)

count = 0

for i in range(1, n-1):        
    for j in range(1, m-1):
        if grid[i][j] != "A":  
            continue

        tl = grid[i-1][j-1]    
        br = grid[i+1][j+1]    
        tr = grid[i-1][j+1]    
        bl = grid[i+1][j-1]    

        diag1 = (tl == "M" and br == "S") or (tl == "S" and br == "M")
        diag2 = (tr == "M" and bl == "S") or (tr == "S" and bl == "M")

        if diag1 and diag2:
            count += 1

print("Total X-MAS occurrences:", count)

