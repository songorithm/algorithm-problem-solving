# POTION
# Jaekyoung Kim (rlakim5521@naver.com)

import copy

def gcd(a, b):
    while (b != 0):
        temp = a % b
        a = b
        b = temp
    return abs(a)

# Main function
if __name__ == "__main__":
    for _ in range(int(raw_input())):
        # Input
        n = int(raw_input())
        materials = map(int, raw_input().split())
        pots = map(int, raw_input().split())
        
        # Solve
        # Get the greatest common divisor of materials.
        gcdOfMaterials = materials[0]
        for material in materials:
            gcdOfMaterials = gcd(gcdOfMaterials, material)
        
        # By divide materials by gcd, get the minimum ratios for the potion.
        minRatios = copy.deepcopy(materials)
        for iter in xrange(n):
            minRatios[iter] = minRatios[iter] / gcdOfMaterials
          
        # To get the magnification, get pots divided by minRatios and round them up.
        # The results and gcd are candidates of the magnification.
        # After that, make the maximum value of candidates a final magnification.
        minMagnifications = copy.deepcopy(pots)
        for iter in xrange(n):
            minMagnifications[iter] = (minMagnifications[iter] + minRatios[iter] - 1) / minRatios[iter]
        finalMagnification = max(gcdOfMaterials,max(minMagnifications))
    
        # Calculate the final ratios by multiplying minRatios by finalMagnification.
        finalRatios = copy.deepcopy(minRatios)
        for iter in xrange(n):
            finalRatios[iter] = finalRatios[iter] * finalMagnification
            
        # Output
        # Subtract pots from finalRatios, and print them.
        for iter in xrange(n):
            print finalRatios[iter] - pots[iter],
        print
