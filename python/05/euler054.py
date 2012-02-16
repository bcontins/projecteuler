from collections import Counter

val_high = 0
val_onepair = 1000000
val_twopair = 2000000
val_threekind = 3000000
val_straight = 4000000
val_flush = 5000000
val_full = 6000000
val_fourkind = 7000000
val_straightflush = 8000000

val_cards={'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}

def evalhand(hand):

    for card in range(2, 10):
        val_cards[str(card)] = card

    values = Counter([card[0] for card in hand]).most_common(3)
    colors = Counter([card[1] for card in hand]).most_common(1)

    straight = sorted([val_cards[card[0]] for card in hand])

    isstraight = (straight == range(straight[0], straight[0]+5))

    if isstraight and colors[0][1] == 5:
        # Add lowest card to compare straights
        return val_straightflush + straight[0]
    elif isstraight:
        # Add lowest card to compare straights
        return val_straight + straight[0]
    elif colors[0][1] == 5:
        # Add highest card to compare flushes
        return val_flush + straight[-1]
    elif values[0][1] == 4:
        # Add card present four times
        return val_fourkind + val_cards[values[0][0]]
    elif values[0][1] == 3 and values[1][1] == 2:
        # Add card present three times
        return val_full + val_cards[values[0][0]]
    elif values[0][1] == 3:
        # Add card present three times
        return val_threekind + val_cards[values[0][0]]
    elif values[0][1] == 2 and values[1][1] == 2:
        # Add card of highest pair and then card of lowest pair and then remaining card
        bestpair = max(val_cards[values[0][0]], val_cards[values[1][0]])
        otherpair = min(val_cards[values[0][0]], val_cards[values[1][0]])
        return val_twopair + bestpair * 15**2 + otherpair * 15 + val_cards[values[2][0]]
    elif values[0][1] == 2:
        return val_onepair + val_cards[values[0][0]]
    else:
        return val_high + sum([straight[idx]*(15**idx) for idx in range(5)])

if __name__ == '__main__':
    result = 0

    f = open("./054/poker.txt", "r")

    for line in f.readlines():
        handone = line.split(' ')[:5]
        handtwo = line.strip().split(' ')[5:]

        #print evalhand(handone)
        #print evalhand(handtwo)

        if evalhand(handone) > evalhand(handtwo):
            result += 1

    print "RESULT=%d" % (result)

