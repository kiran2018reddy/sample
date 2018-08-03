# Write a python program to find if the given number is a perfect cube or not
# using guess and check algorithm

# testcase 1
# Input: 24389
# Output: 24389 is a perfect cube

# testcase 2
# Input: 21950
# Output: 21950 is not a perfect cube

def main():
	# input is captured in s
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
