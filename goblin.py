# @author Trevor Wilkins
# SEC 290 PLA Project
# 8/17/21 & 9/2/21

from enemy import Enemy
import random

# Class for specific enemy type
# Contains variants for melee and ranged weapons (no change to stats)
class Goblin(Enemy):

  # CRITERIA: At least one dictionary

  # Dictionaries of weapons and their associated damage types
  ranged = {
    "shortbow": "pierc",
    "crossbow": "pierc",
    "slingshot": "bludgeon",
    "javelin": "pierc"
  }
  melee = {
    "scimitar": "slash",
    "club": "bludgeon",
    "daggar": "slash",
    "spear": "pierc",
    "shortsword": "slash"
  }

  #List of random failure messages
  failures = [
    " got distracted by something shiny",
    " lost their grip",
    "\'s finger slipped",
    "\'s aim was off",
    " didn't aim very well",
    "\'s weapon couldn't break through the enemy's armor",
    "\'s attack was deflected",
    "\'s attack was dodged",
    "\'s strike was blocked"
  ]

  def __init__(self, name, is_ranged):
    super().__init__(4, 6, 2) # initialize to-hit, dmg die, and dmg modifier
    self.name = name
    self.is_ranged = is_ranged

    self.set_ranged()


  def set_ranged(self):
    if(self.is_ranged):
      self.weapon = random.choice(list(self.ranged.keys()))
      self.dmg_type = self.ranged[self.weapon]
    else:
      self.weapon = random.choice(list(self.melee.keys()))
      self.dmg_type = self.melee[self.weapon]


  # CRITERIA: Format using f-strings
  #Override methods
  def hit_message(self, dmg):
    output = f"\tHIT: {self.name}\'s {self.weapon} {self.dmg_type}ed"
    output += f" the target for {dmg} dmg"

    return output

  def miss_message(self):
    return f"\tMISS: {self.name}" + random.choice(self.failures)