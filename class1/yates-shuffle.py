import random

def fisher_yates_shuffle(array):
    """Return a new array of random words poped from inputted dictionary"""
    shuffled_arr = []
    while array:
        popped_word = array.pop(random.randint(0,len(array)-1))
        shuffled_arr.append(array.pop(random.randint(0,len(array)-1)))
    return shuffled_arr


arr = "this is the random arr that i would like to shuffle".split()
new_arr = fisher_yates_shuffle(arr)
print(new_arr)

