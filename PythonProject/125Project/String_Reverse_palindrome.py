
if __name__ == '__main__':
    stringN = input()
    new_string = ''
    # print(stringN[::-1])
    '''To reverse string'''
    for i in range(len(stringN)):
        new_string += stringN[len(stringN) - i - 1]
    print(new_string)
    '''To judge if palindrome string'''
    if stringN == new_string:
        print('This is palindrome word')