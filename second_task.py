
f = open('task2.txt','r')

N_M_Q = f.readline().split()
AN_cards = f.readline().split()
BM_cards = f.readline().split()

N, M, Q = list(map(int, N_M_Q))

cards_diversity = dict()

for card in AN_cards:
    if card in cards_diversity.keys():  # if A-player have a card, I add it to dict
        cards_diversity[card] += 1
    else:
        cards_diversity[card] = 1

for card in BM_cards:
    if card in cards_diversity.keys():  # if B-player have a card, I remove it from dict
        cards_diversity[card] -= 1
    else:
        cards_diversity[card] = -1


def count_diversity(div_dict):  # func to count how much diverse cards A&B have
    div_sum = 0
    for i in div_dict.values():
        div_sum += abs(i)

    return div_sum


for i in range(Q):
    sign, player, card = f.readline().split()
    sign = int(sign)
    player = 1 if player == "A" else -1

    # A-player - add card, B-player remove card if sign == -1, do the opposite
    if card in cards_diversity.keys():
        cards_diversity[card] += sign*player
    else:
        cards_diversity[card] = player

    print(count_diversity(cards_diversity), end=" ")


f.close()
