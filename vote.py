def cjp ():
    global c
    c+=1
    return
def tvk ():
    global t
    t+=1
    return
def ntk ():
    global n
    n+=1
    return
def dmk ():
    global d
    d+=1
    return
def congress ():
    global cong
    cong+=1
    return
def bjp ():
    global b
    b+=1
    return
def NOTA ():
    global nt
    nt+=1
    return

c=0
t=0
n=0
d=0
cong=0
b=0
nt=0


i = int (input("=== SELECT STATE === \n 1 . TN ELECTION \n 2 . OTHER STATE \n "))
if i ==1:
    while True:
        vote = int(input("==== WELCOME TO TN ELECTION ==== \n poll your vote \n 1 . cjp \n 2 . tvk \n 3 . ntk \n 4 . dmk \n 5 . congress \n 6 . bjp \n 7 . NOTA\n 8 . result \n8" ))
        if vote==1:
            cjp()
            print ("your vote polled successfully ")

        elif vote==2:
            tvk()
            print ("your vote polled successfully ")

        elif vote==3:
            ntk()
            print ("your vote polled successfully ")

        elif vote==4:
            dmk()
            print ("your vote polled successfully ")

        elif vote==5:
            congress()
            print ("your vote polled successfully ")

        elif vote==6:
            bjp()
            print ("your vote polled successfully")

        elif vote==7:
            NOTA ()
            print ("your vote polled successfully ")
        else:
            print(f"=== RESULT === \ntotal count of \ncjp : {c} \ntvk : {t} \nntk : {n} \ndmk : {d} \ncong : {cong} \n bjp : {b} \n NOTA : {nt}")
            break
else:
    print ("NOT ELIGIBLE")
