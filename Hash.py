import time
import csv


#opens the csv file and sorts all the movies in a dictionary 
movies = []
with open("MOCK_DATA.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        movies.append(row)


class Node:
    def __init__(self, key, record):
        self.key = key #title or quote
        self.record = record #the whole movie entry
        self.next = None #keeps track of following node

class LinkedList:
    pass

class LinearProbing:
    pass