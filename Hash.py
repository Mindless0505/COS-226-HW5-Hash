#COS 226 - Hash something out 
#Christopher Noonan
#11/6/26
#
#Approach: loads all movies from MOCK_DATA.csv and creates two hash tables for movie titles and movie quotes.
#it then prints the empty slots in the table, the collisons while inserting into the table and the build time
#for each table.
#
#Attempt 5: Best hash function with a Linked List
#Hash function: The hash function creates a key that uses the character code value and position of the letters
#in the movie title or quote. This attempts to evenly distribute the keys across the entire table making 
#them as unique as possible. Hopefully reducing the number of collisons greatly and empty slots. 
#The hash function was then modified to reduce the size of the key so it doesnt get gigantic
#A Linked List was also chosen over the Linear Probing as it seemed to perform better with the current hash function setup
#
#Results:
# (movie_title) Best hash function - Linked List
# Wasted Space:  7565 slots
# Collisions:  10382
# Time Taken: 0:00:00.040000
# (quote) Best hash function - Linked List
# Wasted Space:  6701 slots
# Collisions:  11521
# Time Taken: 0:00:00.067500


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


#good hash function - multiplies the total by 26 then adds the letters character code.
#the 26 makes the total dependent on the characters position so there are less duplicates if 
#two movie titles contain the same letters.
#A remander operation is added to keep the total from getting too large
def hash_function(key):
    total = 0
    for character in key:
        total = total * 26 + ord(character)
        total = total % (2 ** 32) 
    return total


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

    print(f"({column})","Best hash function - Linked List")
    print("Wasted Space: ", empty, "slots")
    print("Collisions: ", table.collisions)
    print(f"Time Taken: {end-start}")