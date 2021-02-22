# Python에서는 constructor를 생성하거나 내부에 있는 함수를 만들때 인자에 자기 자신을 넘겨주게 됨
class Person:
    def __init__(self, param_name):
        self.name = param_name  # self기준 name 변수를 생성하여 param_name 값을 할당함

    def talk(self):
        print("안녕하세요, 제 이름은", self.name, "입니다")


person_1 = Person("유재석")
print("person_1 :", person_1.name)
person_1.talk()
person_2 = Person("박명수")
print("person_2 :", person_2.name)
person_2.talk()
