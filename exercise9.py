x = "{1:{0}}".format(3, 4)
print("a)",x)
#b) x = "{0:$>5}".format(3)
x = "{0:$>5}".format(3)
print("b)",x)
#c) x = "{a:{b}}".format(a = 1, b = 5)
x = "{a:{b}}".format(a = 1, b = 5)
print("c)",x)
#d) x = "{a:{b}}:{0:$>5}".format (3, 4, a = 1, b = 5, c = 10)
x = "{a:{b}}:{0:$>5}".format (3, 4, a = 1, b = 5, c = 10)
print("d)",x)
