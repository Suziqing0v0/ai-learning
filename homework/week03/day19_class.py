class student:
    def __init__(self,name,score):
        self.name=name
        self.score=score

    def say(self):
        print(f"{self.name}的分数是{self.score}")

su=student("苏子卿",85)
su.say()

hong=student("小红",92)
hong.say()

gang=student("小刚",58)
gang.say()

