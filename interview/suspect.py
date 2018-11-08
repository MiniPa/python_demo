# 1.   日本某地发生了一件谋杀案，警察通过排查确定杀人凶手必为4个嫌疑犯的一个。以下为4个嫌疑犯的供词。
# A说：不是我。
# B说：是C。
# C说：是D。
# D说：C在胡说。
# 已知3个人说了真话，1个人说的是假话。
# 现在请根据这些信息，写一个程序来确定到底谁是凶手。



i = sum = flag = 0
killer = ''

count = 1
while(count <= 4):
    killer = 64 + count
    print(chr(killer))
    sum = (chr(killer) != 'A') + (chr(killer) == 'C') + (chr(killer) == 'D') + (chr(killer) != 'D')
    if sum == 3:
        flag = 1
        print("%s is the killer.\n" % (chr(killer)))
        break
    count += 1
if flag == 0:
    print("can't find\n")






