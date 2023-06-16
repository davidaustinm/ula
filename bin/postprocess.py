import sys
import glob

print("***In postprocess***")

HTML  = 0
LATEX = 1
mode = HTML

if len(sys.argv) < 5:
    print "postprocess requires four arguments"
    sys.exit(1)
    
if sys.argv[1] == "-l":
    mode = LATEX

inputdir = sys.argv[2]
outputdir = sys.argv[3]

inserts = sys.argv[4]
insertsin = open(inserts)
lines = insertsin.readlines()
inserts = {}
while len(lines) > 0:
    line = lines.pop(0)
    tag = line.strip()
    line = lines.pop(0)
    html = ""
    line = lines.pop(0)
    while not line.startswith("======"):
        html += line
        line = lines.pop(0)
    latex = ""
    line = lines.pop(0)
    while not line.startswith("======"):
        latex += line
        line = lines.pop(0)
    inserts[tag] = [html, latex]

if mode == HTML:
    files = glob.glob(inputdir+"/*html")
else:
    files = glob.glob(inputdir+"/*tex")

for f in files:
    fname = f[len(inputdir)+1:]
    print fname
    input = open(f)
    lines = input.readlines()

    output = open(outputdir + "/" + fname, "w")

    while(len(lines)) > 0:
        line = lines.pop(0)

        if line.find("INSERT") >= 0:
            print line
            if mode == HTML:
                index0 = line.find(r">")
                index1 = line.find(r"<", index0)
                print index0, index1
                tag = line[index0+1: index1]
                print "****", tag
                output.write(inserts[tag][mode])
            else:
                line = lines.pop(0)
                tag = line[:-2]
                print "****", tag
                output.write(inserts[tag][mode])
            continue

        
        for key in inserts.keys():
            line = line.replace(key, inserts[key][mode])
            '''
            if line.find(key) >= 0:
                output.write(inserts[key][mode])
                writeline = False;
            '''
        if mode == LATEX and line.startswith(r"\begin{document}"):
            output.write(r"\usepackage{palatino}" + "\n")

        output.write(line)

    

    input.close()
    output.close()
