import random
from playsound3 import playsound

def main_menu():
    playsound('sound_effect.mp3')
    print("Welcome to the RPG GAME!")
    print("Your journey beggins here...")
    print("*" * 40)



def player_function():
    player = {
        "life": 30,
        "attack": 5,
        "gold": 0,
        "inventory": []
    }
    print(f"The player has: {player['life']} HP")
    print(f"The player has: {player['attack']} attack")
    print(f"The player has: {player['gold']} gold")
    print(f"[1] Attack  [2]{player.get('inventory'), 'Vazio'}")
def monster1():
    monster1 = {
        "life": 20,
        "attack": random.randint(0,5),
        "gold": 10
    }
def shoop():
    shoop

