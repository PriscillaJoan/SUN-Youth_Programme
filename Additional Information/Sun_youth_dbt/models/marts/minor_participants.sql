
{{ config(
    schema=generate_schema_name('l3_CONSUMPTION', this),
    materialized='table'
    
) }}SELECT
    n.nok_name,
    n.nok_phone
FROM
    {{ ref('next_of_kin') }} AS n
JOIN
    {{ source('staging', 'minors') }} AS m
ON
    n.participant_id = m.participant_id
