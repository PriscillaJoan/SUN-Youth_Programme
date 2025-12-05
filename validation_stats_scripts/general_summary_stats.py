import pandas as pd

def generate_summary_stats(cleaned_data):
    
    total_participants = len(cleaned_data)
    unique_participants = cleaned_data['participant_id'].nunique()
    
    # present participants
    present_data = cleaned_data[cleaned_data['attendance'].str.lower() == 'present']
    
    # attendance breakdown by gender
    attendance_by_gender = present_data['gender'].value_counts().to_dict()
    
    summary_stats = {
        'total_participants': total_participants,
        'unique_participants': unique_participants,
        'attendance_by_gender': attendance_by_gender
    }
    
    return summary_stats

cleaned_data =  pd.read_csv(r"C:\Users\Admin\Documents\Data Science\practice projects\SUN_Youth_Programme\sample_data\cleaned_data.csv")
summary = generate_summary_stats(cleaned_data)
print(summary)
