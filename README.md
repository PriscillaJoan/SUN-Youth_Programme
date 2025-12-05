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

- Ensure the sample_data.csv file is located in the sample_data folder
- Make sure your Python environment has pandas installed
- Scripts are modular: functions from clean_and_validate_sessions.py can be imported for further analysis
```
## Design Decision
- Row-level validation: Each record is validated individually to capture all errors
- Clean and error data stored separately to enable data quality monitoring
  
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
   - Important for handling minors safely.
    
5. **Performance metrics**
   - Track participants’ performance throughout the training.


# Data Collection Requirements

To support the above, additional data needs to be collected:

- Next of Kin (NOK) CSV:
  - Fields: participant_id, NOK name, NOK phone
  - Purpose: Links minors to their emergency contacts.

- Additional  Participant Information:
  - Fields: Level of education, village, occupation
  - Purpose:Tracking participant distribution geographically and to help tailor training content based on education level

- Participant Performance CSV:
  - Fields: participant_id, pre-assessment score, post-assessment score, trainer’s initial confidence level
  - Purpose: Monitors participant progress and effectiveness of training sessions.
 
 
 # NEXT STEPS
In the next step, a demonstration will show how all this information can be used to enhance analysis and decision-making.

## Minor Improvments
After creating the Python validation scripts, I realized I had several limitations:

- Data was in CSV files, which made it hard to query and join for more complex analysis.  
- Running the scripts manually meant it was hard to reproduce the exact same results every time.  
- It was difficult to track participants across multiple dimensions.  
- Additional data relationships were limited, and I had to manually check data quality.

To solve these issues, the project now uses **dbt (Data Build Tool)** together with **Snowflake**:

- **dbt** helps create a structured and reproducible pipeline. It automatically tracks dependencies between tables, runs transformations in the right order, and makes it easy to test data quality.  
- **Snowflake** stores all the data in one central place, so everyone can query the same source of truth without relying on CSV files.
  
Even though Python scripts are still useful for cleaning and processing, dbt + Snowflake makes the whole system more reliable, easier to reproduce, and ready for more advanced analysis.  

All additional files used for this improved workflow are in the **MINOR IMPROVEMENTS** folder.



## Data Sources and Seeds
```SUN_YOUTH_PROGRAMME/
├── Minor_Improvements/
│   └── logs/
├── new_data/
│   ├── next_of_kin.csv
│   ├── participants_info.csv
│   └── participants_performance_metric.csv
└── Sun_youth_dbt/
    ├── analyses/
    ├── logs/
    ├── macros/
    │   ├── .gitkeep
    │   └── generate_schema_name.sql
    ├── models/
    │   ├── marts/
    │   │   ├── minor_participants.sql
    │   │   └── participants_performance.sql
    │   └── staging/
    │       ├── minors.sql
    │       ├── participants_post_assessment.sql
    │       └── sources.yml
    ├── seeds/
    │   ├── .gitkeep
    │   ├── next_of_kin.csv
    │   └── participants_performance_metric.csv
    ├── snapshots/
    └── tests/
        ├── .gitkeep
        ├── minor_nok_data_check.sql
        └── participants_score_check.sql
```
        
## Data Pipeline Architecture

- **Seeds:(Raw Data)**
  
They are CSV files containing foundational data loaded directly into the database.

  - `participants_performance_metric` :  contains pre- and post-assessment scores and pre confidence levels for participants.  Used to track participant progress throughout the programme
    
  - `next_of_kin` : Contains emergency contact information for minor participants (under 20 years old) which is the next-of-kin name and phone number which is critical for safeguarding and emergency communication
  

## Staging Layer (L2 Processing)

These staging models prepare and clean the raw data, ensuring that downstream models have structured, reliable inputs.

- `minors.sql`:  Identifies participants under the age of 20 from the participants’ information to provide a clean dataset of minor participants for safeguarding and reporting purposes
- `participants_post_assessment.sql`: Computes percentage improvement between pre- and post-assessments including percentage improvement and post-assessment and derives post-assessment confidence levels 



## Marts Layer (L3 Consumption)
This layer creates final tables ready for analytics, reporting, or visualization.

- `minor_participants.sql` Combines minor participant data with their next-of-kin information,providing a complete view of all minor participants and their emergency contacts
  
- `participants_performance.sql`: Integrates participant information with their assessment metrics, providing a complete view of participant performance.


## Macros

- A macro (`generate_schema_name`) was added to dynamically control schema names for models. This ensures that models are created in the correct schema while maintaining flexibility and consistency across different environments.

## Data Quality and Testing
Automated tests to ensure data integrity and catch issues before they impact reporting.

1. `minor_nok_data_check.sql`
   - This test checks that all minor participants have complete next-of-kin information recorded.
   - Any minor participant missing NOK information will fail this test,  ensuring compliance with safeguarding requirements.

2. `participants_score_check.sql`
   - Ensures participants meet minimum performance standards. All participants must achieve a post-assessment score of 50 or higher
   - This helps to identify participants requiring additional support or follow-up intervention.

### Key Features & Benefits

**Reproducibility**
- All transformations are version-controlled and automated through dbt
- Dependencies are tracked automatically using ref() and source() functions
- Anyone can recreate the entire pipeline with a single command

**Modularity**
- Staging models handle data cleaning and transformation
- Marts aggregate and combine data for specific analytical purposes
- Changes to one layer don't break downstream dependencies
- 
**Data Quality**
- Automated testing prevents bad data from reaching reports
- 
 ### Assumptions
- Participants provide accurate personal information.
- Reasons for absence are optional but recommended for better program insights.
- Age and education levels guide content planning for training sessions.

# How to Run This Project
1. **Clone the repository**
   ```bash
   git clone <https://github.com/PriscillaJoan/SUN-Youth_Programme>
   cd SUN_YOUTH_PROGRAMME
   
**Running the tests:**  
1. Create & Activate a virtual enviroment
```
python -m venv env
source env/bin/activate       # Mac/Linux
env\Scripts\activate          # Windows
```
2. Install dependancies
  ```
  pip install pandas
  pin install dbt
  pip install dbt_snowflake
```
3. Initiate DBT
```
 dbt init
 dbt debug
```
4. Load seeds:
   - Load CSV data into the database:
   ```
   dbt seed
   
5. Run Models
- Execute all transformations (staging and marts):
```bash
 dbt run
```

6. Run Tests
- Validate additional data quality
```
dbt test
```
7. Generate Documentation
- Create and view project documentation
```bash
dbt docs generate
dbt docs serve
```
