import re
encoded = input()
if not 1 <= len(encoded) <= 100: exit(f"1<= len({encoded})<=100")
if encoded.count("  ") != 0 or encoded.count("   ") != 0:
    exit(f"sentence has more than 1 space.")

decoded= " "
i = 0
while i < len(encoded):
    c = encoded[i]
    decoded += c
    i += 1
    if c in "aeiou":
        i += 2
print(decoded)

vowels = "aeiou"
for v in vowels:
    encoded = encoded.replace(f"{v}p{v}",v)
print(encoded)

print(re.sub(r'([aeiou])p\1', r'\1', encoded))
