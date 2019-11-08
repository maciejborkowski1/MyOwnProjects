USE DJ050
GO

SELECT *
FROM dbo.Towar
WHERE Kod = '7702018072187'
GO

SELECT *
FROM dbo.PozDok as p
JOIN dbo.Dok as d on d.DokId = p.DokId
JOIN dbo.Towar as t on t.TowId = p.TowId
JOIN dbo.JM as j on j.JMId = t.JMId
JOIN dbo.Kategoria as k on t.KatId = k.KatId
JOIN dbo.Asort as a on t.AsId = a.AsId
JOIN dbo.Kontrahent as knt on knt.KontrId = t.Producent
WHERE --knt.Dostawca = '1' AND 
d.NrDok LIKE 'FV/%'
GO

SELECT *
FROM dbo.Dok
WHERE DokId = '11102'
GO

SELECT *
FROM dbo.Kontrahent as knt
WHERE knt.Dostawca = '1'
GO