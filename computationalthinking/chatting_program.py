import time
from winsound import Beep

print("챗봇> 안녕하세요.")
winsound.Beep(700,500); time.sleep(0.5)
print("챗봇> 나는 인공지능 채팅 로봇입니다.")
winsound.Beep(700,500); time.sleep(0.5)
print("챗봇> 당신의 이름은 무엇인가요?")
name = input("사람> ")
winsound.Beep(700,500); time.sleep(0.5)
print("챗봇>" ,name, "씨 만나서 반가워요")
winsound.Beep(700,500); time.sleep(0.5)
print("챗봇> 당신의 고향은 어디인가요?")
home = input("사람> ")
winsound.Beep(700,500); time.sleep(0.5)
print("챗봇>", name, "씨는 아름다운", home, "에서 왔군요.")
winsound.Beep(700,500); time.sleep(0.5)
print("챗봇> 안녕 다음에 또 만나요.")