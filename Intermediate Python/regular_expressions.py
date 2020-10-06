import re


# Can you write a regular expression that will match each line,
# extracting the title and surname for each person?

lines = open("greetings.txt", "r").readlines()

for line in lines:
    alt_title = re.search(r"(Mr|Miss|Ms|Mrs|Dr|Rev)(\.|\s)", line)
    alt_name = re.search(r"[A-Z](\w+)n", line) # could also have finished with (n or ,)
    print(alt_title.group(0), alt_name.group(0))


import re

lines = open("greetings.txt", "r").readlines()

for line in lines:
    m = re.search(r"Dear\s+(M[r]?[s]?|Miss|Dr|Rev)[\.|\s]\s*(\w+)", line)
    if m:
        print("Title = %s, surname = %s" % (m.group(1), m.group(2)))


# r"Dear\s+(M[r]?[s]?|Miss|Dr|Rev)[\.|\s]\s*(\w+)"
# Dear followed by 1 or more spaces followed by the first group
# This group contains M followed by 0 or 1 r followed by
# 0 or 1 s (Matching Mr, Ms or Mrs), or it contains Miss,
# or it contains Dr or it contains Rev). This is followed
# by a full stop or a space, followed by 0 or more spaces,
# followed by the second group. This second group
# contains 1 or more word characters, thus matching
# the surname. Phew!!!

hamlet_lines = open("textfile.txt", "r").readlines()

for h_line in hamlet_lines:
    line = re.sub(re.compile(r"the\s(\w+)", re.IGNORECASE), "the apple", h_line)
    print(line)
