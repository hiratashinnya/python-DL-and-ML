from ex2_2 import score2grade as s2g

with open("./mathscore.txt", "r") as f:
    lines=f.readlines()

with open("./mathgrade.txt","w") as f:
    for l in lines:
        f.write(l.replace("\n", " "+s2g(int(l.split(" ")[1]))+"\n"))
