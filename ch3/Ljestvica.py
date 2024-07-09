# https://dmoj.ca/problem/coci12c5p1
# Veronica attends a music academy. She was given a music sheet of a composition with only notes (without annotations), and needs to recognise the scale used.
# 베로니카는 음악학교에 다니고 있다. 그녀에게 주어진 음악악보는 오직 주석이 없는 노트뿐이다. 그리고 그녀는 음계를 알아차리는 것이 필요하다.
# In this problem, we will limit ourselves to only the two most frequently used (and usually taught in schools first) scales: A-minor and C-major.
# 여기에 문제는 우리는 오직 자주 빈번하게 사용된 두 가지의 음계 A-minor and C-major만 아는 것이 한계이다.
# This doesn't make them simpler or more basic than other minor and major scales – all minor scales are mutually equivalent save for translation, and so are major scales.
# 이것이 다른 마이너 및 메이저 음계보다 더 단순하거나 더 기본적이지는 않습니다. 번역을 제외하면 모든 마이너 음계는 상호 동등하며 메이저 음계도 마찬가지 입니다.
# Still, out of the 12 tones of an octave {A,A#, B,C,C#,D,D#,E,F,F#,G,G#} used in modern music, A-minor and  C-major scales do use the tones with shortest names:
# A-minor is defined as an ordered septuple (A,B,C,D,E,F,G), and C-major as (C,D,E,F,G,A,B).
# 아직도 12옥타브의 톤, 현대 음악에서 사용되는 A단조와 C장조 음계는 가장 짧은 이름의 음을 사용합니다. A단조는 순서화된 7중주(A,B,C,D,E,F,G)로 정의되고, C장조는 (C,D,E,F,G,A,B)로 정의됩니다.
# Notice that the sets of tones of these two scales are equal.
# 이 두 음계의 음색 세트가 동일하다는 점에 유의 하십시오.
# The catch is that not only the set of tones, but also their usage, determines a scale.
# 문제는 톤세트 뿐만 아니라 그 사용법도 음계를 결정한다는 것입니다.
# Specifically, the tonic (the first tone of a scale), subdominant (the fourth tone) and dominant (the fifth tone) are the primary candidates for accented tones in a composition.
# 구체적으로 말하면 토닉(음계의 첫번째 성조), 하위 도미넌트(네번째 성조), 도미넌트(다섯번째 성조)는 작곡에서 강세를 주는 주요한 후보입니다.
#  In A-minor, these are A,D, and E, and in C-major, they are C,F, and G. We will name these tones main tones.
# A단조에서 A,D,E 이고, C장조에서는 C,F,G 입니다. 이 음을 주음이라고 부르겠습니다.
# Aren't the scales still equivalent save for translation? They are not: for example, the third tone of A-minor (C) is three half-tones higher than the tonic (A), while the third tone of
# C-major (E)is four halftones higher than the tonic (C). The difference, therefore, lies in the intervals. This makes minor scales "sad" and major scales "happy".
# 번역을 제외하면 척도는 여전히 동일하지 않나요? 예를들어, A단조(C)의 세번째 성은 토닉(A)보다 세개의 반음 더 높지만, A단조의 세번째 성은 그렇지 않습니다.
# 다장조(E)는 토닉(C)보다 4개의 반음이 높습니다. 따라서 차이점은 간격에 있습니다. 이는 단음계를 "슬프게" 만들고 장음계를 "행복하게" 만듭니다.
# Write a program to decide if a composition is more likely written in  A-minor or  C-major by counting whether there are more main tones of  A-minor or of
# C-major among the accented tones (the first tones in each measure).
# A단조나 C장조로 작곡될 가능성이 더 높은지 여부를 계산하여 A단조 또는 C장조로 작곡할 가능성이 더 높은지 결정하는 프로그램을 작성하세요.
# 악센트 톤 중 C장조(각 소절의 첫번째 톤)
# If there is an equal number of main tones, determine the scale based on the last tone (which is guaranteed to be either A for A -minor or C for C -major in any such test case).
# 동일한 수의 기본 톤이 있는 경우 마지막 톤을 기준으로 스케일을 결정합니다.(이러한 테스트 사례에서 A단조의 경우, A,C장조의 경우가 C가 보장됩니다.)
# The character | separates measures, so the accented tones are, in order:
# 캐릭터 | 마디를 구분하므로 악센트 톤은 다음과 같습니다.
# C,E,C,E,E,G,E,G,G,E,G,E,C,C,C,C. Ten of them (C,C,G,G,G,G,C,C,C,C) are main tones of C-major, while six (E,E,E,E,E,E) are main tones of A-minor.
# Therefore, our best estimate is that the song was written in  C-major.
# C,E,C,E,E,G,E,G,G,E,G,E,C,C,C,C. 그중 10개 (C,C,G,G,G,G,C,C,C,C)가 다장조의 주음이고, 6개의 (E,E,E,E,E,E)가 A마이너 주음 입니다.
# 그러므로 우리의 최선의 추정은 이곡이 C장조로 쓰여졌다는 것입니다.
# The first and only line of input contains a sequence of at least 2 , and at most 100, characters from the set {A,B,C,D,E,F,G,|}.
# 입력의 첫번째 이자 유일한 줄에는 {A,B,C,D,E,F,G,|} 세트의 문자 시퀀스가 최소 2개, 최대 100개 포함됩니다.
# This is a simplified notation for a composition, where the character | separates measures. The characters | will never appear adjacent to one another, at the beginning, or at the end of the sequence.
# 이는 구성에 대한 단순화된 표기법입니다. 문자 | 조치를 구분합니다. 캐릭터 | 시퀀스의 시작부분이나 끝 부분에는 서로 인접해 표시되지 않습니다.
# The first and only line of output must contain the text C-dur (for C-major) or A-mol (for A-minor).
# 출력의 첫번 째이자 유일한 줄에는 C-dur(C장조 의경우) 또는 A-mol(A단조의 경우) 텍스트가 포함되어야 합니다.

sequence = input()

#if not sequence.isalpha():
#exit("잘못된 형태의 입력입니다.")
#if not 2 <= len(sequence) <= 100:
#exit("범위를 초과하였습니다.")

a_minor = 0
c_major = 0

for i in range(len(sequence)):
    #카운팅을 할때, 만약에 A and C가 함께 나오면 먼저 나온 순서로 카운팅
    if i == 0 or sequence[i-1] == '|':
        if sequence[i] in 'ADE':
            a_minor += 1
        if sequence[i] in 'CFG':
            c_major += 1

if a_minor > c_major:
    print('A-mol')
elif a_minor == c_major and sequence[-1] == 'A':
    a_minor += 1
    print('A-mol')
elif a_minor == c_major and sequence[-1] == 'C':
    c_major += 1
    print('C-dur')
else: # a_minor 가 c_major 보다 작을때,
    print('C-dur')
