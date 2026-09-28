def get_grade(score):
    if score >=90:
        return"优秀"
    elif score >=80:
        return"良好"
    elif score >=70:
        return"中等"
    elif score >=60:
        return"及格"
    else :
        return"不及格"

student={"小明":85,"小红":92,"小刚":58,"小李":78,"小张":90,"小王":66}
def get_average(scores):
    return sum(scores)/len(scores)
print("平均分：",round(get_average(student.values()),1))
for name,score in student.items():
    print(name,score,get_grade(score))

best_name=""
best_score=0
for name,score in student.items():
    if score>best_score:
        best_score=score
        best_name=name
print("最高分",best_name,best_score) 