with open("test text.txt") as f:
    lines = f.readlines()
    for line_num in range(len(lines)):
        lines[line_num] = lines[line_num].strip("\n")
    f.close()

new_lines = []

for line in lines:
    line = line.replace("=","$$<--$$")
    if "for" in line:
        line = line.replace(":"," do")
        line = line.replace("for","for each")
    elif "if" in line:
        line = line.replace(":"," then")
        line = line = line.replace("==","=")
        line = line = line.replace(">=","$$\geq$$")
        line = line = line.replace(">=","$$\leq$$")
    
    new_lines.append(line)

for line in new_lines:
    print(line)

def range_converter()