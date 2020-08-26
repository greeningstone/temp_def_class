# -*- coding: utf-8 -*-
from arithmentic import plus as pl
from arithmentic import subtract as sub
from dataPreprocessing import processing
from dataPreprocessing import importData

a = 3
b = 4

def main():
  print("~~ 사칙 연산을 시작합니다 ~~ ")
  print("a + b =", sub.minus(a, b))
  print("a - b =", pl.add(a, b))
  print("~~ 사칙 연산을 종료합니다 ~~ ")

  ## 데이터 전처리 시작
  data = importData.readData()
  processing.process_data(data)

if __name__ == "__main__":
  main()