import time
from grade_utils import calculate_average, determine_grade

def main():
    print("--- Student Grade Tracker CLI ---")
    
    # List to store student marks
    marks = []
    
    while True:
        try:
            print("\nOptions:")
            print("1. Add a subject mark")
            print("2. Calculate Result")
            print("3. Exit")
            
            choice = input("Enter choice (1-3): ")
            
            if choice == '1':
                mark = float(input("Enter subject mark (0-100): "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    print(f"Mark {mark} added.")
                else:
                    print("Invalid mark! Please enter between 0 and 100.")
            
            elif choice == '2':
                if not marks:
                    print("No marks added yet.")
                else:
                    avg = calculate_average(marks)
                    grade = determine_grade(avg)
                    print(f"\n--- Results ---")
                    print(f"Total Subjects: {len(marks)}")
                    print(f"Average Score: {avg:.2f}")
                    print(f"Final Grade: {grade}")
                    
            elif choice == '3':
                print("Exiting...")
                break
            
            else:
                print("Invalid choice, try again.")
                
        except ValueError:
            print("Error: Please enter a valid number.")

if __name__ == "__main__":
    main()