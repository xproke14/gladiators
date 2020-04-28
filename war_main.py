import random
import importer
import connector


class Warriors:

    def __init__(self, name='', health=0, attack_max=0, block_max=0):
        self.name = name
        self.health = health
        self.attack_max = attack_max
        self.block_max = block_max

    def attack(self):
        return random.random() * self.attack_max + 0.5

    def block(self):
        return random.random() * self.block_max

    @classmethod
    def from_list(cls, my_list):
        name = my_list[0]
        health = my_list[1]
        attack_max = my_list[2]
        block_max = my_list[3]
        return cls(name, int(health), int(attack_max), int(block_max))


def fight_result(w1, w2):

    while True:
        # warrior 1 attacks
        battle_attack = w1.attack()
        defense = w2.block()
        damage = round((battle_attack - defense))
        if damage < 0: damage = 0
        w2.health -= damage
        if w2.health <= 0:
            # returns winner
            return 'A'

        # warrior 2 attacks
        battle_attack = w2.attack()
        defense = w1.block()
        damage = round((battle_attack - defense))
        if damage < 0: damage = 0
        w1.health -= damage
        if w1.health <= 0:
            # returns winner
            return 'B'


def analysis():

    # this function gives an analysis once championship is finished
    # MySQL query is called based on user's input

    print('Gladiator championship has successfully finished!')
    while True:
        result = input('Do you wish to see results? (y/n): ')
        result.lower()
        if result == 'n':
            print('Bye')
            exit()
        elif result == 'y':
            break
        else:
            print('Type \'y\' as yes or \'n\' as no!')

    result_option = ['Number of wins', '3 Best fighters', 'Number of fights by arena', 'Stats by fight', 'EXIT program']

    while True:
        print('------------')
        for number, query in enumerate(result_option):
            print('{} - {}'.format(number, query))
        num = int(input('Enter query number: '))
        if num == 5:
            exit()
        else:
            # this calls MySQL query
            connector.analysis_query(num)


def main():

    # create database and tables in SQL
    connector.new_db()

    # import warriors and arenas from CSV into a dictionary
    w_dict = importer.imp_warriors()
    a_dict = importer.imp_arenas()

    # import dictionaries into database
    connector.warrior_query(w_dict)
    connector.arena_query(a_dict)

    # Each warriors fight every other warrior twice
    # choose warrior A:
    for i in range(len(w_dict)-1):
        war_a = Warriors.from_list(w_dict[i])

        # choose warrior B
        for j in range(len(w_dict)):
            if j > i:
                war_b = Warriors.from_list(w_dict[j])

                # let them fight A vs B
                arena_id = random.randrange(len(a_dict))
                winner = fight_result(war_a, war_b)
                if winner == 'A':
                    connector.fight_query(i+1, j+1, arena_id + 1)
                    # parameters of fight_query are incremented by 1 as MySQL starts with 1, not 0
                else:
                    connector.fight_query(j+1, i+1, arena_id + 1)

                # let them fight B vs A
                arena_id = random.randrange(len(a_dict))
                winner = fight_result(war_b, war_a)
                if winner == 'A':
                    connector.fight_query(i+1, j+1, arena_id + 1)
                else:
                    connector.fight_query(j+1, i+1, arena_id + 1)

    # Analysis of the championship:
    analysis()


main()


