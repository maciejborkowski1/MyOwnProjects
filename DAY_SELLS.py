import datetime

inputPath = 'c:\\temp\\201907130715.dat'
outputPath = 'c:\\temp\\SLIM_test.txt'
i=1

with open(inputPath,'r', errors='ignore') as inFile:
    for line in inFile:
        line = line.replace("'",'').replace('*','').replace('"','')
        line = line.split(',')
        line.insert(0,str(datetime.datetime.today().strftime('%Y%m%d')))
        del line[4:7]
        del line[5]
        del line[7]
        line = ';'.join(line)
        outFile = open(outputPath,'a')

        outFile.write(line)
        outFile.write('\n')

        outFile.close()
        i+=1

input('Raport zapisany w %s, ilość asortymentu %f' % (outputPath, i))







        


