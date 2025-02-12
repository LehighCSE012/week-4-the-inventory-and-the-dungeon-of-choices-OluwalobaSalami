import random
"""
This is the next part of the adventure! How exciting! Here we are using dungeons! Awesome!
"""
def main():
    inventory = []

    def acquire_item(inventory, item):
        #to add an item to the list
        inventory.append(item)
        print(f"You acquired a {item}!")
        return inventory
    
    def display_inventory(inventory):
        if len(inventory) == 0:
            print("Your inventory is empty.")
        else:
            print("Your inventory:")
            for item in inventory:
                #to get the items position in the list
                print(f"{inventory.index(item) + 1}. {item}")

    dungeon_rooms = [
    ("A dusty old library", "key", "puzzle", ("You solved the puzzle!", "The puzzle remains unsolved.", -5)),
    ("A narrow passage with a creaky floor", None, "trap", ("You skillfully avoid the trap!", "You triggered a trap!", -10)),
    ("A grand hall with a shimmering pool", "healing potion", "none", None),
    ("A small room with a locked chest", "treasure", "puzzle", ("You cracked the code!", "The chest remains stubbornly locked.", -5))
    ]

    def enter_dungeon(player_health, inventory, dungeon_rooms):
        for room in dungeon_rooms:
            print(room[0])
            if room[1]:
                acquire_item(inventory, room[1])
            if room[2] == "puzzle":
                print("You encounter a puzzle!")
                choice = input("Solve or skip? ")
                if choice.lower() == "solve":
                    puzzle_outcome = random.choice([True, False])
                    if puzzle_outcome:
                        print(room[3[0]])
                    else:
                        print(room[3[1]])
            elif room[2] == "trap":
                print("You see a potential trap!")
                choice_2 = input("Disarm or bypass? ")
                if choice_2.lower() == "disarm":
                    trap_outcome = random.choice([True, False])
                    if trap_outcome:
                        print(room[3[0]])
                    else:
                        print(room[3[1]])
                        player_health 
            if room[2] == "none":
                print( "There doesn't seem to be a challenge in this room. You move on.")

            





if __name__ == "__main__":
    main()
                


