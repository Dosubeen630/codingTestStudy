# https://dmoj.ca/problem/coci16c1p1
# Pero has negotiated a Very Good data plan with his internet provider.
# 페로는 그의 인터넷 공급자와 매우 좋은 데이터 계획을 가지고 협상을 하려고 한다,
# The provider will let Pero use up X megabytes to surf the internet per month.
# 그 공급자는 한 달에 x메가바이트를 사용 할 수 있다.
# Each megabyte that he doesn't spend in that month gets transferred to the next month and can still be spent.
# 각 메가바이트는 그가 한 달동안 다 사용하지 못하면 다음달로 이월되어 넘어가서 사용 할수 있다.
# Of course, Pero can only spend the megabytes he actually has.
# 물론, 페로는 오직 그가 제공받은 메가바이트만 실제로 사용할 수 있다.
# If we know how many megabytes Pero has spent in each of the first N months of using the plan, determine how many megabytes Pero will have available in the N+1
# month of using the plan.
# 만약 우리는 페로가 얼마나 많은 메가바이트를 각 달에 사용하였는지 알고 그것으로 얼마나 많은 데이터를 다음달에 사용 할 수 있는지를 결정할 수 있다.
# The first line of input contains the integer X(1<=X<=100).
#  첫번째 줄에는 정수 X를 입력한다. 범위는 1 이상 100이하이다.
# The second line of input contains the integer N (1<=N<=100).
# 두번째 줄에는 정수 N을 입력해준다. 범위는 1이상 100이하이다.
# Each of the following
#  lines contains an integer Pi(0<=pi<+10000) ,the number of megabytes spent in each of the first
# N months of using the plan. Numbers pi will be such that Pero will never use more megabytes than he actually has.
# 각 줄에 따라오는 N라인에 포함된 정수 Pi는 첫번째 N달에 사용한 메가바이트를 나타내고, Pi는 페로가 사용하지 않은 그가 실제로 사용할 수 있는 메가바이트를 나타낸다.
# The first and only line of output must contain the required value from the task.
# 출력란에는 한줄로 오직 한줄로 그 업무로 마지막달의 사용량과 이전달에서 이월된 메가바이트양을 합산해서 총 사용할 수 있는 데이터량을 표시해준다.

# 제공되어 지는 메가바이트양과 보여줄 달을 입력 받는다.
mega_bite = input()
if not mega_bite.isdigit():
    exit("입력된 값이 형태가 잘못 되었습니다.")
mega_bite = int(mega_bite)
if not 1<= mega_bite <= 100:
    exit(" 입력된 값의 범위가 큽니다.")
show_month = input()
if not show_month.isdigit():
    exit("입력된 값이 형태가 잘못 되었습니다.")
show_month = int(show_month)
if not 1 <= show_month <= 100:
    exit(" 입력된 값의 범위가 큽니다.")
# 주어진 달 동안 사용 되고 남은 이월된 데이터 저장 변수 선언
total_bite = 0
# 두번째에서 입력받은 보여줄 달의 숫자에 따라 그 수만큼 입력을 더 받는 것을 구현
for n in range(show_month):
    # show_month가 0이 아니면 계속 입력받고
    if show_month !=0:
        # 입력된 각 달의 데이터 사용량 저장변수
        used_bite = int(input())
        total_bite = (total_bite + mega_bite) - used_bite
    else: # show_month가 0이 되면 반복문 종료
        pass
# provide_bite = (mega_bite * show_month) + mega_bite 데이터 총 제공량
result = total_bite + mega_bite
print(result)

