def main():
    # print("question 1")
    # data = [20,40,50,33,3954]
    # sum  = 0
    # for num in data:
    #     sum +=  num
    # print("Total is : ", sum)

    # print("question 2")
    # def summation(low, high):
    #     sum = 0
    #     while low <= high: 
    #         sum = sum + low
    #         low = low + 1  
    #     return sum
    # print(summation(1, 3))

    # print("Question 3")
    # data =  {"b":20, "a":30 }
    # data["b"]= -data["b"]
    # print(data)
    # data["c"]= 40
    # print(data)
    # if "b" in data:
    #     del data["b"]
    # print(data)
    # # for key in sorted(data.keys()):
    # #     print(key)
    # the_keys = list(data.keys())
    # the_keys.sort()
    # for key in the_keys:
    #     print(key)

    # print("Question 4")
    # def get_smallest_number(numbers):
    #     if len(numbers)==0:
    #         return None
    #     smallest = numbers[0]
    #     for number in numbers:
    #         if number< smallest:
    #             smallest = number
    #     return smallest
    # num_list = [15, 3, 8, -10, 25, 0]
    # smallest_number = get_smallest_number(num_list)
    # print("The smallest number in the list is: ", smallest_number)

    print("Question 5")
    dic1={1:10, 2:20}
    dic2={3:30, 4:40}
    dic3={5:50,6:60} 
    res = {**dic1, **dic2, **dic3}
    print("Final dictionary" , res)
if __name__ == '__main__':
    main()