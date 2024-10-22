def main():
    t = int(input())
    for _ in range(t):
        s = input()
        one = s.count('1')
        zero = s.count('0')

        if one > zero:
            print("WIN")
        else:
            print("LOSE")

if __name__ == "__main__":
    main()


#We use s.count('1') and s.count('0') to count the occurrences of '1's and '0's in the string.
#Finally, we print "WIN" or "LOSE" based on the comparison.
