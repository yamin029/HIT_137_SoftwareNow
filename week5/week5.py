def main():
    lower=int(input("enter lower"))
    upper=int(input("enter upper"))
    displayrange(lower,upper)

def displayrange(lower,upper):
     if lower <= upper:
        print(lower)
        displayrange(lower+1,upper)

main()