def shortenRow(row, el): return list(map(lambda x: x / el, row))

def convertToFloat(el): return list(map(float, el))

def getNormalMatrix(matrix, num):
    for i in range(num, len(matrix)):
        if matrix[num][num] != 0:
            break
        matrix[num], matrix[i] = matrix[i], matrix[num]


def isBad(matrix, i):
    if matrix[i].count(0.0) == len(matrix[i]) - 1 and matrix[i][len(matrix) - 1] != 0.0:
        return False
    return True


def gaus(matrix):
    for i in range(1, len(matrix) ):
        if matrix[i - 1][i - 1] == 0:
            getNormalMatrix(matrix, i-1)
        if not isBad(matrix, i-1):
            return False, matrix
        matrix[i - 1] = shortenRow(matrix[i - 1], matrix[i - 1][i - 1])
        for j in range(i, len(matrix)):
            kof = matrix[j][i-1]
            matrix[j] = list(map(lambda x, y: -x + y, list(map(lambda x: kof * x, matrix[i-1])), matrix[j]))
    for i in range(len(matrix) - 1, 0, -1):
        if matrix[i][i] != 0:
            if not isBad(matrix, i):
                return False, matrix
            matrix[i] = shortenRow(matrix[i], matrix[i][i])
            for j in range(i - 1, -1, -1):
                kof = matrix[j][i]
                matrix[j] = list(map(lambda x, y: -x + y, list(map(lambda x: kof * x, matrix[i])), matrix[j]))
    return True, matrix

def readMatrix():
    with open('data.txt', 'r') as file:
        return list(map(convertToFloat, [line.split() for line in file]))


def main():
    matrix = [(-2 ,3 ,-1),
                (-2 ,-1 ,-4)]
    flag, matrix = gaus(matrix)
    if not flag:
        print("Система несовместна")
    print(matrix[0][2])

if __name__ == '__main__':
    main()