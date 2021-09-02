
import random

class Enemy:

    def __init__(self, to_hit, dmg_die, dmg_mod):
        self.to_hit = to_hit
        self.dmg_die = dmg_die
        self.dmg_mod = dmg_mod
        self.crit = False
        self.attack_message = ""

  
  # CRITERIA: At least one user defined function
  # Method that performs necessary math and calculates damage for attacks
  # Returns damage dealt, 0 if missed
    def attack(self, target_AC):
        
        hit_attempt = random.randrange(1, 20) + self.to_hit
        dmg = 0

        # CRITERIA: Simple math
        if(hit_attempt == 20 + self.to_hit):
            self.crit = True
            dmg += random.randrange(1, self.dmg_die)

        if(self.crit or hit_attempt >= target_AC):
            self.crit = False
            dmg += random.randrange(1, self.dmg_die) + self.dmg_mod
            self.attack_message = self.hit_message(dmg)
            return dmg
        
        self.attack_message = self.miss_message()
        return dmg

    def hit_message(self, dmg):
        output = "\tHIT: hit the target for " + str(dmg) + " damage."
        return output
    
    def miss_message(self):
      return "\tMISS: attack failed."

