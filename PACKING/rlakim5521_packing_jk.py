# PACKING
# Jaekyoung Kim (rlakim5521@naver.com)

# Gets a max capacity of received capacity and returns the optimal table
def getMaxCapacity(maxCapacity, optimalTable, itemVolume, itemUrgency, numberOfItem):
    
    for capacity in xrange(1, maxCapacity + 1):
        # Default case is adding nothing.
        for item in xrange(numberOfItem + 1):
            optimalTable[item][capacity] = optimalTable[item][capacity - 1]
        
        # Compares urgencies of all possible cases.
        for item in xrange(1, numberOfItem + 1):
            if(capacity - itemVolume[item] >= 0):
                if(optimalTable[item][capacity - itemVolume[item]] == 0):
                    if(optimalTable[0][capacity] < optimalTable[0][capacity - itemVolume[item]] + itemUrgency[item]):
                        optimalTable[0][capacity] = optimalTable[0][capacity - itemVolume[item]] + itemUrgency[item]
                        for item2 in xrange(1, numberOfItem + 1):
                            optimalTable[item2][capacity] = optimalTable[item2][capacity - itemVolume[item]]
                        optimalTable[item][capacity] = 1
    
# Main function
def MainFunction():
    if __name__ == "__main__":
        for _ in xrange(input()):
            numberOfItem, maxCapacity = map(int, raw_input().split())
            
            # First row is a row for the maximum urgency and
            # the others are used to show whether the item is packed or not.
            optimalTable = [[0] * (maxCapacity + 1) for _ in range(numberOfItem + 1)]
            itemName = {}
            itemVolume = {}
            itemUrgency = {}
            
            # Inserts input data into dictionaries
            for item in xrange(1, numberOfItem + 1):
                itemName[item], tempVolume, tempUrgency = raw_input().split()
                itemVolume[item] = int(tempVolume)
                itemUrgency[item] = int(tempUrgency)
            
            getMaxCapacity(maxCapacity, optimalTable, itemVolume, itemUrgency, numberOfItem)
            
            # Adds used items into list
            portableItems = []
            for item in xrange(1, numberOfItem + 1):
                if(optimalTable[item][maxCapacity]):
                    portableItems.append(itemName[item])
            
            # Output
            print optimalTable[0][maxCapacity], len(portableItems)
            for item in range(len(portableItems)):
                print portableItems[item]
            
MainFunction()
