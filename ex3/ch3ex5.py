from scipy import integrate

result, err = integrate.quad(lambda x: 4.0 / (1 + x*x), 0, 1)
print("result = ", result)
print("err = ", err)