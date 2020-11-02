lorem_text = open('./lorem_text.txt', 'r')

# ------------------------
# print(lorem_text.read())
# ------------------------
# print(lorem_text.read(100))
# ------------------------
# lorem_text.seek(5)
# print(lorem_text.read(100))
# ------------------------
# print(lorem_text.readline())
# print(lorem_text.readline())
# print(lorem_text.readline())
# ------------------------
# print(lorem_text.readlines()[2])
# ------------------------
# for line in lorem_text:
#     print(len(line))
#     print(line)
#     print(len(line.split()))
# ------------------------

lorem_text.close()
# --------------------------------------------------------------------------------------


def sequence_filter(line):
    return '>' not in line


with open('./dna_sequence.txt') as dna_sequences:
    lines = dna_sequences.readlines()
    print(list(filter(sequence_filter, lines)))
