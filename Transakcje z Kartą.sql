USE DJ000
GO

SELECT 
	su.Nazwa
	,COUNT (sd.SklepId) as LiczbaTransakcji
FROM dbo.SklepDok as sd
JOIN dbo.SKLEPY_UNIKAT as su on sd.SklepId = su.SklepId
WHERE 
	sd.NrDok LIKE 'DF/PAR%'
	AND sd.SklepPlatnikId IS NOT NULL 
	AND sd.Data >= DATEADD(DAY,DATEDIFF(DAY,1,GETDATE()),0)
	AND sd.Data < DATEADD(DAY,DATEDIFF(DAY,0,GETDATE()),0)
GROUP BY sd.SklepId, su.Nazwa
ORDER BY su.Nazwa