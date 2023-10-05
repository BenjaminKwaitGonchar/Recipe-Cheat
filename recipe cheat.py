import docx

recipe = docx.Document()
newlines_viz = []
with open("test text.txt") as f:
    lines = f.readlines()
    f.close()

def range_converter(line):
    range_str = line.partition("range(")[1] + line.partition("range(")[2].partition(")")[0] + line.partition("range(")[2].partition(")")[1]
    realized_range = eval(range_str)
    recipeized_range = ""
    recipeized_range += (str(realized_range[0]) + ", " + str(realized_range[1]) + ", ... , " + str(realized_range[-1]) + "")
    return recipeized_range

for line in lines:
    line = line.strip("\n")
    line = line.replace("=","<--")
    line = line.replace("**","^")
    line = line.replace("%","mod")
    line = line.replace('"""',"")
    if "import" in line:
        line = ""
    if "for" in line:
        line = line.replace(":"," do")
        line = line.replace("for","for each")
    elif "if" in line:
        line = line.replace(":"," then")
        line = line = line.replace("==","=")
        line = line = line.replace(">=","≥")
        line = line = line.replace("<=","≤")
    if "def" in line:
        line = line.replace("def","Name:")
        line = line[:line.find("(")]
    if "range(" in line:
        line = line.replace(line.partition("range(")[1] + line.partition("range(")[2].partition(")")[0] + line.partition("range(")[2].partition(")")[1], range_converter(line))
    if line != '' and line.isspace() == False:
        print(line)
        recipe.add_paragraph(text=line, style=None)
        newlines_viz.append(line)

recipe.save('test output.docx')