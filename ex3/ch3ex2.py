# define class
class seito():
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

# make instance
seito1 = seito("yamada",34,56,87,45)
seito1.show()
seito1.showave()
seito2 = seito("sato",90,86,77,45)
seito2.show()
seito2.showave()