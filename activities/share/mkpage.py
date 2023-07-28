input = open('docs')
lines = input.readlines()
input.close()

lines.reverse()

for line in lines:
    line = line.rstrip()
    index = line.find(' ')
    doc = line[:index]
    name = line[index+1:]

    print r'<li><a href="' + doc + r'" target=_blank> ' + name + r'<a></li>'
