def solution (score) :
    scores = []
    for i in range (101) :
        scores.append(0)
    
    for i in score.split() :
        scores[int(i)] += 1

    max_ = max (scores)
    return max_.index(max_)


def main () :
    n = int (input ())
    for i in range (n) :
        i = input()
        score = input()
        print ("#", i+1, solution(score))


main ()