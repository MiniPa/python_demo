a = 2  # type:int
print(4/a, type(4/a))

b = 3.5  # type:float
b1 = 3.5e2  # type:float
b2 = 3.5e-2  # type:float
print(b, b1, b2)

c = 4 + 7j  # type:complex
print(c * c)

d = True  # type:bool
print(d + 2.7)

myName = "TOM"
yourName = 'JACK'
print(myName+yourName)
print(yourName[0:2])

Lilyx = "Lily"
herName = Lilyx
print("her name is: ", herName)

myName = "TOM"
myname = "DADA"
myname = "SAM"
print(myName, myname)

aNumber = 5e-1
aString = " likes "

addExample = 3 + 7.9 + aNumber + 7j + True  # This is OK
jointExample = "Tom" + aString + "Lily"  # Also OK

a = 5
b = 3.2
c = 1
multiplyExam = a*(b+c)  # Correct

print("5.7/2.3 =", 5.7/2.3)
print("5.7//2.3 =", 5.7//2.3)
print("2**3 =", 2**3)
print("9%4 =", 9%4)

x = 5
y = 4
print(x == y)
print(x != y)
print(x > y)
print(x >= y)
print(x < y)
print(x <= y)
print("---")
print(True and True)
print(True and False)
print(True or False)
print(False or False)
print("------")
print(3 and 0, bool(3 and 0))
print(-0.7 and 1.3, bool(-0.7 and 1.3))
print(3 or 0, bool(3 or 0))
print(-0.7 or 0, bool(-0.7 or 0))
print("------")
print(3 > 1 and 9 > 1)
print(1.7 == 8 or 7 > 13)
print(bool(0.000))

import time
time.sleep(0.1)

a = 2  # type:int
myName = "TOM"
# notAutoCastExam = a + myName # WRONG
manualCastExam = str(a) + myName  # CORRECT
print(manualCastExam)

print(int(3.2))
print(float(3))
print(complex(3))
print(bool(3))
print(str(bool(3))+"OK")

print('My dad asked: "How about going out for dinner?"')
print("My mom answered:\"Let's go!\"")

testText = "abcdefg"
print(testText[0:3])
print(testText[1:2])
print(testText[2:5])
print(testText[1:90])

testText = "abcdefg"
testList = testText.split('d')
print(testList)

print(testList[0])
print(testList[1])

print(testList[0][0])
print(testList[0][1])
print(testList[0][1:3])

testList2 = ["Hello", "world!", 12345, True]
print(testList2[3])
print(testList2[2:4])

testList3 = []
print(testList3)
testList3.append("ok")
testList3.append(54321)
testList3.append("ok2")
testList3.append(False)

print(testList3)
testList4 = testList3[1:4]

print("---------")

print("testList3:\n", testList3, end="\n---------\n")
testList3.insert(2, "aNewString")

print("testList3(position2 inserted):\n",
      testList3, end="\n---------\n")

testList3.insert(20, "aNewString")
print("testList3(position200(index out of bound) inserted):\n",testList3)

# testList3.remove(testList3[1])
# print(testList3)
# testList3.reverse()
# print(testList3)

textA = "Hello,"
textB = "World!"
print(textA)  # 仅可改动此行
print(textB)

aList=[1,7,3,2,6]
aList.sort()
print(aList)

myInput = input("please input your information:")
# Lily 13 girl reading
# Tom 13 boy programming
myTmp = myInput.split(' ')
if len(myTmp) == 4:
    print("Hello,", myTmp[0] + '.', "Your are a", myTmp[1] + "-year-old", myTmp[2] + ", you enjoy",
          myTmp[3] + ' very much.')