# Gladiators

## Description:
I borrowed an idea of Derek Banas who creates a class of warriors with 2 warrior instances and let them fight.
I utilize a Warriors class to host a championship of several gladiators; they can be easily accessed in a separate csv file.
Python code creates a dictionary of warriors based on the csv file; the same applies to arenas stored likewise in a csv file.
Warriors are then stored as instances of the class to fight each other. Only 2 warriors are stored as an instance at a time.
Each warrior fights every other warrior twice in a random arena.
All data related to warriors, arenas and fights are stored to 3 MySQL tables; I access them using a connector module.
Once the championship is finished, I let user to see statistics with predefined MySQL queries


## Files:
war_main.py - main file with the base code
connector.py - file works with MySQL connector module
importer.py - serves for importing data from easily manageable csv files
new_db.sql - connector.py creates database and tables using queries written in this file
my_query.sql - connector.py uses this file to evoke predefined MySQL queries analyzing the championship
warriors.csv - details of warriors, can be easily modified
arenas.csv - details of arenas, can be easily modified
