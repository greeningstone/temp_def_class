# -*- coding: uft-8 -*-

import calculation
a = 3
b = 4

def main():
    print("안녕하세요, main() 입니다.")
    print("a+b=",calculation.subtract(a,b))
    print("a=b=", calculation.plus(a,b))

def plus(a,b):
    c=a+b
    return  c

def subtranct(a,b):
    c=a-b
    return c

