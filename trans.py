inputFile = 'C:\\TransferyMiesięczne\\lista.csv'
allDocsFile = 'C:\\TransferyMiesięczne\\Dok_.csv'
outputFile = 'C:\\TransferyMiesięczne\\docsToTransfer.csv'
documentsList = []
documentsCheckList = []

with open(inputFile, 'r', errors='ignore') as file:
    for line in file:
        line=line.split(';')
        doc = line[0].replace('\n','')
        documentsList.append(doc)
print('Lista dokumentów do przetransferowania:')
print(documentsList)
print('Ilość: '+ str(len(documentsList))+'.')

i=0

with open(allDocsFile, 'r', errors='ignore') as file:
    for line in file:
        for doc in documentsList:
            if i == 0:
                fileOut = open(outputFile,'w')
                fileOut.write(line)
                fileOut.close()
                i+=1
            else:
                lineCheck = line.split('|')
                docCheck = lineCheck[8].replace('"','')
                if docCheck == doc:
                    documentsCheckList.append(docCheck)
                    fileOut = open(outputFile,'a')
                    fileOut.write(line)
                    fileOut.close()
                    break
            
print('Lista dokumentów przygotowana do przetransferowania plik \'Dok_.csv\':')
print(documentsCheckList)
print('Ilość: '+ str(len(documentsCheckList))+'.')
input('Porównaj listy!!')
