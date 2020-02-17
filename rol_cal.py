from tkinter import*
######################################################
######################################################
##############롤갭 감소량 계산식 및 위치################
######################################################
######################################################
def BJ1():
    try:
        ###### 이름 정의 ######
        ns00, ns01 = a00.get(), a01.get()
        ns02, ns03 = a02.get(), a03.get()
        Density = ns00
        Elasticity = ns01
        Diameter = ns02
        RPM = ns03  
        ###### 공식 ######
        X = ((Density * ((Diameter/2) ** 2))/Elasticity) * (9.8 + ((Diameter/2) * ((3.141592/30) ** 2) * (RPM ** 2)))
        Y = Diameter * (3.141592/60) * RPM
        ###### 결과 표현  ######
        a = "롤 갭 감소량 = " + "{:10.1f}".format(X)
        b = "소재 속도 = " + "{:10.1f}".format(Y)
    except ZeroDivisionError:
        a =  "Zero Div Error"
        print("Zero Division Error")
        b =  "Zero Div Error"
        print("Zero Division Error")       
    except ValueError:
        a =  "Value Error"
        print("Value Error")
        b =  "Value Error"
        print("Value Error")
    ns1.config(text = a)
    ns1.grid(row = 6, column = 1, sticky = W)
    ns2.config(text = b)
    ns2.grid(row = 7, column = 1, sticky = W)
######################################################
######################################################
################## 엔터 버튼 라벨 #####################
######################################################
######################################################
def ent(var, row, col, width = None):
    # 2nd Function
    w = Entry(root, textvariable = var, width = 22)
    w.grid(row = row, column = col)
    return w

def btn(txt, row, col, cmd = None):
    # 5th Function
    w = Button(root, text = txt, command = cmd)
    w.grid(row = row, column = col)
    return w

def lab(txt, row, col):
    # 6th Function
    w = Label(root, text = txt)
    w.grid(row = row, column = col)
    return w
######################################################
######################################################
##################### 시트 생성 #######################
######################################################
######################################################
root = Tk()             
root.geometry('600x400')
root.resizable(True, True)

'''     0,0     0,1     0,2
        1,0     1,1     1,2
        2,0     2,1     2,2
        3,0     3,1     3,2
        4,0     4,1     4,2
'''
######################################################
######################################################
##################### 이름 정의 #######################
######################################################
######################################################
a00, a01 = DoubleVar(), DoubleVar()
a02, a03 = DoubleVar(), DoubleVar()

v1, k1, r1, t1, e1, f1 = "롤 밀도:", "롤 탄성계수:", "롤 직경:", "롤 RPM:", "실행", ""
s0, s1, s2, s3, s4, s5 = "kg/m^3", "GPa", "m", "-", "[micrometer]", "[m/s]"

lab(v1, 1,0)    ; ent(a00, 1,1) ; lab(s0, 1,2)
lab(k1, 2,0)    ; ent(a01, 2,1) ; lab(s1, 2,2)
lab(r1, 3,0)    ; ent(a02, 3,1) ; lab(s2, 3,2)
lab(t1, 4,0)    ; ent(a03, 4,1) ; lab(s3, 4,2)
btn(e1, 5,0, BJ1); Label(root)  ; lab(s4, 6,2)
lab(f1, 6,0)    ; Label(root)   ; lab(s5, 7,2)

ns1 = Label(root)
ns2 = Label(root)

root.title("롤 갭 감소량 계산(NTM & RSM)")
root.mainloop()