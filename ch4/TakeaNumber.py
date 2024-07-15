# https://dmoj.ca/problem/ecoo13r1p1
# Due to overwhelming demand, the principal has installed one of those "take a number" dispensers to help the attendance secretary manage the line for late slips.
# 압도적인 수요로 인해 교장은 출석 비서가 지각전표 줄을 관리하는데 도움이 되도록 "번호확인" 분배기 중 하나를 설치했습니다.
# The dispenser is filled with slips of paper numbered in order from 1 to 999.
# 디스펜서에는 1부터 999까지 번호가 매겨진 종이 쪽지가 가득 들어 있습니다.
# The principal has made sure to order lots of refills! The attendance desk opens at 8:00 am every morning and closes at 3:00 pm.
# 교장 선생님께서 리필을 많이 주문해 주셨어요. 출석 데스크는 매일 아침 8시에 열고 오후 3시에 닫힙니다.
# When a late student arrives they take the next number from the machine, and when the attendance secretary is ready, he calls the next number in order.
# 지각한 학생이 도착하면 기계에서 다음 번호를 가져오고, 출석 비서가 준비되면 순서대로 다음 번호로 전화를 겁니다.
# When a student takes the last number, the secretary immediately refills the machine with a new set of numbers from 1 to 999.
# 학생이 마지막 번호를 선택하면 비서가 즉시 1 부터 999까지의 새로운 번호 세트를 기계에 다시 채워 줍니다.
# At 3:00 pm, he removes the dispenser and stores it for the next day, then serves any students who are still waiting with numbers in their hands before closing for the day.
# 오후 3시에 그는 디스펜서를 제거하고 다음 날을 위해 보관한 다음, 그 날 마감되기 전에 여전히 손에 숫자를 들고 기다리고 있는 모든 학생들에게 서비스를 제공합니다.
# You will be given detailed data for a number of days in the late slip lineup. The first line contains an integer N (0 < N < 1000) representing the next number in the take a number machine.
# 지연 전표 라인 업의 일수에 대한 상세 데이터를 제공 해드립니다. 첫번째 줄에는 숫자입력 기계의 다음 숫자를 나타내는 정수 N( 0<N<1000)이 포함되어 있습니다.
# This will be followed by some number of lines (up to 1000000) representing the activity at the attendance desk.
# 다음에는 출석 데스크 에서의 활동을 나타내는 몇줄(최대 1000000)이 표시 됩니다.
#  If a line contains the word TAKE, it means a student has arrived and taken the next number (when a student takes the last number available, the machine is immediately refilled).
# 만약 줄에 TAKE 라는 단어가 포함 되어 있으면 학생이 도착하여 다음 번호를 선택했음을 의미합니다. (학생이 사용 가능한 마지막 번호를 선택하면 기계가 즉시 채워집니다.)
#  If a line contains the word SERVE it means that the attendance secretary has served the next student in line (this word will only appear in the file when there is at least one student waiting).
# 만약 줄에 SERVE라는 단어가 포함 되어 있으면 출석 비서가 줄의 다음 학생에게 서비스를 제공했다는 의미입니다.( 이 단어는 대기하는 학생이 한 명 이상 있을 때만 파일에 나타납니다.)
#  If a line contains the word CLOSE it means that the desk has closed for the day and the attendance secretary will serve the students remaining in line and then go home. The very last line will contain the string EOF.
# 만약 줄에 CLOSE 라는 단어가 포함되어 있으면 책상이 그날 문을 닫았다는 의미 이며 출석 담당 비서가 줄에 남아 있는 학생들에게 서비스를 제공한 후 집으로 돌아갑니다. 맨 마지막 줄에는 EOF 문자열이 포함 됩니다.
# At no time will there be more than 999 students waiting in line to be served.
# 서비스를 받기 위해 줄을 서서 기다리는 학생이 999명을 넘지 않습니다.
# Your job is to keep track of the line. Each time you encounter the word CLOSE, you must print three integers on a single line, each separated by a single space.
# 당신의 임무는 라인을 추적 하는 것입니다. CLOSE 라는 단어가 나올때 마다 공백으로 구분 된 세개의 정수를 한 줄에 인쇄 해야 합니다.
# The first integer represents the number of students who were late that day, the second integer represents the number of students who remained in line after the desk was closed, and the third integer represents the next number in the take a number machine for the next day.
# 첫번째 정수는 그날 지각한 학생 수를 나타내고 두번재 정수는 책상이 닫힌 후에도 줄을 서서 기다린 학생 수를 나타내며, 세번째 정수는 다음날 숫자 입력 기계의 다음 숫자를 나타 냅니다.

# TAKE - 다음 번호를 선택한 학생수( 지각한 학생 수), SERVE - 다음 학생 에게 서비스 제공 (take수 - serve수 : 책상 닫힌 후 기다린 학생 수), 다음날 머신의 수 - 이전 머신의 수에서 지각한 학생수 더해줌
late = 0 # 지각한 학생 수
waiting = 0 # 기다린 학생 수
#finish = False
next_number = input()
if not next_number.isdigit(): exit(f"{next_number} != digit")
next_number = int(next_number)
if not 0 < next_number < 1000: exit(f"0< {next_number}< 1000")

#while not finish:
while True:
    attendance_desk_state= input()
    if not attendance_desk_state.isupper(): exit(f"{attendance_desk_state} != upper")
    if not len(attendance_desk_state) < 999: exit(f"{attendance_desk_state} < 999")

    if attendance_desk_state == 'TAKE':
        late += 1
        waiting += 1
        next_number += 1
       # late = attendance_desk_state.count('TAKE')

        if next_number == 1000: # 출석 기계의 번호가 최대 999 이므로 그 범위 넘어 가면 자동 으로 1로 다시 초기화
            next_number = 1

    elif attendance_desk_state == 'SERVE':
        waiting -= 1 # 서비스를 제공 받았으므로 기다 리는 학생 수가 줄어듬.
       # waiting = attendance_desk_state.count('SERVE')
        # 처음에는 수를 세는 것이니 count를 쓰고 싶었 는데 카운트를 사용 하니 매 입력시 입력 되는 단어의 수 1만 출력됨.

    elif attendance_desk_state == 'CLOSE':
        print(late, waiting, next_number)
        late = 0 # 출력 후에 초기화 해주지 않으면 기존의 값과 더해져서 출력 됨.
        waiting = 0 # 출력 후에 초기화 해주지 않으면 기존 값과 더해져서 출력됨.

   # elif attendance_desk_state == 'EOF':
     #   finish = True

    else:
        break  # 위의 EOF 인 경우에 take, serve,close 어느 경우에도 해당 되지 않아
               # 어짜피  루프 종료 됨.