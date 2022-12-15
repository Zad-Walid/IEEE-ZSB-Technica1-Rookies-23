if __name__ == '__main__':
    students = []
    no_students = int(input())
    for _ in range(no_students):
        name = input()
        degree = float(input())
        students.append([name, degree])

    students.sort(key = lambda x:x[1])

    name_of_student = []
    lowest_score = students[0][1]
    second_lowest = 0

    for i in range(no_students):
       if students[i][1] > lowest_score and second_lowest == 0:
          second_lowest = students[i][1]
       if second_lowest != 0 and students[i][1] == second_lowest:
          name_of_student.append(students[i][0])

    name_of_student.sort()
    for name in name_of_student:
        print(name)

