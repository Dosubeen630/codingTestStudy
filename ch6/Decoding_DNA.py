# https://dmoj.ca/problem/ecoo12r1p2
# 아데닌 과 티민은 항상 서로 반대쪽, 시토신 과 구아닌 은 서로 반대쪽
# promoter -> 'TATAAT' 라는 문자열 을 찾아 그 뒤 10개를 제외한 부분 부터 전사 시작
# terminator -> 특정 패턴을 찾아서 전사 종료.
# 현재 위치에 서 6개 이상의 염기 서열을 기준 으로, 그 이후의 염기서 열이 그와 대칭적 이고 역방향 인지 확인.
# 두 개의 서로 대칭적 이고 역방향 인 염기 서열로 이루 어짐. 예를 들어, **"AGGTCC"**와 "GGACCT" 이 같은 경우가 해당됨.
# RNA 전사 -> DNA 의 해당 부분을 RNA 로 변환( 티아민 을 우라실 로 바꿔줌)

# 상보 서열을 위한 매핑
complement_map = {
    'A': 'T',
    'T': 'A',
    'G': 'C',
    'C': 'G'
}


# DNA 전사 과정 함수
def process_dna_to_rna(dna_strand):
    promoter = "TATAAT"
    promoter_length = 10

    # 1. 프로모터 위치 찾기
    promoter_index = dna_strand.find(promoter)

    # 2. 프로모터 이후 10개 뒤부터 전사 시작
    transcription_start = promoter_index + promoter_length

    # 3. 터미네이터 찾기 (대칭적 회문 구조)

    min_length = 6  # 최소 서열 길이
    terminator_start = -1
    for i in range(len(dna_strand) - transcription_start - min_length):
        j = i + min_length + transcription_start
        forward_seq = dna_strand[i+transcription_start:j]
        reverse_complement_seq = ''.join([complement_map[base] for base in forward_seq[::-1]])

        if reverse_complement_seq in dna_strand[j:]:
            terminator_start = i + transcription_start
            break

    # 4. Terminator 앞 까지의 transcription unit 추출
    transcription_unit = dna_strand[transcription_start:terminator_start]

    # 5. DNA를 RNA로 변환 (T를 U로 대체)
    rna_sequence = ''.join([complement_map[base] for base in transcription_unit]).replace('T', 'U')

    return rna_sequence


# 사용자로부터 입력받기
for i in range(5):
    dna_strand = input().strip()
    # print("input:", dna_strand, ":", end="")

    # 빈 문자열 검사
    if len(dna_strand) == 0:
        exit(f"{dna_strand}는 빈 문자열은 안 됩니다. 문자를 입력해 주세요.")

    # 대문자로만 입력받기 검사
    if not dna_strand.isupper():
        exit(f"{dna_strand}는 대문자로 입력해 주세요.")

    # 유효 하지 않은 염기 서열(A, T, C, G 외의 문자가 포함된 경우) 검사
    valid_bases = {"A", "T", "C", "G"}
    if set(dna_strand) - valid_bases:
        print(f"{i + 1}: 유효 하지 않은 DNA 염기 서열 입니다. A, T, C, G로만 구성 되어야 합니다.")
        continue

    # DNA 처리 및 RNA 전사 과정 실행
    rna_sequence = process_dna_to_rna(dna_strand)
    print(f"{i + 1}: {rna_sequence}")

# process_dna_to_rna("AGATTATATAATGATAGGATTTAGATTGACCCGTCATGCAAGTCCATGCATGACAGC")
