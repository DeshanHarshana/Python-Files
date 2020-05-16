if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    choosemark=student_marks.get(query_name)
    sum=0
    for i in choosemark:
        sum=sum+i
    print("%0.2f" % (sum/len(choosemark)))