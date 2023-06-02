from random import randint

def ArrayGenerate(n, Array):
    for i in range(0,n):
        Array.insert(i,randint(0,10))

def FindNumber(x, Array):
    min = Array[0]
    min_index = 0
    for i in range(0,len(Array)):
        if(abs(Array[i]-x) > abs(min - x)):
            min = Array[i]
            min_index = i
    return i


n = int(input("Введите размер массива: "))
Array = []
ArrayGenerate(n, Array)
print(Array)
number = int(input("Введите число X: "))
print(f"Ближайшее по величине к {number} число массива: {FindNumber(number, Array)} ")
