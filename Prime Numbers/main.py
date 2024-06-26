def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def main():
    user_input = int(input("Enter a number: "))
    print("Prime numbers between 2 and", user_input, "are:")
    for num in range(2, user_input + 1):
        if is_prime(num):
            print(num, end=" ")

if __name__ == "__main__":
    main()