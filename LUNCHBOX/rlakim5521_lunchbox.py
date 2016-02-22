+# LUNCHBOX
 +# Jaekyoung Kim (rlakim5521@naver.com)
 +
 +# Main function
 +if __name__ == "__main__":
 +    for _ in xrange(int(raw_input())):
 +        # Input
 +        n = int(raw_input())
 +        heat = map(int, raw_input().split())
 +        eat = map(int, raw_input().split())
 +                
 +        # Solve
 +        eatAndHeat = zip(eat,heat)
 +        eatAndHeat.sort()
 +        eatAndHeat.reverse()
 +        
 +        endTime = []
 +        cookingTime = 0
 +        
 +        for eah in eatAndHeat:
 +            cookingTime += eah[1]
 +            endTime.append(cookingTime+eah[0])
 +            
 +        # Output
 +        print max(endTime) 
