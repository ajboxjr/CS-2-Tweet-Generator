import sys

def cowsay(text, length=20):
    cow_arr = []
    if len(text) > length:
        top_bot = '-'*length+10
        for char in text:
            for in range(length):
                cow_arr.
        for _ in range(length):
            
    else:
        top_bot= '-'*length
    print(top_bot)
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
print(cowsay('hello'))
