# module imports data about warriors and arenas stored in separate csv files


def imp_warriors():
    # function imports rows from csv file into dictionary
    import csv
    warriors = dict()

    with open('C:/Users/DAVID/PycharmProjects/war_project/warriors.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        # next skips first row which is a header row
        next(csv_reader)

        # each line of csv is copied into a dictionary
        warriors = {index: line for index, line in enumerate(csv_reader)}

    return warriors


def imp_arenas():
    # function imports rows from csv file into dictionary
    import csv
    arenas = dict()

    with open('C:/Users/DAVID/PycharmProjects/war_project/arenas.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)

        # each line of csv is copied into a dictionary
        arenas = {index: line for index, line in enumerate(csv_reader)}

    return arenas
