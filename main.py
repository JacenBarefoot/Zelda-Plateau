from random import choice
from dataclasses import dataclass

@dataclass
class Been:
    oman: int
    ja: int
    owa: int
    keh: int


starting_point = "Shrine Of Resurrection"

resurrection = """ -You wake up. Around, you notice the walls have different symbols on them. The room is also very blue. The door to the shrine opens. After realizing where you are, you grab your clothes, sword, and sheath. You then exit the shrine. Outside, you see green flatlands, dark green forests, and a big mountain with snow on it.

You can go to:
- Wild
"""


def wild(been: Been):
    print(
        f""" -You see green flatlands, dark green forests, and a big mountain with snow on it.

You can go to:""")
    if been.oman == 0:
        print("- Oman Au Shrine")
    if been.ja == 0:
        print("- Ja Baij Shrine")
    if been.owa == 0:
        print("- Owa Daim Shrine")
    if been.keh == 0:
        print("- Keh Namut Shrine")
    print("- Fight")


omanau = """ - You walk into a doorway and see an elevator. You take the elevator down and you see a giant blue and gold room with gold squares on the ground, metal plates on the ground for bridges, and metal boxes laying around. You see a trial that you must complete to leave the shrine. You obtain an ability called Magnesis, allowing you to move objects around with magnets. After running around the shrine and using your new ability, you succeed in passing the trial. You leave the shrine.

You can go to:
- Wild
"""

jabaij = """ - You walk through the doorway and see an elevator. You take the elevator down and you see a blue and brown with a bunch of totems, statues, and walls. A trial awaits you to escape. You obtain an ability called Remote Bomb. This allows you to place or throws bombs and detonate them. After playing around with your new ability, you learn how to use it well. You destroy walls in your path and you succeed in passing the trial. You leave the shrine.

You can go to:
- Wild
"""

owadaim = """ - You walk through the doorway and you see an elevator. You take the elevator down and you see a blue and gold room with statues, giant turning gears, and levitating platforms rising up and down. A trial is needed to be passed in orderto leave the shrine. You learn a new ability called Statis.This allows you to be stop to stop time or stop and objects movement for a specific amount of time. After messing with your fun new ability, you successfully complete the trial. You leave the shrine.

You can go to:
- Wild
"""

kehnamut = """ - You walk into the doorway and see an elevator. You take the elevator down and you see a blue and gold room with totems, a balcony at the top, and water covering the ground. You can't escape the shrine unless you complete the trial. You receive an ability called Cryonis, which allows you  freeze water into tall pillars that can let you reach high places. After figuring out how your new ability works, you use it successfully to pass the trial.

You can go to:
- Wild
"""


def print_desc(been: Been, attack: list, location: str) -> None:
    print(f"\nYou are in the {location.title()}!")
    if location == "Shrine Of Resurrection":
        print(resurrection)
    elif location == "Oman Au Shrine":
        print(omanau)
        print("New attack received: Magnesis")
        attack.append("magnesis")
    elif location == "Ja Baij Shrine":
        print(jabaij)
        print("New attack gained: Bomb")
        attack.append("bomb")
    elif location == "Owa Daim Shrine":
        print(owadaim)
        print("You have gained a new ability: Cryonis")
        attack.append("cryonis")
    elif location == "Keh Namut Shrine":
        print(kehnamut)
        print("You have a new ability: Stasis")
        attack.append("stasis")
    elif location == "Wild":
        wild(been)


def is_valid_transition(been: Been, location: str, destination: str) -> bool:
    if location == "Shrine Of Resurrection":
        return destination == "Wild"
    elif location == "Oman Au Shrine":
        been.oman += 1
        return destination == "Wild"
    elif location == "Ja Baij Shrine":
        been.ja += 1
        return destination == "Wild"
    elif location == "Keh Namut Shrine":
        been.keh += 1
        return destination == "Wild"
    elif location == "Owa Daim Shrine":
        been.owa += 1
        return destination == "Wild"
    elif location == "Wild":
        if destination == "Oman Au Shrine" and been.oman == 0:
            return destination == "Oman Au Shrine"
        elif destination == "Ja Baij Shrine" and been.ja == 0:
            return destination == "Ja Baij Shrine"
        elif destination == "Owa Daim Shrine" and been.owa == 0:
            return destination == "Owa Daim Shrine"
        elif destination == "Keh Namut Shrine" and been.keh == 0:
            return destination == "Keh Namut Shrine"
        elif destination == "Fight":
            return destination == "Fight"
        else:
            return False
    else:
        return False


def invalid_destination_message(location: str, destination: str) -> str:
    return f"You cannot go to {destination} from {location}."


def input_destination_or_q(attack: list, been: Been, location: str) -> str:
    while True:
        print("Where would you like to go? [q to quit]")
        destination = input("> ").title()
        if destination == "Q" or is_valid_transition(been, location,
                                                     destination):
            return destination
        else:
            print(invalid_destination_message(location, destination))


def enemy_hp1(enemy: str) -> int:
    if enemy == "Blue Bokoblin":
        enemy_hp = 10
    elif enemy == "Red Bokoblin":
        enemy_hp = 5
    elif enemy == "Black Bokoblin":
        enemy_hp = 15
    elif enemy == "Silver Bokoblin":
        enemy_hp = 20
    elif enemy == "Moblin":
        enemy_hp = 12
    elif enemy == "Blue Chuchu":
        enemy_hp = 5
    elif enemy == "Stalkoblin":
        enemy_hp = 1
    return enemy_hp


def enemyt(numt: int) -> str:
    if numt == 1:
        enemy_type1 = "Blue Bokoblin"
    elif numt == 2:
        enemy_type1 = "Red Bokoblin"
    elif numt == 3:
        enemy_type1 = "Blue Chuchu"
    elif numt == 4:
        enemy_type1 = "Stalkoblin"
    elif numt == 5:
        enemy_type1 = "Moblin"
    elif numt == 6:
        enemy_type1 = "Black Bokoblin"
    else:
        enemy_type1 = "Silver Bokoblin"
    return enemy_type1


def enemy_type(num_enem_dead: int) -> int:
    num = [1, 2, 3, 4, 5]
    if num_enem_dead >= 9:
        num.append(6)
    if num_enem_dead >= 20:
        num.append(7)
    numt = choice(num)
    return numt


def weapons(typew: int) -> str:
    numt = typew
    if numt == 1:
        weapon = "boko spear"
    elif numt == 2:
        weapon = "spiked moblin spear"
    elif numt == 3:
        weapon = "boko bow"
    elif numt == 4:
        weapon = "rusty claymore"
    else:
        weapon = "rusty halberd"
    return weapon


def enemy_atk() -> str:
    attk = ["side attack", "jump attack", "jab"]
    eatt = choice(attk)
    return eatt


def weapon_dmg1(weapon: str) -> int:
    if weapon == "boko spear":
        ewdamage = 5
    elif weapon == "spiked moblin spear":
        ewdamage = 7
    elif weapon == "boko bow":
        ewdamage = 4
    elif weapon == "rusty claymore":
        ewdamage = 3
    else:
        ewdamage = 8
    return ewdamage


def weapon_type() -> int:
    typenum = [1, 2, 3, 4, 5]
    numt = choice(typenum)
    return numt


def chuchu_battle(been: Been, attack: list, enemy_hp: int, hp: int) -> None:
    chuatk = [2, 3, 1, 2, 4]
    print("You have found a Blue Chuchu. Time to fight.")
    while hp > 0 and enemy_hp > 0:
        chuchu_atk = choice(chuatk)
        print(f"\nHealth: {hp}")
        print(f"Chuchu Health: {enemy_hp}")
        u_attack = user_attack(attack)
        print(f"You use {u_attack}")
        u_dmg = user_attdamage("Blue Chuchu", been, u_attack)
        enemy_hp -= u_dmg
        if enemy_hp > 0:
            print(f"The Chuchu attacks.\n")
            hp -= chuchu_atk
    if enemy_hp <= 0:
        print("\n- You have defeated the Blue Chuchu")


def att_of_enemy(eatt: str) -> int:
    if eatt == "side attack":
        atk = 2
    elif eatt == "jump attack":
        atk = 3
    elif eatt == "jab":
        atk = 2
    return atk


def user_attack(attack: list) -> str:
    u_attack = input(f"Choose your attack {attack} \n> ")
    return u_attack


def user_attdamage(enemy: str, been: Been, u_attack: str) -> int:
    if u_attack == "slash":
        attk5 = 8
    elif u_attack == "spin attack":
        attk5 = 9
    elif u_attack == "bow and arrows":
        attk5 = 7
    elif u_attack == "boomerang":
        attk5 = 7
    elif u_attack == "bomb" and has_bomb(been):
        print(f"You throw it at {enemy}")
        attk5 = 11
    elif u_attack == "magnesis" and has_magnesis(been):
        print(f"A box flies at {enemy}")
        attk5 = 12
    elif u_attack == "cryonis" and has_cryonis(been):
        print(
            f"You make a pillar of ice beneath the {enemy}, and they fly a few feet away."
        )
        attk5 = 4
    elif u_attack == "stasis" and has_stasis(been):
        print(
            f"A Keese freezes in time and falls on the {enemy}'s head, the Keese then flies away."
        )
        attk5 = 3
    else:
        attk5 = 0
    return attk5


def has_bomb(been: Been) -> bool:
    if been.ja == 1:
        return True
    else:
        return False


def has_magnesis(been: Been) -> bool:
    if been.oman == 1:
        return True
    else:
        return False


def has_cryonis(been: Been) -> bool:
    if been.owa == 1:
        return True
    else:
        return False


def has_stasis(been: Been) -> bool:
    if been.keh == 1:
        return True
    else:
        return False


def fight(been: Been, attack: list, hp: int) -> int:
    num_enem_dead = 0
    typew = weapon_type()
    numt = enemy_type(num_enem_dead)
    enemy = enemyt(numt)
    enemy_hp = enemy_hp1(enemy)
    weapon = weapons(typew)
    weapon_dmg = weapon_dmg1(weapon)
    if enemy == "Blue Chuchu":
        chuchu_battle(been, attack, enemy_hp, hp)
    else:
        print(f"\nYou found a {enemy} wielding a {weapon}. Time to fight.\n")
        while hp > 0 and enemy_hp > 0:
            eatt = enemy_atk()
            atk = att_of_enemy(eatt)
            complete_atk = weapon_dmg + atk
            print(f"\nHealth: {hp}")
            print(f"Enemy Health: {enemy_hp}")
            u_attack = user_attack(attack)
            print(f"You use {u_attack}")
            u_dmg = user_attdamage(enemy, been, u_attack)
            enemy_hp -= u_dmg
            if enemy_hp > 0:
                print(f"\nThe {enemy} uses {eatt}.\n")
                hp -= complete_atk
        if enemy_hp <= 0:
            print(f"\n- You have defeated the {enemy}")
    return hp


def main() -> None:
    been = Been(0, 0, 0, 0)
    hp_up = [5, 6, 7, 6, 8, 7]
    heal = choice(hp_up)
    hp = 25
    attack = ["slash", "spin attack", "bow and arrows", "boomerang"]
    location = starting_point
    while hp > 0:
        print_desc(been, attack, location)
        destination = input_destination_or_q(attack, been, location)
        if destination == "Q":
            break
        elif destination == "Fight":
            hp = fight(been, attack, hp)
            if hp > 0:
                hp += heal
                if hp > 25:
                    hp = 25
        else:
            location = destination
    if hp <= 0:
        print("You have died.")


if __name__ == "__main__":
    main()
