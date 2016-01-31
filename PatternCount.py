text = "ACTGTACGATGATGTGTGTCAAAG"
pattern = "TGT"
count = 0
for i in range(len(text) - len(pattern) + 1):
    check = ""
    for j in range(len(pattern)):
        check = check + text[i + j]
    if check == pattern:
        count += 1
print(count)
