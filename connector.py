# connector file operates MySQL databases
# functions from this file are called in the main section to create databases and insert data


def run_connector(command_list, use_database_dummy, update_vs_select):
    # use_database_dummy = 0 when database not created; 1 when created already
    # update_vs_select: update queries = 0 (mydb.comit() needed)
    # update_vs_select: select queries = 1 (print mycursor.column_names needed)

    import mysql.connector

    if use_database_dummy == 0:
        mydb = mysql.connector.connect(host='localhost', user='david', password='')
    else:
        mydb = mysql.connector.connect(host='localhost', user='david', password='', database='warrior_db')

    mycursor = mydb.cursor()

    for command in command_list:
        try:
            # this skippes errors which have no effect on the result
            mycursor.execute(command)
            if update_vs_select == 0:
                mydb.commit()
        except Exception:
            continue

    if update_vs_select == 1:
        print('------------')
        print(mycursor.column_names)
        print('------------')
    for i in mycursor:
        print(i)


def new_db():
    # def creates new database a all new needed tables. Source code is imported from a separate file
    with open('C:/Users/DAVID/PycharmProjects/war_project/new_db.sql', 'r') as rf:
        file_content = rf.read()
        file_list = file_content.split(';')

    run_connector(file_list, 0, 0)


def fight_query(winner, loser, arena):
    # def appends MySQL table 'fights' after every executed fight from the main section
    my_command = ['INSERT INTO fights(winner_id, loser_id, arena_id) VALUES({},{},{})'
                  .format(int(winner), int(loser), int(arena))]

    run_connector(my_command, 1, 0)


def warrior_query(war_dict):
    # MySQL table 'warriors' is appended with warriors stored in a dictionary
    for key, value in war_dict.items():
        name = value[0]
        health = int(value[1])
        attack_max = int(value[2])
        block_max = int(value[3])

        my_command = ['INSERT INTO warriors(war_name, health, attack_max, block_max)'
                                        'VALUES(\'{}\', {}, {}, {})'.format(name, health, attack_max, block_max)]

        run_connector(my_command, 1, 0)


def arena_query(arena_dict):
    # MySQL table 'arenas' is append with arenas stored in a dictionary
    for key, value in arena_dict.items():
        arena_name = value[0]
        location = value[1]

        my_command = ['USE warrior_db', 'INSERT INTO arenas(arena_name, location)'
                                        'VALUES(\'{}\', \'{}\')'.format(arena_name, location)]

        run_connector(my_command, 1, 0)


def analysis_query(num):
    # final analysis on executed fights
    with open('C:/Users/DAVID/PycharmProjects/war_project/my_query.sql', 'r') as rf:
        file_content = rf.read()
        file_list = file_content.split(';')
        new_query = [file_list[num]]

    run_connector(new_query, 1, 1)

