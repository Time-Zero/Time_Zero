from ast import Sub
from asyncore import read
from cProfile import label
from dataclasses import dataclass
from enum import Flag
from pickle import TRUE
from re import T
from time import process_time_ns
from traceback import print_tb
from turtle import tilt, width
from xml.dom import WrongDocumentErr
import pandas as pd
import csv
import openpyxl
import matplotlib.pyplot as plt

class Csv_Process:
    def Read_Csv(fPath):
        readed = pd.read_csv(fPath)
        dis = readed["所在地"].value_counts()  # 大学所在地统计
        Overall_Ranking = readed.sort_values(
            by="综合分数", ascending=False)[:10]  # 综合分数排名
        # Subjects = readed.columns[8:]  # 获取各项评分的种类
        # Subject_Ranking = ['']  # 创建一个列表，用来存储不同评分标准的结果，构成一个二维结构
        # for n in Subjects:  # for循环依次选取不同的评分标准
        #     tmp = readed.sort_values(by=n, ascending=False)[:10]  # 不同评分标准取前十
        #     Subject_Ranking.append(tmp)  # 将结果加入列表
        School_Level = readed.sort_values(by="办学层次",ascending=False)[:10]  #办学层次
        Subject_Level = readed.sort_values(by="学科水平",ascending=False)[:10]  #学科水平
        School_Resources = readed.sort_values(by="办学资源",ascending=False)[:10]  # 办学资源
        Teacher_Level = readed.sort_values(by="师资规模与结构",ascending=False)[:10]  #师资水平与结构
        Talent_develop = readed.sort_values(by="人才培养",ascending=False)[:10]  #人才培养
        Scientific_Research = readed.sort_values(by="科学研究",ascending=False)[:10]  #科学研究
        Serving_Community = readed.sort_values(by = "服务社会",ascending=False)[:10]  #服务社会
        Academic_Talent = readed.sort_values(by="学术人才",ascending=False)[:10]
        Significant_Results = readed.sort_values(by="重大项目与成果",ascending=False)[:10]
        International_Competitiveness = readed.sort_values(by="国际竞争力",ascending=False)[:10]
        Ranking_Change = readed.sort_values(by="排名变化", ascending=False)[:10]
        Ranking_Change.dropna(axis="index", how="all",
                              inplace=True, subset=["排名变化"])
        Ranking_Up10 = Ranking_Change[:10]  # 排名前进前10
        Ranking_Down10 = Ranking_Change[-10:]  # 排名倒退前10
        Type_University = readed["高校类型"].value_counts()  #高校类型统计
        
        with pd.ExcelWriter("D:\\PROJECT\\PYTHON_PROJECT\\works\\result.xlsx") as writer:
          dis.to_excel(writer,sheet_name="大学所在地统计",index=True)
          Overall_Ranking.to_excel(writer,sheet_name="综合分数排名",index=TRUE)
          School_Level.to_excel(writer,sheet_name="办学层次",index=True)
          Subject_Level.to_excel(writer,sheet_name="学科水平",index=True)
          School_Resources.to_excel(writer,sheet_name="办学资源",index=True)
          Teacher_Level.to_excel(writer,sheet_name="师资规模与结构",index=True)
          Talent_develop.to_excel(writer,sheet_name="人才培养",index=True)
          Scientific_Research.to_excel(writer,sheet_name="科学研究",index=True)
          Serving_Community.to_excel(writer,sheet_name="服务社会",index=True)
          Academic_Talent.to_excel(writer,sheet_name="学术人才",index=True)
          Significant_Results.to_excel(writer,sheet_name="重大项目与成果",index=True)
          International_Competitiveness.to_excel(writer,sheet_name="国际竞争力",index=True)
          Ranking_Up10.to_excel(writer,sheet_name="排名上升前10",index=True)
          Ranking_Down10.to_excel(writer,sheet_name="排名下降前10",index=True)
          Type_University.to_excel(writer,sheet_name="高校类型",index=True)
        
        plt.figure(figsize=(16,7))
        p1 = plt.bar(dis.index,dis.values)
        plt.bar_label(p1,label_type='edge') 
        plt.title("大学所在地统计")

        plt.figure()
        p2 = plt.bar(Type_University.index,Type_University.values)
        plt.bar_label(p2,label_type='edge')
        plt.title("大学类型统计")
        plt.show()

Csv_Process.Read_Csv("D:\\PROJECT\\PYTHON_PROJECT\\works\\1.csv")
