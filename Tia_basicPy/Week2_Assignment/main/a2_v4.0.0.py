from a2_support import *

# Implement your classes here
class Card:
    def __init__(self):
        self.card_damage = 0
        self.card_block = 0
        self.card_energy_cost = 1
        self.status_modifiers = {}
        self.card_name = 'Card'
        self.card_description = 'A card.'
        self.status_require = True
    
    def get_damage_amount(self):
        return self.card_damage
    
    def get_block(self):
        return self.card_block
    
    def get_energy_cost(self):
        return self.card_energy_cost

    def get_status_modifiers(self):
        return self.status_modifiers
    
    def get_name(self):
        return self.card_name
    
    def get_description(self):
        return self.card_description
    
    def requires_target(self):
        return self.status_require
    
    def __repr__(self) -> str:
        return str(self.__class__.__name__+"()")

    def __str__(self) -> str:
        return f'{self.card_name}: {self.card_description}'

# child class
class Strike(Card):

    def __init__(self): 
        self.card_damage = 6
        self.card_block = 0
        self.card_energy_cost = 1
        self.status_modifiers = {}
        self.card_name = 'Strike'
        self.card_description = 'Deal 6 damage.'
        self.status_require = True

class Defend(Card):

    def __init__(self): 
        self.card_damage = 0
        self.card_block = 5
        self.card_energy_cost = 1
        self.status_modifiers = {}
        self.card_name = 'Defend'
        self.card_description = 'Gain 5 block.'
        self.status_require = False

class Bash(Card):

    def __init__(self): 
        self.card_damage = 7
        self.card_block = 5
        self.card_energy_cost = 2
        self.status_modifiers = {}
        self.card_name = 'Bash'
        self.card_description = 'Deal 7 damage. Gain 5 block.'
        self.status_require = True

class Neutralize(Card):

    def __init__(self): 
        self.card_damage = 3
        self.card_block = 0
        self.card_energy_cost = 0
        self.status_modifiers = {'weak': 1, 'vulnerable': 2}
        self.card_name = 'Neutralize'
        self.card_description = 'Deal 3 damage. Apply 1 weak. Apply 2 vulnerable.'
        self.status_require = True
        
class Survivor(Card):

    def __init__(self): 
        self.card_damage = 0
        self.card_block = 8
        self.card_energy_cost = 1
        self.status_modifiers = {'strength': 1}
        self.card_name = 'Survivor'
        self.card_description = 'Gain 8 block and 1 strength.'
        self.status_require = False
        
class Eruption(Card):

    def __init__(self): 
        self.card_damage = 9
        self.card_block = 0
        self.card_energy_cost = 2
        self.status_modifiers = {}
        self.card_name = 'Eruption'
        self.card_description = 'Gain 9 damage.'
        self.status_require = True

class Vigilance(Card):

    def __init__(self): 
        self.card_damage = 0
        self.card_block = 8
        self.card_energy_cost = 2
        self.status_modifiers = {'strength':1}
        self.card_name = 'Vigilance'
        self.card_description = 'Gain 9 damage.'
        self.status_require = False

# Entities Abstract Class
class Entity:
    def __init__(self, max_hp: int) -> None:
      self.max_hp = max_hp
      self.current_hp = max_hp
      self.block = 0
      self.strength = 0
      self.weak = 0
      self.vulnerable = 0
    
    def get_hp(self):
        return self.current_hp
    
    def get_max_hp(self):
        return self.max_hp
    
    def get_block(self):
        return self.block
    
    def get_strength(self):
        return self.strength
    
    def get_weak(self):
        return self.weak
    
    def get_vulnerable(self):
        return self.vulnerable
    
    def get_name(self):
        return str(self.__class__.__name__)
    
    def reduce_hp(self, amount: int) -> None:
        reduction_poin = amount - self.block
        
        if reduction_poin <= 0:
            reduction_poin = 0
            self.block -= amount
        else:
            self.block = 0
        
        self.current_hp = self.current_hp - reduction_poin
        if self.current_hp < 0:
            self.current_hp = 0
        
    def is_defeated(self) -> bool:
        if self.current_hp <= 0:
            return True
        else:
            return False
    
    def add_block(self, amount: int) -> None:
        self.block += amount
    
    def add_strength(self, amount: int) -> None:
        self.strength += amount
        
    def add_weak(self, amount: int) -> None:
        self.weak += amount
    
    def add_vulnerable(self, amount: int) -> None:
        self.vulnerable += amount
        
    def new_turn(self):
        self.block = 0
        
        if self.vulnerable > 0:
            self.vulnerable -= 1
        
        if self.weak > 0:
            self.weak -= 1

    # revision 1.0.0
    def __repr__(self) -> str:
        return str(self.__class__.__name__+"("+str(self.max_hp)+")")

    def __str__(self) -> str:
        return f'{self.get_name()}: {self.get_hp()}/{self.get_max_hp()} HP'
        
class Player(Entity):
    def __init__(self, max_hp: int, cards:list = None) -> None:
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.block = 0
        self.strength = 0
        self.weak = 0
        self.vulnerable = 0
        self.energy = 3
        self.deck = cards
        self.hand = []
        self.discard = []
    
    def get_energy(self) -> int:
        return self.energy
    
    def get_hand(self) -> list:
        return self.hand
    
    def get_deck(self) -> list:
        return self.deck
    
    def get_discarded(self) -> list:
        return self.discard
    
    def start_new_encounter(self) -> None:
        # revision 1.0.0
        if self.get_hand() == []:
            self.deck.extend(self.get_discarded())
            self.discard = []
        
    def end_turn(self) -> None:
        self.discard.extend(self.hand)
        self.hand = []
    
    def new_turn(self) -> None:
        self.energy = 3
        draw_cards(self.deck, self.hand, self.discard)
    
    def play_card(self, card_name: str):
        hand_card_name = []
        for card in self.hand:
            hand_card_name.append(card.get_name())
            
        if card_name in hand_card_name:
            the_index = hand_card_name.index(card_name)
            if self.hand[the_index].card_energy_cost > self.energy:
                return None
            else:
                self.energy -= self.hand[the_index].card_energy_cost
                self.discard.extend([self.hand[the_index]])
                result = self.hand[the_index]
                del self.hand[the_index]
                return result
        else:
            return None
    
    # revision 1.0.0
    def __repr__(self) -> str:
        return str(self.__class__.__name__+"("+str(self.max_hp)+", "+str(self.deck)+")")
    
class IronClad(Player):
    def __init__(self):
        self.max_hp = 80
        self.current_hp = 80
        self.block = 0
        self.strength = 0
        self.weak = 0
        self.vulnerable = 0
        self.energy = 3
        self.deck = [Strike(),Strike(),Strike(),Strike(),Strike(),Defend(),Defend(),Defend(),Defend(),Bash()]
        self.hand = []
        self.discard = []
    
    # revision 2.0.0
    def __repr__(self) -> str:
        return str(self.__class__.__name__+"()")

class Silent(Player):
    def __init__(self):
        self.max_hp = 70
        self.current_hp = 70
        self.block = 0
        self.strength = 0
        self.weak = 0
        self.vulnerable = 0
        self.energy = 3
        self.deck = [Strike(),Strike(),Strike(),Strike(),Strike(),Defend(),Defend(),Defend(),Defend(),Defend(),Neutralize(),Survivor()]
        self.hand = []
        self.discard = []
    
    # revision 2.0.0
    def __repr__(self) -> str:
        return str(self.__class__.__name__+"()")

class Watcher(Player):
    def __init__(self):
        self.max_hp = 72
        self.current_hp = 72
        self.block = 0
        self.strength = 0
        self.weak = 0
        self.vulnerable = 0
        self.energy = 3
        self.deck = [Strike(),Strike(),Strike(),Strike(),Defend(),Defend(),Defend(),Defend(),Eruption(),Vigilance()]
        self.hand = []
        self.discard = []
    
    # revision 2.0.0
    def __repr__(self) -> str:
        return str(self.__class__.__name__+"()")

class Monster(Entity):
    counter = 0
    def __init__(self, max_hp: int) -> None:
      self.max_hp = max_hp
      self.current_hp = max_hp
      self.block = 0
      self.strength = 0
      self.weak = 0
      self.vulnerable = 0
      self.id = Monster.counter
      Monster.counter =+1
    
    def get_id(self) -> int:
        return self.id
    
    def action(self):
        raise NotImplementedError

    # revision 1.0.0
    def __repr__(self) -> str:
        return str(self.__class__.__name__+"("+str(self.max_hp)+")")
    
class Louse(Monster):
    def __init__(self, max_hp):
      self.max_hp = max_hp
      self.current_hp = max_hp
      self.block = 0
      self.strength = 0
      self.weak = 0
      self.vulnerable = 0
      self.id = Monster.counter
      Monster.counter =+1
      self.damage_amount = random_louse_amount()
    
    def action(self):
        return {'damage': self.damage_amount}

class Cultist(Monster):
    def __init__(self, max_hp):
      self.max_hp = max_hp
      self.current_hp = max_hp
      self.block = 0
      self.strength = 0
      self.weak = 0
      self.vulnerable = 0
      self.id = Monster.counter
      Monster.counter =+1
      self.num_calls = 0
    
    def action(self):
        if self.num_calls == 0:
            self.damage_amount = 0
            self.weak = 0
        else:
            self.damage_amount = 6 + self.num_calls
            if self.num_calls % 2 == 0:
                self.weak = 0
            else:
                self.weak = 1
        
        self.num_calls +=1 
        return {
            'damage': self.damage_amount,
            'weak': self.weak}

class JawWorm(Monster):
    def __init__(self, max_hp):
      self.max_hp = max_hp
      self.current_hp = max_hp
      self.block = 0
      self.strength = 0
      self.weak = 0
      self.vulnerable = 0
      self.id = Monster.counter
      Monster.counter =+1
      self.damage_taken = 0
      self.damage_amount = 0
    
    def action(self):
        self.damage_taken = self.max_hp-self.current_hp
        # revision 1.0.0
        self.block += -(-self.damage_taken//2)
        self.damage_amount = self.damage_taken//2
        return {
            'damage': self.damage_amount}

class Encounter:
    def __init__(self, player:Player, monster_list:list):
        self.player = player
      
        listMonster=[]
        for monster in monster_list:
            if monster[0] == "Louse":
                listMonster.append(Louse(monster[1]))
            elif monster[0] == "Cultist":
                listMonster.append(Cultist(monster[1]))
            # revision 4.0.0
            elif monster[0] == "JawWorm":
                listMonster.append(JawWorm(monster[1]))
        self.monster = listMonster
        # revision 4.0.0
        self.player_turn_status = True
        self.player.start_new_encounter()
    
    def start_new_turn(self) -> None:
        self.player.new_turn()
    
    def end_player_turn(self) -> None:
        self.player.end_turn()
        for monsta in self.monster:
            monsta.new_turn()
        # revision 4.0.0
        self.player_turn_status = False
    
    def get_player(self) -> Player:
        return self.player
    
    def get_monsters(self):
        return self.monster

    def is_active(self) -> bool:
        status = False
        if self.player.is_defeated():
            return False
        for monsta in self.monster:
            if not monsta.is_defeated():
                return True
        return status
    
    def player_apply_card(self, card_name: str, target_id: int = None) -> bool:
        hand_card_name = []
        for item in self.player.get_hand():
            hand_card_name.append(item.get_name())
        
        # check target requiring
        theCardIndex = hand_card_name.index(card_name)
        if self.player.get_hand()[theCardIndex].status_require and target_id==None:
            return False
        
        # check id monster
        monsterId = []
        for monsta in self.monster:
            monsterId.append(monsta.id)
        
        if target_id != None and target_id not in monsterId:
            return False
        
        # card checking
        theCard = self.player.play_card(card_name)
        if theCard == None:
            return False
        
        self.player.add_block(theCard.get_block())
        cardStatusModifier = theCard.get_status_modifiers()
        if target_id != None:
            theMonsterIndex = monsterId.index(target_id)
        
        if 'strength' in cardStatusModifier.keys():
            self.player.add_strength(cardStatusModifier['strength'])
        if 'weak' in cardStatusModifier.keys():
            self.monster[theMonsterIndex].add_weak(cardStatusModifier['weak'])
        if 'vulnerable' in cardStatusModifier.keys():
            self.monster[theMonsterIndex].add_vulnerable(cardStatusModifier['vulnerable'])
            
        # calculate the damage
        if target_id != None:
            totalDamage = theCard.get_damage_amount() + self.player.get_strength()
            if self.monster[theMonsterIndex].vulnerable > 0:
                # revision 4.0.0
                totalDamage *= 3//2
            if self.player.weak > 0:
                # revision 4.0.0
                totalDamage *= 3//4
            
            self.monster[theMonsterIndex].reduce_hp(totalDamage)
        
            if self.monster[theMonsterIndex].is_defeated():
                del self.monster[theMonsterIndex]
        
        return True

    def enemy_turn(self) -> None:
        # revision 4.0.0
        if not self.player_turn_status:
            for monsta in self.monster:
                dict_action = monsta.action()
                if 'weak' in dict_action.keys():
                    # revision 4.0.0
                    if self.player.get_weak()==0:
                        self.player.add_weak(dict_action['weak'])
                if 'vulnerable' in dict_action.keys():
                    self.player.add_vulnerable(dict_action['vulnerable'])
                if 'strength' in dict_action.keys():
                    monsta.add_strength(dict_action['strength'])
            
                totalDamage = dict_action['damage'] + monsta.get_strength()
                
                if self.player.get_vulnerable() > 0:
                    # revision 4.0.0
                    totalDamage *= 3/2
                if monsta.get_weak() > 0:
                    # revision 4.0.0
                    totalDamage *= 3/4
                self.player.reduce_hp(totalDamage)
            # revision 4.0.0
            self.player_turn_status=True
        self.start_new_turn()
                
        
def main():
    # Implement this only once you've finished and tested ALL of the required
    # classes.
    typePlayer = input("Enter a player type: ")
    # typePlayer = "ironclad"
    if typePlayer == "ironclad":
        player = IronClad()
    elif typePlayer == 'silent':
        player = Silent()
    elif typePlayer == 'watcher':
        player = Watcher()
    
    fileName = input("Enter a game file: ")
    # fileName = "games/game1.txt"
    encounterAct = read_game_file(fileName)
    
    for encounter in encounterAct:
        print("New encounter!\n")
       # create monster instance
       # revision 2.0.0
        gameEcounter = Encounter(player,encounter)
        display_encounter(gameEcounter)
        while gameEcounter.is_active():
            enterMove = input("Enter a move: ")
            enterMove = enterMove.split(" ")
            if enterMove[0]=="end" and enterMove[1]=="turn":
                gameEcounter.end_player_turn()
                gameEcounter.enemy_turn()
                display_encounter(gameEcounter)
            elif enterMove[0]=="inspect" and enterMove[1]=="deck":
                print()
                print(player.get_deck(),"\n")
            elif enterMove[0]=="inspect" and enterMove[1]=="discard":
                print()
                print(player.get_discarded(),"\n")
            elif enterMove[0]=="describe":
                if enterMove[1]=="Strike":
                    print("\n"+Strike().card_description+"\n")
                elif enterMove[1]=="Defend":
                    print("\n"+Defend().card_description+"\n")
                elif enterMove[1]=="Bash":
                    print("\n"+Bash().card_description+"\n")
                elif enterMove[1]=="Neutralize":
                    print("\n"+Neutralize().card_description+"\n")
                elif enterMove[1]=="Survivor":
                    print("\n"+Survivor().card_description+"\n")
            elif enterMove[0]=="play":
                if len(enterMove) < 3:
                    if gameEcounter.player_apply_card(enterMove[1]):
                        display_encounter(gameEcounter)
                    else:
                        print(CARD_FAILURE_MESSAGE)
                else:
                    if gameEcounter.player_apply_card(enterMove[1], int(enterMove[2])):
                        display_encounter(gameEcounter)
                    else:
                        print(CARD_FAILURE_MESSAGE)
                    
        if player.is_defeated():
            print(GAME_LOSE_MESSAGE)
            exit()
        else:
            print(ENCOUNTER_WIN_MESSAGE)
    
    if player.is_defeated():
        print(GAME_LOSE_MESSAGE)
        exit()
    else:
        print(GAME_WIN_MESSAGE)

if __name__ == '__main__':
    main()