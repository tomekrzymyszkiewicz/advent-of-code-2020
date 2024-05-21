with open("input.txt", "r") as f:
    trees_map = f.read().split("\n")

current_row = 1
current_col = 3
X_count = 0
while current_row < len(trees_map):
    if trees_map[current_row][current_col % len(trees_map[0])] == "#":
        X_count += 1
    current_row += 1
    current_col += 3

print(X_count)
