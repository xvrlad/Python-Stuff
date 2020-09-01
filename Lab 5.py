##def rate(n):
##    total = 0
##    i = 0
##    count = 2
##    count += 1
##    while i < n:
##        count += 1
##        j = 0
##        count += 1
##        while j < n:
##            count += 1
##            total += j
##            count += 1
##            j += 1
##            count += 1
##        count += 1
##        i += 1
##        count += 1
##    count += 1
##    print("Number of operations:", count)
##    return total

##def rate(n):
##    total = 0
##    i = 1
##    count = 2
##    count += 1 
##    while i < n:
##        count += 1
##        j = 0
##        count += 1
##        while j < n:
##            count += 1
##            total += j
##            count += 1
##            j += 1
##            count += 1
##        count += 1
##        i *= 2
##        count += 1
##    count += 1
##    print("Number of operations:", count)
##    return total

##def rate(n):
##    total = 0
##    i = 0
##    count = 2
##    count += 1
##    while i < n:
##        count += 1
##        j = 0
##        count += 1
##        while j < 2 * n:
##            count += 1
##            total += j
##            count += 1
##            j += 1
##            count += 1
##        count += 1
##        i += 1
##        count += 1
##    count += 1
##    print("Number of operations:", count)
##    return total

def rate(n):
    total = 0
    i = 0
    count = 2
    count += 1
    while i < 4:
        count += 1
        j = 0
        count += 1
        while j < i:
            count += 1
            total += j
            count += 1
            j += 1
            count += 1
        count += 1
        i += 1
        count += 1
    count += 1
    print("Number of operations:", count)
    return total

def main():
    rate(2)
    rate(10)
    rate(100)
    return

main()
