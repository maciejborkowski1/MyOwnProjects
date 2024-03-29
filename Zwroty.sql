USE DJ000
GO

--SELECT *
--FROM dbo.SklepDok as s
--WHERE s.NrDok = 'ZWPAR/19/21/1'

SELECT DISTINCT
	k.Nazwa
	,d.NrDok
	,CAST (d.Data AS DATE) as 'Data'
	,CASE 
		WHEN d.FormaPlat = 3 THEN 'Karta'
		ELSE 'Gotówka'
	END as 'Zwrot na'
FROM dbo.SklepDok as d
JOIN dbo.SklepKontr as k on d.SklepId = k.KontrId
WHERE 
	d.Data >= DATEADD(DAY,DATEDIFF(DAY,1,GETDATE()),0)
	AND
	d.Data < DATEADD(DAY,DATEDIFF(DAY,0,GETDATE()),0)
	AND
	d.NrDok LIKE 'ZWPAR%'
	AND
	k.Nazwa NOT LIKE 'DJ001NOWE%'
	AND
	k.Nazwa NOT LIKE 'DZ%'
ORDER BY
	k.Nazwa, Data

