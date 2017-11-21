import sys
import textwrap
"""
Cowsay python is a copy of the system cowsay progam. User can input a sentence from the terminal and the cow will print out the word
"""

def cowsay(text, length=20):
    cow_arr = []
    top_bot= '-'*length
    print(top_bot)
    text = textwrap.fill(text,length)
    print(text)
    print(top_bot)
    print(build_cow())

def build_cow():
    return """
         \   ^__^
          \  (oo)\_______
             (__)\       )\/\\
                 ||----w |
                 ||     ||
    """
print(cowsay(" ".join(sys.argv[1:])))
