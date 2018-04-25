input = open("submitInput.txt","r")
out = open("submitOutput.txt","w")
lines = input.readlines()
C = int(lines[0])
C = C+1
for i in range(1,C):
    line = lines[i].split(" ")
    sol = (int(line[0])-1) * (int(line[1])-1)
    out.write("Case #{}: {}\n".format(i,sol))
