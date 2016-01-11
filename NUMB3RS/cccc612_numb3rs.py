'''
author: Minchul Jung(ccc612@gmail.com)
problem: NUMB3RS
link: https://algospot.com/judge/problem/read/NUMB3RS
solution description
    1) push 1.0 probability on start town
    2) retrive last probability dictionary (prob)
        2-1) calculate next probability
            [current towns probability] * 1.0 / [sum of roads to next town]
        2-2) if there is aready calculated probability, sum up each probability
    3) repeat 2) until last day
    4) return probabilities want to know (r_town)
'''

def get_numb3rs(towns, r_town, start, day):
    prob = {start:1.0}

    for i in xrange(day):
        tmp_prob = {}
        for town in prob.keys():
            tot = float(sum(towns[town]))
            for index, isRoad in enumerate(towns[town]):
                if isRoad == 1:
                    c_prob = prob[town] * (1.0 / tot)
                    if index not in tmp_prob:
                        tmp_prob[index] = c_prob
                    else:
                        tmp_prob[index] += c_prob
        prob = tmp_prob

    result = []
    for t in r_town:
        if t in prob:
            result.append(prob[t])
        else:
            result.append(0.0)

    return result


# process input
tc = int(raw_input())

for i in xrange(tc):
    town, day, start = map(int, raw_input().split())

    # read town roads
    towns = []
    for i in xrange(town):
        towns.append( map(int, raw_input().split()) )

    raw_input() # pass the number of town to print result
    r_town = map(int, raw_input().split())

    result = get_numb3rs(towns, r_town, start, day)

    print(" ".join( map(lambda x : "%.8f" % round(x, 8), result)))
