'''This script provides you with a single, high-speed monkey to type the
complete works of Shakespeare. He's a tad hit or miss...'''
import random
import string
import time
import re

def startTyping(text):
    monkeyTyped = ''
    while monkeyTyped == '' or not re.search(monkeyTyped, text) == None:
        monkeyTyped = monkeyTyped + (random.choice(string.ascii_lowercase + string.digits))
    # The last thing that the monkey typed ruined it so remove it and return
    return (monkeyTyped[:-1])

comp_works = open('Shakespeare.txt', 'r')
s = comp_works.read()
comp_works.close()
# Convert to lowercase and remove all punctuation to reduce the search space a bit...(slight cheat!)
s = s.lower()
remove_punc = re.compile('[%s]' % re.escape(string.punctuation))
shakespeare = remove_punc.sub('', s)
totalKeyPresses = 0
monkeyProgress = ''
maxLenSoFar = 0
bestSoFar = ''
hits = dict()
print("Go on little monkey...type!\n")
start = time.time()
# Infinite loop ... unless the monkey does it!
while len(monkeyProgress) != len(shakespeare):
    monkeyProgress = startTyping(shakespeare)
    totalKeyPresses = totalKeyPresses + len(monkeyProgress) + 1
    # Check in with progress if he gets past 4 characters
    if len(monkeyProgress) > 4:
        if len(monkeyProgress) in hits:
            hits[len(monkeyProgress)] += 1
        else:
            hits[len(monkeyProgress)] = 1
        if len(monkeyProgress) > maxLenSoFar:
            maxLenSoFar = len(monkeyProgress)
            bestSoFar = "'{}'".format(monkeyProgress)
        monkeyProgress = "'{}'".format(monkeyProgress)
        print(totalKeyPresses, monkeyProgress, "   ---> Best so far:: {} (Length={})".format(bestSoFar, maxLenSoFar))
    # Let us know that he is still going!
    if totalKeyPresses % 1000 == 0:
        if totalKeyPresses % 10000 == 0:
            now = time.time() - start
            print("\nSummary of progress so far::")
            print("\n...The monkey has been typing for {0:.2f} minutes".format(now/60))
            for length, freq in hits.items():
                print("\tMatch length of {} --> {} times.".format(length, freq))
            print("\n")
