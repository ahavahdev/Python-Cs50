from cs50 import get_int

scores = []
for i in range(3):
    score = get_int("score: ")
    scores.append(score)
    #ou
    #scores += [score]


avarage = sum(scores) / len(scores)
print(f"A média é: {avarage}")

    
    
    