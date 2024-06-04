def input_grades():
    grades = {}
    try:
        with open('grades.txt', 'r') as file:
            for line in file:
                subject, grade = line.strip().split(',')
                grades[subject] = float(grade)
    except FileNotFoundError:
        print("No previous grades found.")
    except Exception as e:
        print(f"Error reading grades: {e}")
    
    while True:
        subject = input("Enter subject name (or type 'done' to finish): ")
        if subject.lower() == 'done':
            break
        try:
            grade = float(input(f"Enter grade for {subject}: "))
            grades[subject] = grade
        except ValueError:
            print("Invalid input. Grade must be a number.")

    with open('grades.txt', 'w') as file:
        for subject, grade in grades.items():
            file.write(f"{subject},{grade}\n")

def calculate_average():
    try:
        with open('grades.txt', 'r') as file:
            total_grade = 0
            count = 0
            for line in file:
                _, grade = line.strip().split(',')
                total_grade += float(grade)
                count += 1
            if count == 0:
                print("No grades found.")
            else:
                average = total_grade / count
                print(f"Average grade: {average:.2f}")
    except FileNotFoundError:
        print("No grades found.")
    except Exception as e:
        print(f"Error calculating average: {e}")

def main():
    while True:
        print("\n*** Student Grade Tracker ***")
        print("1. Input grades")
        print("2. Calculate average grade")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            input_grades()
        elif choice == '2':
            calculate_average()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()