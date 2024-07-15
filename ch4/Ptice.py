# https://dmoj.ca/problem/coci08c1p2
# Adrian, Bruno and Goran wanted to join the bird lovers' club.
# 아드리안, 브루노 및 고란은 새 애호가 클럽에 가입 하기를 원했습니다.
# However, they did not know that all applicants must pass an entrance exam.
# 그러나 그들은 모든 지원자가 입학 시험에 합격 해야 한다는 사실을 몰랐 습니다.
# The exam consists of N questions, each with three possible answers: A, B and C.
# 시험은 N개의 질문 으로 구성 되며 각 질문 에는 A,B,C의 세가지 답이 있습니다.
# Unfortunately, they couldn't tell a bird from a whale so they are trying to guess the correct answers.
# 불행 하게도 그들은 새와 고래를 구별 할 수 없어서 정답을 추측 하려고 노력 하고 있습니다.
# Each of the three boys has a theory of what set of answers will work best:
# 세 소년은 각각 어떤 대답이 가장 효과적 인지에 대한 이론을 가지고 있습니다.
# Adrian claims that the best sequence is: A,B,C,A,B,C,A,B,C,A,B,C,...
# 아드리안은 가장 좋은 수서는 다음과 같다고 주장 합니다.
# Bruno is convinced that this is bette: B,A,B,C,B,A,B,C,B,A,B,C,...
# 브루노는 이것이 최선 이라고 확신 합니다.
# Goran laughs at them and will use this sequence: C,C,A,A,B,B,C,C,A,A,B,B,...
# 고란은 그들을 비웃으며 다음 순서를 사용 합니다.
# Write a program that, given the correct answers to the exam, determines who of the three was right – whose sequence contains the most correct answers.
# 시험에 대한 정답이 주어 지면 세가지 중 누가 옳았는지 결정 하는 프로 그램을 작성 하세요. 그 순서 에는 가장 정답이 포함 되어 있습니다.
# The first line contains an integer N(1<=N<=100), the number of questions on the exam.
# 첫번째 줄에는 시험 문제 수인 정수 N이 포함 됩니다.
# The second line contains a string of N letters A, B and C. These are, in order, the correct answers to the questions in the exam.
# 두번째 줄에는 다음 문자 열이 포함 됩니다. 문자 A,B,C. 이것은 순서 대로 시험 문제에 대한 정답 입니다.
# On the first line, output M, the largest number of correct answers one of the three boys gets.
# 첫번째 줄에는 세 남학생 중 한 명이 얻은 가장 많은 정답 수 인 M을 출력 합니다.
# After that, output the names of the boys (in alphabetical order) whose sequences result in M correct answers.
# 그 후, M개의 정답이 나온 남자 아이의 이름을 (알파벳 순으로) 출력 합니다.

# 도메인 분석: 사용자로 부터 시험문제 수, 시험 정답을 입력 받음.
# 출력으로 세 남자 아이중 정답을 맞힘 개수와 누가 정답을 많이 맞추었는지 이름 출력 (고려사항: 맞힌 수가 비슷하거나 같으면 이름 알파벳 순서대로 출력해라.)
# 아드리안 -> A,B,C 순석대로 / 브루노 -> B,A,B,C / 고란 -> C,C,A,A,B,B

# 입력 값의 유효성 체크
problem_num = input()
if not problem_num.isdigit() : exit(f"{problem_num} != digit")
problem_num = int(problem_num)
if not 1 <= problem_num <= 100: exit(f"1 <= {problem_num} <= 100")

correct_answers = input()
if not correct_answers.isupper(): exit(f"{correct_answers} != upper")


adrian_pattern = "ABC" # 우선, 아드 리안 정답의 패턴을 선언!
bruno_pattern = "BABC"
goran_pattern = "CCAABB"

index = 0 # 패턴의 반복을 위해 인덱스 변수 선언
a_count = 0 # 아드 리안 정답 개수 카운팅 을 위한 변수 선언
b_count = 0 # 브루노 정답 개수 카운팅 을 위한 변수 선언
g_count = 0 # 고란 정답 개수 카운팅 을 위한 변수 선언

#while True:
for i in range(len(correct_answers)):
    adrian_answer = adrian_pattern[index % len(adrian_pattern)] # 나머지 연산자 사용 하여 정답의 길이 만큼 학생의 답 패턴을 맞춰줌.
    bruno_answer = bruno_pattern[index % len(bruno_pattern)]
    goran_answer = goran_pattern[index % len(goran_pattern)]

    index += 1
    if correct_answers[i] == adrian_answer:
        a_count += 1


    if correct_answers[i] == bruno_answer:
        b_count += 1


    if correct_answers[i] == goran_answer:
        g_count += 1


most_answer = a_count # 정답을 가장 많이 맞춘 개수 비교 ,
                    # 아드 리안의 답이 가장 많이 정답과 일치 할때, 다른 학생 답과 비교 하여 가장 많은 정 답수 구하기
if b_count > most_answer:
    most_answer = b_count
if g_count > most_answer:
    most_answer = g_count

print(most_answer)

# 가장 정답을 많이 맞춘 학생 이름 출력 하기
if a_count == most_answer:
    print("Adrian")
if b_count == most_answer:
    print("Bruno")
if g_count == most_answer:
    print("Goran")




