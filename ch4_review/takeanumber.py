# https://dmoj.ca/problem/ecoo13r1p1
# 출석 관리 프로그램. take는 지각 학생. serve는 정시 도착. close는 출결 기계가 서비스 마감.
# 사용자로 부터 기계의 시작 번호 입력 받음. 지각 학생 수와 정시 도착한 학생 수 입력 받고 서비스 마감 관련 정보 제공받음.
# 출력은 지각 학생 수, 출결 기계 문닫고 줄을 서 있는 학생 수 , 다음 날 기계 에서 시작 할 때 다음 수
# 지각한 학생 수는 다음 날 기계 에서 시작 할때 표시 되는 다음 수와 관련 있음.


machine_numb = input()
if not machine_numb.isdigit():exit(f"{machine_numb} != digit")
machine_numb = int(machine_numb)
if not 0 < machine_numb < 1000: exit(f"범 위 벗어남. (0 < {machine_numb} < 1000)")

late_student_num = 0
waited_student_num = 0
next_machine_numb = machine_numb

isCLOSED = False
while not isCLOSED:
    student_state = input()
   # if not student_state.isupper():exit(f"{student_state} != upper")

    if student_state == 'CLOSE':

        print(f"{late_student_num}, {waited_student_num}, {next_machine_numb}")
        late_student_num = 0
        waited_student_num = 0

    elif student_state == 'TAKE':
        late_student_num += 1
        waited_student_num += 1
        next_machine_numb += 1

        if machine_numb == '999':
            machine_numb = '1'

    elif student_state == 'SERVE':
        waited_student_num -= 1

    else: # and student_state == 'EOF':
        isCLOSED = True
        break









