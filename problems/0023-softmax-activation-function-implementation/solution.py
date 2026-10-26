import math

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    results = []
    sum = 0
    max_score = max(scores)
    for i in range(len(scores)):
        sum+= math.exp(scores[i]-max_score)

    for i in range(len(scores)):
        results.append((math.exp(scores[i]-max_score))/ sum)
    
    return results