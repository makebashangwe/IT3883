
class Students:
    students = []

    def __init__(self, name, scores):
        self.name = name
        self.scores = scores


    def summary(self):
        print(f"Name: {self.name}\nScores: {self.scores}")

    def average(self):
        sum = 0
        for score in self.scores:
            sum += score
        return sum / len(self.scores)

    def average_of_all_students(self):
        total = 0
        for student in Students.students:
            total += student.average()

        average_of_all_students = total / len(Students.students)
        return average_of_all_students
def main():
    try:
        user_file = open("Assignment2input.txt", "r")

        for line in user_file:
            if line.strip() == "":
                continue
            else:
                raw_data = str(line).strip("\n").split(" ")
                name = raw_data[0]
                raw_data.remove(name)
                
                if len(raw_data) == 0:
                    print("Invalid input. Student has no scores.")
                    continue
                try:
                    scores = list(map(int, raw_data))
                    student = Students(name, scores)
                    Students.students.append(student)
                except ValueError:
                    print("Invalid input. Please try again.")


        user_file.close()

    except FileNotFoundError:
        print("Input file was not found.")

    except ValueError:
        print("Invalid input. Please try again.")
    except Exception:
        print("Invalid input. Please try again.")

    total = 0
    for student in Students.students:
        total += student.average()

    print("Student Summary:")
    for student in Students.students:
        student.summary()
    print(f"There are {len(Students.students)} students in total.")

    if len(Students.students) > 0:
        average_of_all_students = total / len(Students.students)
        print(f"The average of all students is {round(average_of_all_students,2)}.")
    else:
        print("No valid student records found.")


main()