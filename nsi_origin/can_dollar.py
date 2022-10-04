dollar = 1.65
euros = 1
n = 1

for loop in range(8):
    print(str(n) + ". " + str(euros) + " euros = " + str(dollar * euros) + " $CAN")
    n += 1
    euros *= 2