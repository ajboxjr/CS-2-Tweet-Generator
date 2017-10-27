import sys
import random
listz = sys.argv[1:]

def reverse(word):
    for word  in range(len(word)-1):


reverse("The reverse string {}".format(listz[::-1]))
words_arr = []
while len(listz) > 0:
    rand_index = random.randint(0,len(listz)-1)
    words_arr.append(listz.pop(rand_index))
    
print(" ".join(words_arr))
