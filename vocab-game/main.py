from flashcard import *
from vocab_set import *




dictionary = [] 
vocab_sets = [] 
with open('/usr/share/dict/words', 'r') as f:
    dictionary = f.read().split()

def is_word(word):
    if word in dictionary:
        return True
    else:
        return False

def select_set(sel_set):
    if vocab_sets:
        for setz in sets:
            if setz.title == sel_set:
                return setz
def is_set(sel_set):
    if sel_set in vocab_sets.title:
        return True
    else:
        return False

if __name__ == '__main__':
    option= ""
    while (option != 'q'):
        print("Welcome to the voca Builder, what would you like to do")
        print("Menu: /n1. Create Set /n2. Add Vocab /n3. Play Game")
        option = int(input("> " ))
        if option == 1:
            set_name = input("What would you like to name the set?")
            if(not is_set):
                flash_set  = VocabSet(set_name)
                vocab_sets.append(flash_set)
        if option == 2:
            for item in vocab_sets:
                print(item.title)
            vocab_set = select_set(vocab_sets, input("Which one would you like to selected"))
            end_pos = input("How many words would you like to input")
            for _ in range(end_pos):
                name = input("What is the word")
                if is_word(name):
                    definition = input("Name: {}. Definition: ".format(name))
                    vocab_set.add(VocabCard(name, definition))
                else:
                    print("Sorry that is not a word")

