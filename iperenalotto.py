from random import sample, randrange

#set a list of magic numbers
magic_numbers = [
    32, 33, 40, 41, 42, 44, 49, 51, 52,
    59, 60, 61, 62, 63, 72, 73, 74, 75,
    76, 77, 79, 81, 82, 85, 86, 87, 89
]

def schedina():
    """Random extract 6 numbers from my lucky numbers + a Superstar from the 90"""

    #extract 6 unique numbers random from magic list
    sestina = sorted(sample(magic_numbers,6))

    #pick a superstar random from the 90
    superstar = randrange(1,91)

    #print the result
    print(f"{sestina} SuperStar {superstar}")

giocate = int(input('Quante giocate vuoi fare?: '))

print('Ecco i tuoi numeri: ')

for _ in range(giocate):
    schedina()

