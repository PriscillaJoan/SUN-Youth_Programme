SELECT *
FROM 
    {{ source('staging', 'participants_info') }}
WHERE 
    AGE <= 20