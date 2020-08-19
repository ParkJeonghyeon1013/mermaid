import random
from c1_character import mermaid

knife = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

for i in range (5):
    child_pick = random.choice(knife)
    print("knife 리스트는: {0}".format(knife))
    print(child_pick)
    knife.remove(child_pick)
    print("삭제된 knift 리스트는: {0}\n".format(knife))