import winsound
import time

음계 = {"도":523,"레":587, "미":659, "파":698,"솔":783,"라":880,"시":987, "또":1046}

학교종 = "솔솔라라솔솔미 솔솔미미레 솔솔라라솔솔미 솔미레미도"

for i in 학교종:
    if i == " ":
        time.sleep(1)
    else:
        windsound.Beep(음계[i], 300)