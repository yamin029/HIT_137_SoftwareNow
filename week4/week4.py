# info  = {"yamin" : 20, "Tamu": 40, "Ana" : 20}
# for key in info:
#     print(key, info[key])

# grades = {90: "A", 80:"B", 70:"C"}
# keys = list(info.keys())
# keys.sort()
# for key in keys:
#     print(key, info[key])

hexToBinaryTable = {'0': '0000', '1':'0001', '2':'0010','3': '0011','4':'0100', '5': '0101','6':'0110', '7': '0111', '8': '1000', '9':'1001', 'A': '1010', 'B': '1011','C':'1100', 'D': '1101', 'E': '1110','F':'1111'}

def convert(number, table):
    binary = ''
    for num in number:
        binary = binary+ hexToBinaryTable[num]

    return binary

def main():
    print(convert("35A", hexToBinaryTable))

if __name__ == "__main__":
    main()