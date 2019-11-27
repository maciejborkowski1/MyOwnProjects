USE DJ000
GO

SELECT DISTINCT
	k.Nazwa
	,s.SklepId
	,s.NrSklepu
FROM dbo.SklepDok as d
JOIN dbo.SklepKontr as k on d.SklepId = k.KontrId
JOIN dbo.Sklep as s on d.SklepId = s.SklepId
WHERE
	k.Nazwa LIKE 'DJ%' OR k.Nazwa LIKE 'DZ%'
	AND
	k.Nazwa NOT LIKE '%(zam)'
ORDER BY
	k.Nazwa