{{ config(
    schema=generate_schema_name('l3_CONSUMPTION', this),
    materialized='table'
) }}
SELECT
    pi.name,
    pi.phone,
    pi.education_level,
    pi.gender,
    pa.pre_assessment_score,
    pa.post_assessment_score,
    pa.percentage_improvement,
    pa.post_confidence_level
    
FROM
    {{ source('staging', 'participants_info') }} AS pi
JOIN
    {{ source('staging', 'participants_post_assessment') }} AS pa
ON
    pa.participant_id = pi.participant_id
