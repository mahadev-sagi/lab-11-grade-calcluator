import matplotlib.pyplot as plt

def menu():
    print('1. Student grade')  # should ask for a student name and calculate their entire grade.
    print('2. Assignment statistics')
    print('3. Assignment graph')
def find_students():
    students ={}
    with open("data/students.txt","r") as file:
        for line in file:
            line = line.strip()
            student_id = line[:3]
            name = line[3:].strip()
            students[student_id]=name
        return students

def find_assignments():
    assignments = {}
    with open('data/assignments.txt', "r") as file:
        lines = file.readlines()
        for i in range (0,len(lines),3):
            name = lines[i].strip()
            assignment_id = lines[i+1].strip()
            points = int(lines[i+2].strip())
            assignments[assignment_id] = {'name':name,'points':points}
        return assignments










def main():
    while True:
        menu()
        choice = input('\nEnter your selection:')
        if choice == '1':
            student_name = input("What is the student's name:")
            print(find_students())
        elif choice == '2':
            assignment_name = input("What is the assignment name:")
            print(find_assignments())




















if __name__ == '__main__':
    main()