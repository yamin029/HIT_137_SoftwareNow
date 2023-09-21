def main():
    print("Number Sort")
    f = open("/Users/yaminhossain/Desktop/CDU/Software_Now/week4/numbers.txt", 'r')
    numbers = []
    for num in f:
        words = num.split()
        for word in words: 
            numbers.append(int(word))
    midpoint  = len(numbers)//2
    print(midpoint)
    print(len(numbers)%2==1)
   

    numbers.sort()
    print(numbers)
if __name__ == "__main__":
    main()