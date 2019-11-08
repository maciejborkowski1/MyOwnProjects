USE DJ050
GO

SELECT
	SUM (CAST ((p.Wartosc + (p.Wartosc*((p.Stawka / 100) /100 ))) AS DECIMAL (10,2))) as 'TOTAL_SALES'
	,CAST (d.Data as DATE) as 'DATE'
FROM dbo.PozDok as p
JOIN dbo.Dok as d on d.DokId = p.DokId
WHERE 
	(p.IloscPlus - p.IloscMinus) > 0 AND
	d.NrDok LIKE 'DF/PAR%' AND 
	d.Data BETWEEN '2019-04-16' AND '2019-04-22'
GROUP BY d.Data