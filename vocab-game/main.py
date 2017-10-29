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
        for set_item in vocab_sets:
            if set_item.title == sel_set:
                return set_item
        return False

def is_set(sel_set):
    for set_item in vocab_sets:
        if sel_set == set_item.title:
            return True
        else:
            return False
def view_sets():
    for collection in vocab_sets:
        print(collection)

if __name__ == '__main__':
    option= ""
    while (option != 'q'):
        print("Welcome to the voca Builder, what would you like to do")
        print("Menu: /n1. Create Set /n2. Add Vocab /n3. Play Game")
        option = int(input("> " ))
        if option == 1:
            set_name = input("What would you like to name the set?")
            if is_set(set_name):
                print("Sorry that is already a set")
            else:
                flash_set  = VocabSet(set_name)
                vocab_sets.append(flash_set)
                print("{} has been set".format(flash_set.title))
        if option == 2:
            view_sets()
            vocab_set = select_set(input("Which one would you like to selected"))
            if(is_set(flash_set)):
                end_pos = int(input("How many words would you like to input"))
                for _ in range(end_pos):
                    name = input("What is the word")
                    if is_word(name):
                        definition = input("Name: {}. Definition: ".format(name))
                        vocab_set.add_card(VocabCard(name, definition))
                    else:
                        print("Sorry that is not a word")
            else:
                print("{} is already a set".format(flash_set))

