# PACKING
# Jaekyoung Kim (rlakim5521@naver.com)


def pack(capacity, item, numberOfItem, optimalTable, itemVolume, itemUrgency):
    if(item > numberOfItem): return 0
    if(optimalTable[item][capacity] != 0): return optimalTable[item][capacity];
    optimalTable[item][capacity] = pack(capacity, item + 1, numberOfItem, optimalTable, itemVolume, itemUrgency)
    if(capacity >= itemVolume[item]):
        optimalTable[item][capacity] = max(optimalTable[item][capacity], pack(capacity - itemVolume[item], item + 1, numberOfItem, optimalTable, itemVolume, itemUrgency) + itemUrgency[item])
    return optimalTable[item][capacity]

def reconstruct(capacity, item, portableItems, numberOfItem, optimalTable, itemVolume, itemUrgency, itemName):
    if(item > numberOfItem): return portableItems
    if(pack(capacity, item, numberOfItem, optimalTable, itemVolume, itemUrgency) == pack(capacity, item + 1, numberOfItem, optimalTable, itemVolume, itemUrgency)):
        reconstruct(capacity, item + 1, portableItems, numberOfItem, optimalTable, itemVolume, itemUrgency, itemName)
    else:
        portableItems.append(itemName[item])
        reconstruct(capacity - itemVolume[item], item + 1, portableItems, numberOfItem, optimalTable, itemVolume, itemUrgency, itemName)
    return portableItems

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
            
            maxUrgency = pack(maxCapacity, 1, numberOfItem, optimalTable, itemVolume, itemUrgency)
            
            # Adds used items into list
            portableItems = []
            portableItems = reconstruct(maxCapacity, 1, portableItems, numberOfItem, optimalTable, itemVolume, itemUrgency, itemName)
            
            # Output
            print maxUrgency, len(portableItems)
            for item in range(len(portableItems)):
                print portableItems[item]
                
MainFunction()
