def score2grade(p):
    if p < 70:
        if p < 60:
            return("D")
        else:
            return("C")
    else:
        if p < 90:
            if p < 80:
                return("B")
            else:
                return("A")
        else:
            return("S")
