def runner(n,*args):
    students = []
    marks = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])

for x in range(5):
    marks.append(students[x][1])
a = sorted(set(marks))

second = []
for i in students:
    if i[1] == a[1]:
        second.append(i[0])

second.sort()
for i in second:
    print(i)

if __name__ == '__main__':

