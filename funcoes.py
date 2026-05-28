import random
from playsound3 import playsound

def main_menu():
    playsound('sound_effect.mp3')
    print("Welcome to the RPG GAME!")
    print("Your journey beggins here...")
    print("-" * 40)

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

def shop(player):
    itens_to_sell = [
        {"name": "Iron Sword", "bonus_attack": 5, "price": 10},
        {"name": "Dragon Slayer", "bonus_attack": 20, "price": 50},
        {"name": "Healing Potion", "healed_life": 10, "price": 5}
    ]
    print("Welcome to Bardo's SHOP!")
    print("-" * 40)
    print(f"[1] Sword: {itens_to_sell[0]['name']} / PRICE: {itens_to_sell[0]['price']}")
    print(f"[2] Sword: {itens_to_sell[1]['name']} / PRICE: {itens_to_sell[1]['price']}")
    print(f"[3] Potion: {itens_to_sell[2]['name']} / PRICE: {itens_to_sell[2]['price']}")
    print("[5] Leave")

    shop_choice = int(input("What you need for your journey? "))
    if shop_choice == 5:
        return player
    
    elif player['gold'] < itens_to_sell[shop_choice - 1]['price']:
        print("You dont have money for this.")
        return player
    
    elif shop_choice == 1:
        print(f"You will need that: {itens_to_sell[0]}")
        player['attack'] += itens_to_sell[0].get('bonus_attack')
        player['gold'] -= itens_to_sell[0].get('price')
        player['inventory'].append(itens_to_sell[0]['name'])
        return player
    elif shop_choice == 2:
        print("I see someone needs power...")
        player['attack'] += itens_to_sell[1].get('bonus_attack')
        player['gold'] -= itens_to_sell[1].get('price')
        player['inventory'].append(itens_to_sell[1]['name'])
        return player
    elif shop_choice ==3:
        print(f"Remember this.{itens_to_sell[2]['name']}")
        player['gold'] -= itens_to_sell[2]['price']
        player['inventory'].append(itens_to_sell[2]['name'])
        return player

def potion(player):
    if player['inventory'] == 'Healing Potion':
        player['life'] += 10
        player['inventory'].remove('Healing Potion')
        print(f"You healed +10 HP, your HP now: {player['life']}")
    else:
        print("You dont have this item.")
    return player
