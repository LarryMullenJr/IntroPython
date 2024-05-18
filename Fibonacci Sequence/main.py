
# define required variables
def fibonacci(first, second, count):
    # define empty list to store the F sequence
    fibonacci_sequence = []
    # check if count is less than or equal to 0
    if count <= 0:
        return fibonacci_sequence
    # check if count is 1
    elif count == 1:
        # if count is 1, append the first number to the sequence
        fibonacci_sequence.append(first)
    # check if count is 2
    elif count == 2:
        #if count is 2, append both first and second numbers to the sequence
        fibonacci_sequence.extend([first, second])
    else:
        # if count is greater that 2, append the first two numbers to the sequence
        fibonacci_sequence.extend([first, second])
        # generate additional F numbers based on the count
        for i in range(2, count):
            # calculate the next F number by adding the last two numbers
            next_num = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
            # add the next F number to the sequence
            fibonacci_sequence.append(next_num)
    # return the F sequence        
    return fibonacci_sequence

# take inputs from user
def main():
    # prompt the user to input the first number
    first = int(input("Enter the first number: "))
    # prompt the user to input the second number
    second = int(input("Enter the second number: "))
    # prompt the user to input how many times to cycle the F sequence
    count = int(input("Enter how many numbers to generate: "))
    # generate the F sequence based on user inputs
    sequence = fibonacci(first, second, count)
    # print the F sequence for the user
    print("Fibonacci sequence:", sequence)

if __name__ == "__main__":
    main()