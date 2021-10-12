from LinkedList import LinkedList
from Node import Node

class HashTable:
    def __init__( self, cap ):
        self.cap = cap
        self.length = 0
        words = []
        for i in range(0, cap, 1):
            words.append( None )
        self.storage = words
    
    def printHashTable( self ):
        print( "Capacity: ", self.cap )
        print( "Length: ", self.length )
        print( "Storage: ", self.storage )

    def add( self, word ):

        val = 0
        for letter in word:
            val += ord( letter )

        index = (int((((val / 13) * 32) + 14) * 7)) % self.cap
        # Check if the length has not surpassed the capacity of the hash table 
        if self.storage[ index ] == None:
            self.storage[ index ] = { 
                'word' : word,
                'count' : 1
             }
            self.length += 1
        else:
            # We should change the current value to a linked list and add the new value at the end of that list
            if self.storage[ index ]['word'] == word:
                self.storage[ index ][ 'count' ] += 1
                #list = LinkedList()
                #list.insertLast( self.storage[ index ] )
                #self.storage[ index ] = list
            #self.storage[ index ].insertLast( val )
    
    def findCount( self, word ):

        val = 0
        for letter in word:
            val += ord( letter )
        index = (int((((val / 13) * 32) + 14) * 7)) % self.cap

        if self.storage[ index ] == None:
            print( f"The word {word} is not yet in our HashTable!" )
            return 0
        else:
            print( self.storage[ index ] )
            if self.storage[ index ][ 'word' ] == word:
                return self.storage[ index ][ 'count']
            #if type(self.storage[ index ]) != int:
            #    print( f"The value {val} is stored at position {index} of the HashTable" )
            #    list = self.storage[ index ]
            #    node = list.findNode( val )
            #    print( "Printing the value from a node in the linked list", node.val)
            #else:
            #    if self.storage[ index ] == val:
            #        print( f"The value {val} is stored at position {index} of the HashTable" )
            #    else:
            #        print( f"The value {val} is not yet in our HashTable!" )
    
    def remove( self, val ):
        pass
        # First find if the value is in the hashtable
        # If it is in the hastable remove it (subtracting the length)
        # If it is a linked list, make sure to remove the appropriate Node inside that link list