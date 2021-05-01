# define class
class Seito():
    # init
    def __init__(self, name, japanese, math, science, society):
        self.name = name
        self.japanese = japanese
        self.math = math
        self.science = science
        self.society = society
    # print self
    def show(self):
        print(self.name, self.japanese, self.math, self.science, self.society)
        return
    # calc & show average
    def showave(self):
        ave=(self.japanese + self.math + self.science + self.society) / 4.0
        print(self.name, "ave =", ave)
        return
# print name & grade each subject
def check(seito: Seito):
    grades = seito.name+" : "
    for item in list(seito.__dict__.items())[1:]:
        grades+=item[0]+"="+("pass" if int(item[1]) > 60 else "failure")+", "
    print(grades[:-2])
    return

if __name__ == "__main__":
    # make instance
    seito1 = Seito("yamada",34,56,87,45)
    seito1.show()
    check(seito1)
    seito2 = Seito("sato",90,86,77,45)
    seito2.show()
    check(seito2)