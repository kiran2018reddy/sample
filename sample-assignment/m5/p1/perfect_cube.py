"""cube"""
def main():
    """cube"""
    y_1 = int(input())
    guess_1 = 0
    for guess_1 in range(abs(y_1)+1):
        if guess_1**3 >= abs(y_1):
            break
    if guess_1**3 != abs(y_1):
        print (y_1, 'is not a perfect cube')
    else:
        if y_1 < 0:
            guess_1 = -guess_1
    print(str(y_1)+ 'is' + 'a perfect cube')
if __name__ == "__main__":
    main()
