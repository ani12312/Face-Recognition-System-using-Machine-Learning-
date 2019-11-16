import pandas as pd 
import os

def attendance_here(character,today,current_time, att_type="entry"):
    file_path="attendance.csv"
    df=pd.read_csv(file_path)
    
    entry = pd.DataFrame([[character,today,current_time, att_type]], columns=["emp_id","date","time","att_type"])

    df = df.append(entry) 
    df.to_csv(file_path, index = False)

