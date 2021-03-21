all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "나연", "미나", "다현"]


# hash table은 시간복잡도는 상대적으로 작지만,
# 배열저장을 이용하는 구조이기 때문에 공간 복잡도는 상대적으로 커지게 된다
def get_absent_student(all_array, present_array):
    attendance_list = {}
    for name in all_array:
        attendance_list[name] = 'absent'

    for name in present_array:
        del attendance_list[name]

    for name in attendance_list.keys():
        print(name)

    return


get_absent_student(all_students, present_students)