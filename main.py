# @author Trevor Wilkins
# SEC 290 PLA Project
# 8/17/21 & 9/2/21

# This is a project that can be used to simulate a goblin army in a game of Dungeons and Dragons. To make this work, the program uses an array of goblins loaded from a file,randomly assigns them either ranged or melee weapons based on the boolean in the file, then allows the user enter an Armor Class (AC) for a target for the goblin army to strike. The program then prints messages sorted by hits/misses, and allows the user to advance to another round of combat, or stop


from goblin import Goblin
import fileinput


def main():
    # CRITERIA: At least one list
    # Set up an empty list for our Goblin army
    goblins = [
    ]

    # CRITERIA: Text file input and processing
    # Load our army from our goblins.txt file
    for line in fileinput.input(files = 'goblins.txt'):
      g = line.split(", "); # split the name and weapon boolean
      goblins.append(Goblin(g[0], g[1])) # push the goblin to the array


    #Intro message
    print("Welcome to the D&D Goblin Army Simulator. Your army is at your disposal!")


    # CRITERIA: At least one while loop
    #Loop indefinitely, but track turn number
    turn = 0
    while(True):
      turn += 1
      # Get the user to give us the target AC
      target_AC = int(input("\n\tPlease enter the target's AC (5-25 or 0 to stop): "))
      

      if(target_AC == 0):
        break # exits the while loop

      print(f"\n----------TURN {turn}----------")
      hits = []
      misses = []
      #Have each goblin in the army attack, and likewise set the attack message
      total_dmg = 0;
      for g in goblins:
        total_dmg += g.attack(target_AC)

        #sort attacks by hits and misses
        if(g.attack_message.find("HIT") != -1):
          hits.append(g.attack_message)
        else:
          misses.append(g.attack_message)


      # CRITERIA: At least one for loop
      # Print all hits, total damage, then all misses
      for h in hits:
        print(h)

      print(f"\nTOTAL DAMAGE: {total_dmg}\n")

      for m in misses:
        print(m)

    print("Program terminated.")


main()