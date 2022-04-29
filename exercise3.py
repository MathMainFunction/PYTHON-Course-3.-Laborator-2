paragraph = "«Ми обов'язково навчимося програмувати»"
#3_1: [!]3 символ - это пробел
print("3.1:", paragraph[3])

#3_2:
print("3.2:", paragraph[-2])

#3_3:
print("3.3:", paragraph[0:5])

#3_4:
print("3.4:", paragraph[:-2])

#3_5:
print("3.5:", paragraph[::2])

#3_6:
print("3.6:", paragraph[1::2])

#3_7:
print("3.7:", paragraph[::3])

#3_8:
print("3.8:", paragraph[::-1])

#3_9:
print("3.9:", paragraph[::-2])

#3_10:
print("3.10:", len(paragraph))

#3_11:
print("3.11:", paragraph[int(len(paragraph)/2)-2:int(len(paragraph)/2)+2])

#3_12:
t = paragraph.replace('програмувати', '')
print("3.12:", t)

#3_13
x="програмувати"
print ("3.13:", paragraph.replace(x, 'ніколи не'))

#3_14
print ("3.14:", paragraph + 'на Python')

#3_15
print("3.15:", paragraph.split()[-1])








