def ScoreCounter(word):
    count = 0
    list_score= {1:"AEIOULNSTRАВЕИНОРСТ",
                2:"DGДКЛМПУ",
                3:"BCMPБГЁЬЯ",
                4:"FHVWYЙЫ",
                5:"KЖЗХЦЧ",
                8:"JXШЭЮ",
                10:"QZФЩЪ"}
    for i in word:
        for score, letter in list_score.items():
            if i in letter:
                count += score
    return count

word = input("Введите слово: ")
score = ScoreCounter(word.upper())
print(f"Количество очков: {score}")
