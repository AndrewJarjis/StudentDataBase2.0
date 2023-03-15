def list_names(students):
    for i, student in enumerate(students):
        print(f"{i + 1}. {student['name']}")


def get_new_student():
    student = {'name': input("Enter student name: "), 'hometown': input("Enter student hometown: "),
               'favorite_food': input("Enter student favorite food: ")}
    return student


students = [
    {"name": "Tina", "hometown": "Portland", "favorite_food": "puppy chow"},
    {"name": "Klaus", "hometown": "Frankfurt", "favorite_food": "pizza"},
    {"name": "Julia", "hometown": "Houston", "favorite_food": "shrimp"}
]

while True:
    print("Select an option:")
    print("add - Create a new student")
    print("view - Look at existing students")
    print("quit - Exit the program")
    choice = input("Enter your choice: ")

    if choice == "quit":
        print("Goodbye!")
        break
    elif choice == "add":
        new_student = get_new_student()
        students.append(new_student)
        print("Student added!")
    elif choice == "view":
        list_names(students)
        index = input("Select a student by number or name: ")
        if index.isdigit():
            index = int(index) - 1
            if 0 <= index < len(students):
                student = students[index]
                print(f"Selected student: {student['name']}")
                while True:
                    choice = input("Select an option (hometown or favorite food): ")
                    if choice == "hometown":
                        print(f"{student['name']}'s hometown is {student['hometown']}")
                        break
                    elif choice == "favorite food":
                        print(f"{student['name']}'s favorite food is {student['favorite_food']}")
                        break
                    else:
                        print("Invalid choice. Try again.")
            else:
                print("Invalid index. Try again.")
        else:
            found = False
            for student in students:
                if student['name'] == index:
                    print(f"Selected student: {student['name']}")
                    while True:
                        choice = input("Select an option (hometown or favorite food): ")
                        if choice == "hometown":
                            print(f"{student['name']}'s hometown is {student['hometown']}")
                            break
                        elif choice == "favorite food":
                            print(f"{student['name']}'s favorite food is {student['favorite_food']}")
                            break
                        else:
                            print("Invalid choice. Try again.")
                    found = True
                    break
            if not found:
                print("Invalid name. Try again.")
    else:
        print("Invalid choice. Try again.")
