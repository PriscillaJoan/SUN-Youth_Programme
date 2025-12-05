import pandas as pd

def clean_and_validate_sessions(data):
    """Validates participant data and returns cleaned data and error log"""
    
    # read csv file where sample data is saved
    df = pd.read_csv(r"C:\Users\Admin\Documents\Data Science\practice projects\SUN_Youth_Programme\sample_data\sample_data.csv")

    # store original row numbers for error tracking
    df['original_row'] = df.index

    # initialize error tracking
    errors = []

    # ---------DATA CLEANING----------
    # trimming white spaces
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].str.strip()

    # format date
    df['session_date'] = pd.to_datetime(df['session_date'], format='%Y-%m-%d', errors='coerce')

    # standardize gender
    df['gender'] = df['gender'].str.lower()  # Change into lowercase

    gender_map = {
        'M': 'Male',
        'F': 'Female',
        'f': 'Female',
        'm': 'Male',
        'male': 'Male',
        'female': 'Female'
    }

    df['gender'] = df['gender'].map(gender_map)

    # clean phone numbers
    df['phone'] = df['phone'].str.replace(r'[^0-9\+]', '', regex=True)

    # -- VALIDATE INFORMATION

    # validate participant_id (format: SUN followed by 5 digits)
    df['participant_id'] = df['participant_id'].astype(str)
    df['valid_id'] = df['participant_id'].str.match(r'^SUN\d{5}$')
    
    # validate age convert it to numeric and check range 10-35
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    df['valid_age'] = df['age'].between(10, 35)
    
    # validate attendance is not blank
    df['valid_attendance'] = df['attendance'].notna() & (df['attendance'] != '')
    
    # validate phone (format: +2547XXXXXXXX or 07XXXXXXXX)
    df['valid_phone'] = df['phone'].str.match(r'^(?:\+2547\d{8}|07\d{8})$', na=False)
    
    # validate gender mapping worked
    df['valid_gender'] = df['gender'].notna()
    
    # validate session_date parsed correctly
    df['valid_date'] = df['session_date'].notna()
    
    # ----- ERROR LOGS ----
    for idx, row in df.iterrows():
        issues = []
        
        if not row['valid_id']:
            issues.append(f"Invalid participant_id format: {row['participant_id']}")
        
        if not row['valid_age']:
            issues.append(f"Age out of range (10-35) or invalid: {row['age']}")
        
        if not row['valid_attendance']:
            issues.append("Attendance is blank")
        
        if not row['valid_phone']:
            issues.append(f"Invalid phone format: {row['phone']}")
        
        if not row['valid_gender']:
            issues.append(f"Invalid gender value")
        
        if not row['valid_date']:
            issues.append("Invalid session date")
        
        if issues:
            errors.append({
                'row_number': row['original_row'],
                'participant_id': row['participant_id'],
                'name': row['name'],
                'issues': ' | '.join(issues)
            })
    
    # cleaned data with only valid records
    valid_records = (df['valid_id'] & df['valid_age'] & df['valid_attendance'] & 
                     df['valid_phone'] & df['valid_gender'] & df['valid_date'])
    
    cleaned_data = df[valid_records].copy()
    
    # drop validation columns and original_row from cleaned data
    validation_cols = ['valid_id', 'valid_age', 'valid_attendance', 'valid_phone', 
                       'valid_gender', 'valid_date', 'original_row']
    cleaned_data = cleaned_data.drop(columns=validation_cols)
    
    # reset index for cleaned data
    cleaned_data = cleaned_data.reset_index(drop=True)
    
    # error log
    error_log = pd.DataFrame(errors)
    
    return cleaned_data, error_log


if __name__ == "__main__":
    try:
        data =  r"C:\Users\Admin\Documents\Data Science\practice projects\SUN_Youth_Programme\sample_data\sample_data.csv"
        # run validation
        cleaned_data, error_log = clean_and_validate_sessions(data)

        
        # display results
        print("=" * 80)
        print("CLEANED DATA (Valid Records Only)")
        print("=" * 80)
        print(f"\nTotal valid records: {len(cleaned_data)}")
        print(cleaned_data.to_string(index=True))

        print("\n" + "=" * 80)
        print("ERROR LOG (Invalid Records)")
        print("=" * 80)
        print(f"\nTotal errors found: {len(error_log)}")
        if len(error_log) > 0:
            print(error_log.to_string(index=False))
        else:
            print("No errors found!")

        # save to csv files
        cleaned_data.to_csv(r"C:\Users\Admin\Documents\Data Science\practice projects\SUN_Youth_Programme\sample_data\cleaned_data.csv", index=False)
        print(f"\n Cleaned data saved to 'cleaned_data.csv'")
        
        if len(error_log) > 0:
            error_log.to_csv(r"C:\Users\Admin\Documents\Data Science\practice projects\SUN_Youth_Programme\sample_data\error_log.csv", index=False)
            print(f" Error log saved to 'error_log.csv'")
        
        print("\nValidation complete!")
    except FileNotFoundError:
        print("Error: 'sample_data.csv' not found. Please ensure the file exists in the current directory.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")