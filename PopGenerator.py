import random
boy_num = 0
girl_num = 0

got_girl = False
for couple in range(100000000):
    got_girl = False
    while got_girl == False:

        if random.random() > .5:
            boy_num += 1

        else:
            girl_num += 1
            got_girl = True


print("{0} : {1}".format(boy_num,girl_num))

print(boy_num / girl_num)
