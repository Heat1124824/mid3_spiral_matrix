def create_spiral_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    top = 0
    left = 0
    bottom = n - 1
    right = n - 1
    cnt = 1

    while top <= bottom and left <= right:
        for i in range(top, bottom + 1):
            matrix[i][left] = cnt
            cnt += 1
        left += 1

        for i in range(left, right + 1):
            matrix[bottom][i] = cnt
            cnt += 1
        bottom -= 1

        for i in range(bottom, top - 1, -1):
            matrix[i][right] = cnt
            cnt += 1
        right -= 1

        for i in range(right, left - 1, -1):
            matrix[top][i] = cnt
            cnt += 1
        top += 1

    return matrix

def main():
    n = int(input("n = "))
    spiral_matrix = create_spiral_matrix(n)
    for row in spiral_matrix:
        print(row)

if __name__ == "__main__":
    main()
