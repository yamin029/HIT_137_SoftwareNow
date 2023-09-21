# data = "Hi there!"
# for index in range(len(data)):
#     print(index, data[index])

# fileList = ['myfile.txt', 'myprogram.exe', 'yourFile.txt']
# for fileName in fileList:
#     if '.txt' in fileName:
#         print(fileName)

# sentence = input("Enter a sentence: ")
# listOfWords = sentence.split(' ')
# print("There are ", len(listOfWords), "words!")
# sum = 0
# for word in listOfWords:
#     sum += len(word)
# print("The average word length is : ", sum/len(listOfWords))

f = open('myfile.txt','w')
f.write("First Lne.\nSecond Line.\nThird Line.\n")
f.close()