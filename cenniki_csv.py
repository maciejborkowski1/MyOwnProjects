import pyodbc
conn = pyodbc.connect('Driver=;'
                      'Server=;'
                      'Database=;'
                      'Trusted_Connection=yes;')


inputPath = 'c:\\temp\\cenniki\\J4.csv'
priceCode = input('Podaj kod cennika:')
input("Podany kod cennika to '%s', kontynuować?" % priceCode)
#i=0

with open(inputPath, 'r', errors='ignore') as inFile:
    for line in inFile:
##        if i == 0:
##            del line
##        else:
        line = line.split(';')
        del line[:2]
        del line[1:]
        line = ''.join(line)
        if line[-3] == '-':
            line = line.split('-')
            partNo = line[0]
            segCode = int(line[1])
            print('Symbol to: %s, wariant to: %s' % (partNo, segCode))
            #print(type(segCode))
            cursor = conn.cursor()
            cursor.execute("""SELECT basic_price
                              FROM TestDB.dbo.qiquote
                              WHERE part_no = ? AND seg1_code = ? AND price_code = 'BAZOWY'
                              ORDER BY TestDB.dbo.qiquote.sysdocid DESC""", partNo, segCode)

            for i in cursor:
                basePrice = i[0]
                break

            cursor = conn.cursor()
            cursor.execute("""SELECT sysdocid
                              FROM TestDB.dbo.qiquote
                              WHERE part_no = ? AND seg1_code = ? AND price_code = ?
                              ORDER BY TestDB.dbo.qiquote.sysdocid DESC""", partNo, segCode, priceCode)


            for i in cursor:
                currentId = i[0]
                break

            cursor = conn.cursor()
            cursor.execute("""UPDATE TestDB.dbo.qiquote
                              SET basic_price = ?
                              WHERE sysdocid = ? """, basePrice currentId)
            print(basePrice)
                
        else:
            partNo = line
            print ('Symbol bez wariantu to %s' % partNo)
            cursor = conn.cursor()
            cursor.execute("""SELECT basic_price
                              FROM TestDB.dbo.qiquote
                              WHERE part_no = ? AND price_code = 'BAZOWY'
                              ORDER BY TestDB.dbo.qiquote.sysdocid DESC""", partNo)

            for i in cursor:
                basePrice = i[0]
                break

            cursor = conn.cursor()
            cursor.execute("""SELECT sysdocid
                              FROM TestDB.dbo.qiquote
                              WHERE part_no = ? AND price_code = ?
                              ORDER BY TestDB.dbo.qiquote.sysdocid DESC""", partNo, priceCode)
  
            for i in cursor:
                currentId = i[0]
                break

            cursor = conn.cursor()
            cursor.execute("""UPDATE TestDB.dbo.qiquote
                              SET basic_price = ?
                              WHERE sysdocid = ? """, basePrice, currentId)

            print(basePrice)
        #i+=1
conn.commit()
conn.close()
        
print('Done')
