import sys
amp = r" \amp "
minus= r" {}-{} "
plus = r" {}+{} "
equal= r" {}={} "
end  = r" \\"
newline = "\n"

if len(sys.argv) < 2:
    print "Give a file name"
    sys.exit(1)

filename = sys.argv[1]
print filename
input = open(filename)
lines = input.readlines()

line = lines.pop(0)
variables = line.split()
N = len(variables)

multi = False
if len(lines) > 1:
    multi = True

s = r"\begin{alignedat}{"+str(N+1) + r"}" + newline

while len(lines) > 0:
    line = lines.pop(0)
    tokens = line.split()
    first = True
    for i in range(N):
        if tokens[i] == "0":
            s = s + amp + amp
            continue
        if first:
            if tokens[i] == "1":
                s = s + variables[i] + amp
            elif tokens[i] == "-1":
                s = s + "-" + variables[i] + amp
            else:
                s = s + tokens[i] + variables[i] + amp
            first = False
            continue
        a = tokens[i]
        if a[0] == "-":
            a = a[1:]
            s = s + minus + amp
        else:
            s = s + plus + amp
        if a == "1":
            s = s + variables[i] + amp
        else:
            s = s + a + variables[i] + amp
    s = s + equal + amp + tokens[-1]
    if multi:
        s = s + end
    s = s + newline

s = s + r"\end{alignedat}"
print s
