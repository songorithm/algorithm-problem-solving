n = int(raw_input())
f = raw_input()

def hug(members, fans):
    result = 0
    hugging_all = 0
    for f in fans:
        if f == 'F':
            hugging_all += 1
            if(hugging_all == members):
                result += 1
                hugging_all -= 1
        else:
            hugging_all = 0
    return result

count = hug(n, f)
print "%d" % count

# MY ANSWER:
# 4
# FFFMMM 0
# MMMFFF 0
# FFFFF  2
# FFFFFFFFFF 7
# FFFFM 1
# FFFFFMMMMF 2
# MFMFMFFFMMMFMF 0
# MMFFFFFMFFFMFFFFFFMFFFMFFFFMFMMFFFFFFF 10