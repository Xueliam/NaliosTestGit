
def Fizzbuzz(dict):
    for i in range(1, 101):
        output = ''
        for multiple, word in dict.items():
            if i % int(multiple) == 0:
                output += word
        print(output if output else i)


