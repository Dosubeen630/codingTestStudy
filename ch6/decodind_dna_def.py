def complement(base):
    """
    염기의 상보 염기를 반환
    :return: complement_map
    """
    complement_map = {'A': 'T', 'T': 'A', 'G': 'C', 'C':'G'}

    return complement_map[base]

def get_rna_sequence_from_complementary(sequence):
    """ DNA 의 상보적 서열을 RNA 서열로 변환  ('T' -> 'U') """
    rna_sequence = ''
    for base in sequence:
        comp_base = complement(base)
        if comp_base == 'T':
            rna_sequence += 'U'
        else:
            rna_sequence += comp_base

    return rna_sequence

def get_complementary_sequence(sequence):
    """ 주어진 DNA 서열의 상보 적인 서열을 반환"""
    complementary_sequence = ''
    # 주어진 서열의 각 염기를 순차적 으로 처리
    for base in sequence:
        # 각 염기의 상보 적인 염기를 구함
        comp_base = complement(base)
        # 상보 염기를 결과 서열에 추가
        complementary_sequence += comp_base

    return complementary_sequence

def find_terminator_start(dna_sequence):
    """
    DNA 서열 에서 terminator 의 시작 위치 찾기
    min_length: 최소 서열 길이
    :return: i
    """

    sequence_length = len(dna_sequence)
    # 모든 서열의 시작점을 반복
    min_length = 6
    for i in range(sequence_length-min_length):
        j = i + min_length
        forward_seq = dna_sequence[i:j]
        reverse_complement_seq = get_complementary_sequence(forward_seq)[::-1] # 상보 서열의 역순
        if reverse_complement_seq in dna_sequence[j:]:
            return i

def find_transcription_unit(dna_sequence):
    """ Transcription unit 구하는 함수 , Promoter 뒤에서 Terminator 앞 까지의 transcription unit 을 반환"""

    promoter = "TATAAT"
    promoter_length = 10

    # Promoter 의 위치 찾기 (10자리)
    promoter_index = dna_sequence.find(promoter)

    # Promoter 뒤 에서 부터 transcription unit 이 시작
    transcription_start = promoter_index + promoter_length

    # Terminator 의 시작 위치 찾기
    terminator_start = find_terminator_start(dna_sequence[transcription_start:])

    # Terminator 앞 까지의 transcription unit 추출
    transcription_unit = dna_sequence[transcription_start:transcription_start + terminator_start]

    return transcription_unit



# 예제 DNA 서열
# dna_sequence = "AGATTATATAATGATAGGATTTAGATTGACCCGTCATGCAAGTCCATGCATGACAGC"
# dna_sequence = "AGTCTTCAAGGGGATTCCCAGGTATATAATGCAGATCGCGACGAAATATCGGGCGGGATCCATACCGACCCAGCCGCCCGA"
dna_sequence = "TATAATGGGGGAGAGACCGAGTGTTTAAGTCCCGAGGGATCGGGAGTGAGATTGAGGGAATTCCGGGAATCTCACT"

# Transcription unit 구하기
transcription_unit = find_transcription_unit(dna_sequence)

# 결과 출력
print(f"{get_rna_sequence_from_complementary(transcription_unit)}")

print(complement("A"))  # T
print(complement("G"))  # C
print(complement("T"))  # A
print(complement("C"))  # G

print(get_complementary_sequence("AGTC"))  # TCAG
print(get_rna_sequence_from_complementary("AGTC"))  # TCAG -> UCAG



