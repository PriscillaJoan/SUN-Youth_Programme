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

## Minor Improvments

I used project leverages **dbt (data build tool)** in combination with **Snowflake** to build a structured and reproducible data pipeline for the SUN Youth Programme. All the folders are in the ***MINOR IMPROVEMENTS**


I used dbt and snowflake to demonstrate best practices in working with databases, ensuring **reproducibility**, **clarity**, and **modular design**.

## Data Sources and Seeds

- **Seeds:**  
  - `participants_performance_metric` – contains pre- and post-assessment scores and pre confidence levels for participants.  
  - `next_of_kin` – contains next-of-kin information for minor participants.  

These seeds were used to create new staging tables and views for further analysis.

## Staging Layer (L2 Processing)

- **Minors:** Identifies participants under the age of 20 from the participants’ information.  
- **Participants Post Assessment:** Calculates improvement metrics, including percentage improvement and post-assessment confidence levels from the parrticipants performancee metric.  

These staging models prepare and clean the raw data, ensuring that downstream models have structured, reliable inputs.

## Marts Layer (L3 Consumption)

- **Minor Participants:** Combines data from the staging layer to produce a table containing all minor participants and their next-of-kin information.  
- **Participants Performance:** Integrates participant information with their assessment metrics, providing a complete view of participant performance.

This layer creates final tables ready for analytics, reporting, or visualization.

## Macros

- A macro (`generate_schema_name`) was added to dynamically control schema names for models. This ensures that models are created in the correct schema while maintaining flexibility and consistency across different environments.

## Key Points

- **Reproducibility:** Using dbt ensures that models can be recreated consistently, with all dependencies tracked automatically via `ref()` and `source()`.  
- **Modularity:** Staging models clean and transform raw data; marts aggregate and combine data for analytics.  
- **Documentation:** Sources, models, and seeds are documented to provide clarity on their purpose and lineage.

## Data Quality and Testing

To ensure data integrity and maintain high-quality outputs, the following **dbt tests** have been implemented:

1. **Minor nok data check**
   - This test checks that all minor participants have **next-of-kin (NOK) name and phone number** recorded.  
   - Any minor participant missing NOK information will fail this test, ensuring that all critical contact details are captured for reporting and follow-up.

2. **Participants score check**  
   - This test ensures that all participants have a **post-assessment score of 50 or higher**.  
   - Any participant with a score below 50 will fail the test,this is to ensure that we are following up on the performance of our partcipants.

These tests are run using dbt’s testing framework, combining **built-in column-level tests** and **custom SQL tests**. They provide automated data validation, helping to detect and prevent inconsistencies or missing critical information in the pipeline.

**Running the tests:**  

## Running the Project

1. Load seeds:  
   ```bash
   dbt seed

   - Collect additional data such as name, age, address, and occupation of a participant’s next of kin.
   - Purpose: Provides background context on participants and a reliable contact in case of emergencies or difficulty reaching the participant.

### Assumptions
- Participants provide accurate personal information.
- Reasons for absence are optional but recommended for better program insights.
- Age and education levels guide content planning for training sessions.


