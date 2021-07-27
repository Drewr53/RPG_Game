from classes.game import Person, bcolors

magic = [{"name": "Fire", "cost": 10, "dmg": 60},
         {"name": "Thunder", "cost": 10, "dmg": 60},
         {"name": "Blizzard", "cost": 10, "dmg": 60}]


player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

running = True

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS" + bcolors.ENDC)

while running:
    print("=======================")
    player.choose_action()
    choice = input("Choose Action: ")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "points of damage.   Enemy HP:", enemy.get_hp())
    elif index == 1:
        player.choose_magic()
        magic_choice = input("Choose Magic: ")
        magic_index = int(magic_choice) - 1
        magic_dmg = player.generate_spell_damage(magic_index)
        player.reduce_mp(int(player.get_spell_mp_cost(magic_index)))
        enemy.take_damage(magic_dmg)
        print("You attacked for", magic_dmg, "points of damage. You have ", player.get_mp, "Enemy HP:", enemy.get_hp())
