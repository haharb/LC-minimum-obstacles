def minimumObstacles(grid):
    moves = [(1, 0), (-1, 0), (0, -1), (0, 1)]

    def canReach(r, c):
        if not (0 <= r < len(grid)) or not (0 <= c < len(grid[0])) or (grid[r][c] == 1):
            return False

        if (r, c) == (len(grid) - 1, len(grid[0]) - 1):
            return True
               
        grid[r][c] = 1

        res = False

        for dr, dc in moves:
            res = res or canReach(r + dr, c + dc)

        grid[r][c] = 0

        return res

    userInput = input("Enter points to check\n\n")
    while userInput != "q":
        nums = userInput.split()
        try:
            num1 = int(nums[0])
            num2 = int(nums[1])
            print(canReach(num1, num2))
            print(f"{grid} at ({num1}, {num2})")
            userInput = input("Enter points to check\n\n")
        except ValueError:
            print("WRONG VALUE")


#minimumObstacles([[0,1,1],[1,1,0],[1,1,0]])
minimumObstacles([[0,1,0,0,0],[0,1,0,1,0],[0,1,0,1,0]])

