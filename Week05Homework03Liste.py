letters="abcdefghij"
numberList= [i for i in range(1,11)]
letterList = [k for k in letters]

numberLetter= [(str(satir)+sutun+",") for satir in numberList for sutun in letterList]
letterNumber= [(satir+str(sutun)+",") for satir in letterList for sutun in numberList]
print("1.Liste ",numberLetter)
print("2.Liste ",letterNumber)