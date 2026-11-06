#COS 226 - Hash something out 
#Christopher Noonan
#11/6/26
#
#Approach: loads all movies from MOCK_DATA.csv and creates two hash tables for movie titles and movie quotes.
#it then prints the empty slots in the table, the collisons while inserting into the table and the build time
#for each table.
#
#Attempt 1: Poor hash function with a Linked List
#Hash function: The hash function returns a value of 0 regardless of input.
#This makes it so every single key is identical. Thus all the entries are in the same spot on the table
#This should create a significant amount of collisons with a lot of wasted space
#
#Results:
#(movie_title) Poor hash function - Linked List
#Wasted Space:  14999 slots
#Collisions:  78340596
#Time Taken: 0:00:03.813998
#
#(quote) Poor hash function - Linked List
#Wasted Space:  14999 slots
#Collisions:  111409320
#Time Taken: 0:00:04.938001



import time
import csv
from datetime import datetime

#opens the csv file and sorts all the movies in a dictionary 
movies = []
with open("MOCK_DATA.csv", newline="", encoding="utf-8") as file:
    #automatically reads the header from the file and creates a dictionary for all the movies using the header categories
    reader = csv.DictReader(file)
    for row in reader:
        movies.append(row)


#poor hash function - returns a key of 0 no matter what making them all the same
def hash_function(key):
    return 0



class Node:
    def __init__(self, key, record):
        self.key = key #title or quote
        self.record = record #the whole movie entry
        self.next = None #keeps track of following node

class LinkedList:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * size #slots start out empty
        self.collisions = 0

    def insert(self, key, record):
        # set index as the remander of the hash key by the table size
        index = hash_function(key) % self.size 

        #empty slot with no collisions put node in
        if self.slots[index] is None:
            self.slots[index] = Node(key,record)
            return

        #slot is full keep moving counting every full slot as collision
        node = self.slots[index]
        while True:
            self.collisions = self.collisions + 1 #if collision adds to counter
            if node.key == key:
                return                          #if the same key is already stored skip it
            if node.next is None:
                node.next = Node(key, record) #reached end of node list add new node here
                return
            node = node.next #(check) if next slot is full set pointer to next slot and continue the loop again

    #function for getting movie from key
    def get(self, key):
        # set index as the remander of the hash key by the table size
        index = hash_function(key) % self.size
        node = self.slots[index]
        #scans the list one by one to find desired movie from key
        while node is not None:
            if node.key == key:
                return node.record #if movie is found from key return the movies information
            node = node.next #else move to next node
        return None #if movie isnt found return nothing


    #function for counting empty space in the hash table
    def count_empty(self):
        empty = 0
        for slot in self.slots:
            if slot is None:
                empty = empty + 1
        return empty
        
class LinearProbing:
    def __init__(self,size):
        self.size = size
        #set all to empty
        self.keys = [None] * size
        self.records = [None] * size
        self.collisions = 0

    def insert(self, key, record):
        # set index as the remander of the hash key by the table size
        index = hash_function(key) % self.size
        

        #while the slot being looked at is full, count as collision
        while self.keys[index] is not None:
            self.collisions = self.collisions +1
            if self.keys[index] == key:
                return                       #if the same key is already stored skip it
            index = (index + 1 ) % self.size #try next slot

        self.keys[index] = key
        self.records[index] = record

    #function for getting movie from key
    def get(self,key):
        # set index as the remander of the hash key by the table size
        index = hash_function(key) % self.size
        
        while self.keys[index] is not None: #keep scanning keys if keys remain
            if self.keys[index] == key:
                return self.records[index] #if key is found return movie 
            index = (index + 1) % self.size
        return None 

    #function for counting empty space in the hash table
    def count_empty(self):
        empty = 0
        for key in self.keys:
            if key is None:
                empty = empty + 1
        return empty


for column in ["movie_title", "quote"]:
    table_size = int(len(movies))

    table = LinkedList(table_size) #create hash table

    start = datetime.now()
    for row in movies:
        key = row[column]
        if key is None: #if row is missing column
            continue
        key = key.strip() #cleans up key
        if key == "": #skip empty key
            continue
        table.insert(key,row)
    end = datetime.now()

    empty = table.count_empty()
    percent = round(empty / table_size *100, 1)

    print(f"({column})","Poor hash function - Linked List")
    print("Wasted Space: ", empty, "slots")
    print("Collisions: ", table.collisions)
    print(f"Time Taken: {end-start}")