-- flag any minor who doesnt have their nok contact information
-- Flag minor participants missing next-of-kin information
SELECT *
FROM {{ ref('minor_participants') }}
WHERE nok_name IS NULL
   OR nok_phone IS NULL

