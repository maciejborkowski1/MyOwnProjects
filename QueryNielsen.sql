USE DJ050
GO

SELECT
	'DJ050' as 'SHOPCODE'
	,t.Kod as 'BARCODE'
	,t.Skrot as 'PLU'
	,t.Nazwa as 'BARNAME'
	,CASE 
		WHEN t.Producent IS NULL THEN 'BRAK'
		ELSE knt.Nazwa
	END as 'MANUFACTER'
	,CASE
		WHEN knt.KontrId = 19 THEN 1
		ELSE 0
	END as 'PRIVATE_LA'
	,j.Nazwa as 'UNIT_OF_MEASURE'
	,CAST ((p.IloscPlus - p.IloscMinus) AS DECIMAL(10,2)) as 'SALESITEM'
	,CAST ((p.Wartosc + (p.Wartosc*((p.Stawka / 100) /100 ))) AS DECIMAL (10,2)) as 'SALES_VALU'
	,CAST (t.CenaDet AS DECIMAL(10,2)) as 'REGULAR_PRICE'
	,k.CentrKatId as 'GRPProd_ID'
	,k.Nazwa as 'GRPProd'
	,a.CentrAsId as 'GRPProd2_ID'
	,a.Nazwa as 'GRPProd2'
	,CAST (d.Data AS DATE) as 'DATE'
	,d.Zmiana as 'TIME'
	,'DJ050' + d.NrDok as 'TLOG'	
	,d.Razem as 'TRANS_TOT'
FROM dbo.PozDok as p
JOIN dbo.Dok as d on d.DokId = p.DokId
JOIN dbo.Towar as t on t.TowId = p.TowId
JOIN dbo.JM as j on j.JMId = t.JMId
JOIN dbo.Kategoria as k on t.KatId = k.KatId
JOIN dbo.Asort as a on t.AsId = a.AsId
LEFT JOIN dbo.Kontrahent as knt on knt.KontrId = t.Producent
WHERE 
	p.IloscPlus > 0 
	AND
	(d.NrDok LIKE 'DF/PAR%' OR d.NrDok LIKE 'FV/%')
	AND
	d.Data = CAST (GETDATE() as DATE)
ORDER BY
	SHOPCODE, BARCODE, DATE, TLOG