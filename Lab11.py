import matplotlib.pyplot as plt
import os


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
            if i+2 < len(lines):
                name = lines[i].strip()
                assignment_id = lines[i+1].strip()
                points = int(lines[i+2].strip())
                assignments[assignment_id] = {'name':name,'points':points}
            else:
                break
        return assignments

def find_submissions():
    submissions = []
    sub_path = 'data/submissions'
    for i in os.listdir(sub_path):
        file_path = os.path.join(sub_path,i)
        with open(file_path,'r') as file:
            for line in file:
                line = line.strip()
                if '|' in line:
                    student_id,assignment_id,percentage = line.strip().split('|')
                    submissions.append({
                        'student_id':student_id,
                        'assignment_id':assignment_id,
                        'percentage': int(percentage)
                        })
                else:
                    break
    return submissions



def main():
    while True:
        menu()
        choice = input('\nEnter your selection:')
        if choice == '1':
            students = find_students()
            student_name = input("What is the student's name:")
            for student_id, name in students.items():
                if name == student_name:
                    total_points = 0
                    points_earned = 0
                    submissions = find_submissions()
                    assignments = find_assignments()
                    for submission in submissions:
                        if submission['student_id'] == student_id:
                            assignment = assignments.get(submission['assignment_id'])
                            if assignment:
                                total_points  += assignment['points']
                                points_earned += (assignment['points']*submission['percentage'])/100
                    grade = ((points_earned /total_points) *100)
                    print(f'{grade:.0f}%')
                    break

        elif choice == '2':
            assignment_name = input("What is the assignment name:")
            assignments = find_assignments()
            submissions = find_submissions()
            for id, assignment in assignments.items():
                if assignment['name'] == assignment_name:
                    scores = []
                    for submission in submissions:
                        if submission['assignment_id'] == id:
                            scores.append(submission['percentage'])
                    if scores:
                        print(f'Min: {min(scores)}')
                        print(f'Avg: {sum(scores)/len(scores):.0f}')
                        print(f'Max: {max(scores)}')

        elif choice == '3':
            assignments = find_assignments()
            submissions = find_submissions()
            assignment_name = input('What is the assignment name:')
            for id, assignment in assignments.items():
                if assignment['name'] == assignment_name:
                    scores = []
                    for submission in submissions:
                        if submission['assignment_id'] == id:
                            scores.append(submission['percentage'])
                    plt.hist(
                        scores,
                        bins = [0,25,50,75,100],
                        edgecolor = 'black'
                    )
                    plt.title(f'Distribution for {assignment_name}')
                    plt.xlabel("Percentage")
                    plt.ylabel('Number of Students')
                    plt.show()

























if __name__ == '__main__':
    main()