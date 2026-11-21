import random
def create_hero(name):
    hp = random.randint(70,120)
    potions = random.randint(1,3)
    return {"name" : name, "hp" : hp, "potions" : potions}

def print_hero(hero,n):
    if n:
        print(f"""
Your hero name is {hero["name"]}
He has {hero["hp"]} hp
And he have {hero["potions"]} potions left
""")
    else:
        print(f"""
Yours enemies name is {hero["name"]}
He has {hero["hp"]} hp
""")
        
def enemy_waves():

    for name in ["Goblin", "Skeleton", "Orc", "Troll"]:
        enemy = create_hero(name)
        yield enemy


def fight(hero,enemy):
    while hero["hp"] > 0   and enemy["hp"] > 0 :
        act = input('(a)ttack or (p)otion')
        if act == 'p':
            if hero["potions"] > 0 :
                hero["hp"] += random.randint(10,25)
                hero["potions"]-=1
            else:
                print("You drank all yours potions,you'll attack automaticaly")
                act = 'a'
        if act == "a":
            damage = random.randint(15,30)
            enemy["hp"] -= damage
        if random.randint(0,1) == 0:
            damage = random.randint(5,15)
            hero["hp"] -= damage
        print_hero(hero,True)
        print_hero(hero,False)

def play():
    global gold
    gold = 0
    hero_name = input("Name your hero : ")
    hero = create_hero(hero_name)
    print_hero(hero,True)
    for enemy in enemy_waves():
        print_hero(enemy,False)
        fight(hero,enemy)



play()