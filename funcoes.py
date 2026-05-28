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
    return player
    
def monster1():
    monster1 = {
        "life": 20,
        "attack": 1,
        "gold": 10
    }
    return monster1

def shoop():
    itens_to_sell = [
        {"nome": "Iron Sword", "bonus_attack": 5, "price": 10},
        {"nome": "Dragon Slayer", "bonus_attack": 20, "price": 50},
        {"heal_potion": "Healing Potion", "healed_life": 10, "price": 5}
    ]

