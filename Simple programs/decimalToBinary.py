def decimalToBinary(n):
    return bin(n).replace("0b","")
if __name__ == '__main__':
    print(decimalToBinary(18))
    print(decimalToBinary(8))
    print(decimalToBinary(7))