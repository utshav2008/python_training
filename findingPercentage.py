if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

avg = ( student_marks[query_name][0] + student_marks[query_name][1] + student_marks[query_name][2] )/3

print("%.2f" % avg)


### Learn
## what _ does?
## what *line does?
## printing formated floats