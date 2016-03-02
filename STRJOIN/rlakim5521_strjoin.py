# STRJOIN
# Jaekyoung Kim (rlakim5521@naver.com)

# Main function
if __name__ == "__main__":
    for _ in xrange(int(raw_input())):
        # Input
        n = int(raw_input())
        length = map(int, raw_input().split())
        
        # Solve
        cost = 0
        for _ in xrange(n-1):
            length.sort()
            cost += length[0] + length[1]
            length.append(length[0]+length[1])
            length.remove(length[0])
            length.remove(length[0])
        
        # Output
        print cost
