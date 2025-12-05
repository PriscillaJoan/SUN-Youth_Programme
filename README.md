# SUN Youth Programme Data Validation & Analysis

## Overview

This project focuses on validating, cleaning, and analyzing participant session data for the SUN Youth Programme. It ensures that participant information is accurate, 
attendance is tracked correctly, and summary statistics are generated for reporting and program planning.

The scripts included can:

- Clean and validate raw participant data.
- Generate error logs for invalid records.
- Produce summary statistics such as total participants, unique participants, and attendance breakdown by gender.

---

## Folder Structure

SUN_Youth_Programme/
- sample_data/
  - `sample_data.csv` — sample data created in the data_validation.ipynb notebook
  - `error_log.csv` — contains records with validation errors
  - `cleaned_data.csv` — contains data after validation and cleaning
- validation_stats_scripts/
  - `clean_and_validate_sessions.py` — script for cleaning and validating data
  - `general_summary_statistics.py` — script for generating summary statistics
- `README.md` — project documentation

---

## Requirements

- Python 3.8+
- pandas

Install pandas with:

```bash
pip install pandas

Install pandas with:
pip install pandas

## Usage

### 1. Navigate to the folder containing the scripts:
cd validation_stats_scripts

### 2. Run the validation script:
python clean_and_validate_sessions.py

This will:
- Read the raw sample_data.csv
- Validate and clean the data
- Save cleaned_data.csv with valid records only
- Save error_log.csv which records any issues

### 3. Run the summary statistics script:
python general_summary_statistics.py

This will:
- Generate summary statistics including total participants, unique participants, and attendance breakdown by gender
- Display results in the console

## Notes

- Ensure the sample_data.csv file is located in the sample_data/ folder
- Make sure your Python environment has pandas installed
- Scripts are modular: functions from clean_and_validate_sessions.py can be imported for further analysis
```

## Additional Considerations

While the current scripts handle data validation, cleaning, and summary statistics, there are several additional aspects that could enhance the system:

1. **Reason for Absence**
   - Add a column to capture why a participant was absent (e.g., illness, travel, personal reasons).
   - Purpose: Helps track attendance patterns and identify participants who may need extra support.

2. **Level of Education**
   - Include the participants’ education level.
   - Purpose: Enables tailoring training sessions according to the participants’ knowledge and skill levels, ensuring sessions are relevant and effective.

3. **Age Ranges**
   - Group participants by age brackets (e.g., 10–15, 16–20, 21–28, 28-35.).
   - Purpose: Ensures training content is suitable for the participants’ capacities and developmental needs.

4. **Next of Kin / Emergency Contact Information**
   - Collect additional data such as name, age, address, and occupation of a participant’s next of kin.
   - Purpose: Provides background context on participants and a reliable contact in case of emergencies or difficulty reaching the participant.

### Assumptions
- Participants provide accurate personal information.
- Reasons for absence are optional but recommended for better program insights.
- Age and education levels guide content planning for training sessions.


