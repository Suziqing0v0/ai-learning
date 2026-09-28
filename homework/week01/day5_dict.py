students={"小明":85,"小红":92,"小刚":58}
print(students["小红"])
students["小李"]=78
print(students)
for name,score in students.items():
    print(name,score)
