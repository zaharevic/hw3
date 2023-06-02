from random import randint

def ArrayGenerate(n, Array):
    for i in range(0,n):
        Array.insert(i,randint(0,10))

def FindNumber(x, Array):
    score = 0
    for i in range(0, len(Array)):
        if Array[i] == x:
            score += 1
    return score

n = int(input("Введите размер массива: "))
Array = []
ArrayGenerate(n, Array)
print(Array)
number = int(input("Введите число X: "))
print(f"Количество {number} в массиве = {FindNumber(number, Array)}")