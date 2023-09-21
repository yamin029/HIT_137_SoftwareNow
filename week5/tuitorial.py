def main():
    # print("Question 1")
    # number_to_check=15
    # range_start = 10
    # range_end = 20
    # if in_the_range(number_to_check, range_start, range_end):
    #     print("Number is in the range")
    # else:
    #     print("Number is not in the list")

    # print("Question 2")
    # sample_string = 'The Quick Brow'
    # lower, upper = count_upper_lower_string(sample_string)
    # print("No. of Lower case characters ", lower)
    # print("No. of Upper case characters ", upper)

    print("Question 3")
    sample_list = [1,2,3,3,3,3,4,5]
    print("Unique List",get_unique_list(sample_list))

def get_unique_list(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

def count_upper_lower_string(input_string):
    lower_count=0
    upper_count=0

    for char in input_string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return lower_count, upper_count

def in_the_range(number_to_check, range_start, range_end):
    return range_start<= number_to_check <= range_end


if __name__ == "__main__":
    main()