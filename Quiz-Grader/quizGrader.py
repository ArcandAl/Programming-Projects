# Alec Arcand
import os
import os.path


def main():
    directoryList = os.listdir('.')  # '.' indicates the current directory
    gradeSheet = studentNames()
    nameToName = fileNames()
    poss = []
    for dirItem in directoryList:
        if os.path.isdir(dirItem):
            os.chdir(dirItem)   # Go into subdirectory
            gradeQuiz(gradeSheet, nameToName) #grade that quiz for all 4 students
            possible = possiblePoints(poss)
            os.chdir('..')

    formatted(gradeSheet, sum(possible))

def fileNames():
    bothnames = {}
    students = open('students.txt', 'r')
    for line in students:
        line = line.rstrip()
        line1 = line
        line = line.casefold()
        line = line.replace(', ', '_')
        bothnames[line1] = line
    return bothnames

def studentNames():
    results = {}
    students = open('students.txt', 'r')
    for line in students:
        line = line.rstrip()
        results[line] = []
    students.close()
    return results

def gradeQuiz(studentDict, nameToName):
    answerFile = open('answers.txt', 'r')
    answerKey = answerFile.readlines()
    for student, studentFileName in nameToName.items():
        studentFile = open(studentFileName + str('.txt'), 'r')
        studentAnswers = studentFile.readlines()
        correctCount = 0
        for line1, line2 in zip(answerKey, studentAnswers):
            if line1 == line2:
                correctCount += 1
            else:
                correctCount += 0

        studentDict[student].append(correctCount)
    return studentDict

def possiblePoints(poss):
    possible = poss
    for filename in os.listdir('.'):
        if 'answers' in filename:
            quiz = open(filename, 'r')
            for i in quiz:
                possible.append(1)
    return possible

def percent(total, possible):
    total = sum(total)
    percent = (total / possible) * 100
    return percent

def formatted(results, poss):
    gradeFile = open('gradeReport.txt', 'w' )
    gradeFile.write("Student Quiz Report".center(36) + "\n\n\n")
    gradeFile.write("%-15s %9s %9s %9s %9s %9s %9s %9s %20s %18s \n" % ("Student Name", "Quiz 1", "Quiz 2", "Quiz 3", "Quiz 4", "Quiz 5", "Quiz 6", "Quiz 7", "Total Quiz Points", "Overall Quiz %"))
    gradeFile.write("-"*125+"\n")

    lst = []
    for i in results:
        lst.append([i, sum(results[i]), percent(results[i], poss)])



    for i in lst:
        studentName = i[0]
        totalPoints = i[1]
        overallQuiz = i[2]
        for i in results:
            quiz1 = int(results[i][0])
            quiz2 = int(results[i][1])
            quiz3 = int(results[i][2])
            quiz4 = int(results[i][3])
            quiz5 = int(results[i][4])
            quiz6 = int(results[i][5])
            quiz7 = int(results[i][6])

        gradeFile.write("%-15s %7s %9s %9s %9s %9s %9s %7s %15s %20.1f\n" % (studentName, quiz1, quiz2, quiz3, quiz4, quiz5, quiz6, quiz7, totalPoints, overallQuiz))


main()
