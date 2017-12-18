#!/usr/bin/env python3
import sys
try:
    filename='/home/shiyanlou/test.csv'
    with open(filename) as file:
        d={}
        for i in file.readlines():
            e=i.strip().split('=')
            key,value=e[0],e[1]
            d[key]=value
        print(d)


    for arg in sys.argv[1:]:
        b=arg.split(':')
        Salary=int(b[1])
    if Salary<JiShuH:
        Fiof=Salary*(YangLao+YiLiao+ShiYe+GongShang+ShengYu+GongJiJin)
        Rest=(Salary-3500-Fiof)
        if Salary<2193:
            
        if Rest<0:
            Tax=0
        if 0<Rest<1500:
            Tax=Rest*0.03
        if 1500<=Rest<4500:
            Tax=Rest*0.1-105
        if 4500<=Rest<9000:
            Tax=Rest*0.2-555
        if 9000<=Rest<35000:
            Tax=Rest*0.25-1005
        if 35000<=Rest<55000:
            Tax=Rest*0.3-2755
        if 55000<=Rest<80000:
            Tax=Rest*0.35-5505
        if 80000<=Rest:
            Tax=Rest*0.45-13505
        Income=format((Salary-Fiof-Tax-SocIns),".2f")
        print(b[0]+':'+Income)

    
except:
    print("Parameter Error")
