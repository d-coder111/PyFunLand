import random

def dragon_treasure_hunt():
    print("🦉 Welcome, brave adventurer, to the Dragon's Treasure Hunt - Legendary Edition!")
    print("I am Hoot, the wise owl, and I will guide you through this dangerous journey.")
    print("Your quest is to find the dragon's treasure hidden behind one of the many doors.")
    print("With each level, the danger grows, but so do the rewards!\n")

    level = 1
    lives = 3
    max_level = 5

    while lives > 0 and level <= max_level:
        print(f"\n🌟 Level {level}:")
        num_doors = level + 2  # Number of doors increases with each level
        treasure_path = random.randint(1, num_doors)
        
        print(f"There are {num_doors} doors before you.")
        print(f"Choose wisely, for the treasure is behind one door, and traps behind the others!")
        print(f"You have {lives} lives left.")

        # Owl gives a hint
        if random.random() < 0.5:  # 50% chance of getting a hint
            hint = random.choice([treasure_path, random.randint(1, num_doors)])
            print(f"\n🦉 Hoot's Hint: 'I sense the treasure may be behind door {hint}. But can you trust me?'")
        
        # Player chooses a door
        try:
            choice = int(input(f"Which door will you open (1-{num_doors})? "))
        except ValueError:
            print("❌ That's not a valid number. Please choose a door!")
            continue
        
        if choice < 1 or choice > num_doors:
            print(f"❌ Invalid choice. Please pick a door between 1 and {num_doors}.")
        elif choice == treasure_path:
            print("\n🎉 You found the treasure! Onward to the next level!\n")
            level += 1  # Advance to the next level
        else:
            lives -= 1
            if lives > 0:
                print("💀 Oh no! It was a trap! You've lost a life. But the journey continues...")
            else:
                print("\n💀 You've fallen into too many traps...")
                print("GAME OVER! The treasure remains hidden forever...")

    if lives > 0 and level > max_level:
        print("\n🏆 CONGRATULATIONS! You have completed all levels and claimed the legendary dragon's treasure!")
    elif lives == 0:
        print(f"\nThe treasure was behind door {treasure_path}. Better luck next time, adventurer.")

# Start the game
dragon_treasure_hunt()
