import pandas as pd 
import os

def attendance_here(character,today,current_time):
    n=os.listdir("C:/Users/ANIRBAN MISRA/Downloads/originalimages_part1/ourdata")
    file_path="C:/Users/ANIRBAN MISRA/Downloads/originalimages_part1/attendance.csv"
    df=pd.read_csv(file_path)

    today1=str(today)
    current_time1=str(current_time)
    character1=str(character)
    m=[]
    for i in range(len(n)):
        arr=df[n[i]].tolist()
        if len(arr)!=0:
            m.append(arr)
        else:
            m.append(["b"])
    attendance=today1+"at"+current_time1
    position=n.index(character1)
    if (m[position][len(m[position])-1].find ("b")!=-1):
        m[position][len(m[position])-1]=attendance
    elif  (m[position][len(m[position])-1].find (today1)!=-1):
        print("haramkhor")
    else:
        m[position].append(attendance)
        for i in range(len(m)-1):
            m[i].append("b")

    resdict={n[i]:m[i]for i in range(0,len(n))}
    df = (pd.DataFrame(resdict))
    df.to_csv(file_path)