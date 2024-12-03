import re

with open('input.txt', 'r') as file:
    content = file.read()
    print(content)
    
pattern = r'mul\((\d+),\s*(\d+)\)'
    
matches = re.findall(pattern, content)

print("Matches found:", matches)

total = 0 

for i in matches:
    total += (int(i[0])*int(i[1]))
    print(int(i[0])*int(i[1]))
    
print(total)

valid_mul_matches = []

enabled = True

pattern = r"(do\(\)|don\\'t\(\)|mul\((\d+),\s*(\d+)\))"

for match in re.finditer(pattern, content):
    matched_string = match.group(0)
    
    if matched_string == "do()":
        enabled = True 
    elif matched_string == "don't()":
        enabled = False 
    elif matched_string.startswith("mul"):
        if enabled:

            valid_mul_matches.append(match.groups())

print("Valid mul() instructions found:", valid_mul_matches)
valid_total = 0 

for i in valid_mul_matches:
    print(int(i[1])*int(i[2]))
    valid_total += int(i[1])*int(i[2])

print(valid_total)
