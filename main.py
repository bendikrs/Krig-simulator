import random, time
import matplotlib.pyplot as plt

try:
    import pygame.mixer
    pygame.mixer.init()
    pygame.mixer.music.load("runnning_in_the_90s.mp3")
    pygame.mixer.music.play(-1, 7.9)
    time.sleep(5.1)
except:
    pass


def makeDeck(): #returnerer ei liste med kort
    deck = []
    for i in range(13):
        for n in range(4):
            deck.append(i+2)
    return deck
def dealCards(): # Returnerer to lister
    handA, handB = [], []
    deck = makeDeck()
    for i in range(len(deck)):
        temp = random.choice(deck)
        if i % 2:
            handA.append(temp)
        else:
            handB.append(temp)
        deck.remove(temp)
    return handA, handB
def compareCard(a, b): # a, b, w
    if a > b:
        return "a"
    if b > a:
        return "b"
    else:
        return "w"
def renewHand(hand, deck):
    if len(hand) == 0:
        hand = deck
        random.shuffle(hand)
        deck = []
    return hand, deck
def war(deck1, deck2, hand1, hand2, n=4, done=False):
    if done:
        return deck1, deck2, hand1, hand2

    if len(hand1) <= n:
        temp = hand1
        hand1 = []
        hand1, deck1 = renewHand(hand1, deck1)
        temp.reverse()
        for i in temp:
            hand1.insert(0, i)

    if len(hand2) <= n:
        temp = hand2
        hand2 = []
        hand2, deck2 = renewHand(hand2, deck2)
        temp.reverse()
        for i in temp:
            hand2.insert(0, i)

    if len(hand1) <= n:
        hand1 = []
        return deck1, deck2, hand1, hand2

    if len(hand2) <= n:
        hand2 = []
        return deck1, deck2, hand1, hand2



    #print("War handA", hand1[:5], "War handB", hand2[:5])
    if compareCard(hand1[n], hand2[n]) == "a":
        for i in range(n):
            deck1.append(hand1[0])
            deck1.append(hand2[0])
            del hand1[0]
            del hand2[0]
        done = True
    elif compareCard(hand1[n], hand2[n]) == "b":
        for i in range(n):
            deck2.append(hand1[0])
            deck2.append(hand2[0])
            del hand1[0]
            del hand2[0]
        done = True
    else:
        n += 4
        deck1, deck2, hand1, hand2 = war(deck1, deck2, hand1, hand2, n, False)
    return deck1, deck2, hand1, hand2
def minutt_sekund(sekunder):
    minutes = sekunder // 60
    sekunder = sekunder - minutes*60
    if sekunder < 10:
        sekunder = "0" + str(sekunder)

    tid = str(minutes) + ":" + str(sekunder)
    return tid #mm:ss


def main():
    plotListA, plotListB = [], []
    handA, handB = dealCards()
    deckA, deckB = [], []
    running, counter = True, 0
    krigCount = 0

    while running:
        #print("deckA",deckA[:5], "deckB", deckB[:5])
        #print("handA", handA[:5], "handB", handB[:5])
        if compareCard(handA[0], handB[0]) == "a":
            deckA.append(handA[0])
            deckA.append(handB[0])
            del handA[0]
            del handB[0]
        elif compareCard(handA[0], handB[0]) == "b":
            deckB.append(handA[0])
            deckB.append(handB[0])
            del handA[0]
            del handB[0]
        else:
            #print("jadda!!!!!!!!!!!!!!!")
            krigCount += 1
            deckA, deckB, handA, handB = war(deckA, deckB, handA, handB)

        handA, deckA = renewHand(handA, deckA)
        handB, deckB = renewHand(handB, deckB)

        counter += 1
        plotListA.append(len(handA)+len(deckA))
        plotListB.append(len(handB)+len(deckB))



        print("Player 1 " + "-"*(len(handA)+len(deckA)) + "|" + "-"*(len(handB)+len(deckB)) + " Player 2" )
        time.sleep(0.05)

        if not handA:
            print("Spelar 1 vann etter", counter, "forsøk og", krigCount, "krigar.")
            print("Det tilsvarer", minutt_sekund(round(counter*4)), "mm:ss")
            plt.plot([x for x in range(len(plotListB))], plotListB, 'ro')
            plt.show()
            running = False
        if not handB:
            print("Spelar 1 vann etter", counter, "forsøk og", krigCount, "krigar.")
            print("Det tilsvarer", minutt_sekund(round(counter*4)), "mm:ss")
            plt.plot([x for x in range(len(plotListA))], plotListA, 'ro')
            plt.show()
            running = False

        # if not handA:
        #     return "Bendik"
        #     running = False
        # if not handB:
        #     return "Ole Bendik"
        #     running = False


main()

# wins = {"Player1": 0, "Player2": 0}
# for i in range(100000):
#     win = main()
#     wins[win] += 1
#
# for key, value in wins.items():
#     print(str(key) + ": " + str(value))
