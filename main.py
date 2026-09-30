import random

player = {
    "name": "Hero",
    "health": 100,
    "attack": 20
}

enemy = {
    "name": "Goblin",
    "health": 80,
    "attack": 15
}

print("==================== RPG BATTLE ====================")

def show_stats(player, enemy):
    print(f"{player['name']} HP: {player['health']}")
    print(f"{enemy['name']} HP: {enemy['health']}")



def player_attack(enemy,player):
   print("You chose Attack!")
   damage = calculate_damage(player["attack"])
   enemy["health"] = enemy["health"] - damage
   print(f"{player['name']} dealt {damage} damage!")




def enemy_attack(player,enemy):
  print("Goblin have attacked!!")
  damage = calculate_damage(enemy["attack"])
  player["health"] = player["health"] - damage

  print(f"{enemy['name']} dealt {damage} damage!")


def calculate_damage(attack):
    damage = random.randint(attack - 5, attack)
    return damage
  



def check_winner(player, enemy):
  if player["health"] <= 0:
    print("🎉 YOU Lose! Goblin defeated You!")
    return enemy

  elif enemy["health"] <= 0:
    print("🎉 YOU WIN! You defeated Goblin!")
    return player

def potion(player):
    old_health = player["health"]
    if player["health"] < 100:
        player["health"] = min(player["health"] + 20, 100)
        healed = player["health"] - old_health
        print(f"HERO IS HEALED! {healed} HP")

    else:
        print("cannot heal")

    


def battle(player, enemy):

  while True:
    
    show_stats(player,enemy)
  
    player_option = input("What do you want to do? Attack or Potion: ").lower()

    
  
    if player_option == "attack":
      player_attack(enemy,player)
      

  
    elif player_option == "potion":
      potion(player)
  
  
    else:
      print("incorrect option selected")
      continue


              
    if check_winner(player, enemy):
      break


    enemy_attack(player,enemy)

              
    if check_winner(player, enemy):
      break




def game():
  battle(player,enemy)


game()



    
    
  
  