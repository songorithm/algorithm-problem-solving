# RATIO
# Jaekyoung Kim (rlakim5521@naver.com)

# Main function
if __name__ == "__main__":
    for _ in range(int(raw_input())):
        # Input
        N, M = map(int, raw_input().split())
        
        baseWinningRate = (M * 100) / N
        
        # Solve
        # If a winning rate is more than 99%, there is no possibility to get a name of 'mighty lord'
        if(baseWinningRate >= 99):
            print -1
            continue
        
        k = 1073741824
        n = N
        m = M
        # If player winning k times serially can get a name of 'mighty lord', pass.
        # Else, add the k. Then we can get the highest rate which can not get a name of 'mighty lord'.
        while(k!=0):
            if(100*(m+k)/(n+k) > 100*m/n):
                pass
            else:
                m=m+k
                n=n+k
            k = k / 2
        
        # Output
        print m - M + 1
