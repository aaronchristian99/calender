import random

def genrandom():
    return random.randint(1, 6)
    
while True:
    c = input('enter "one" to roll a dice or enter "exit" to exit: ')
    if c == "one":
        print(f'number is: {genrandom()}')
    elif c ==  "exit":
        break
    else:
        print("please enter valide option.")
