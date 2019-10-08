import datetime
import calendar

inputPath = 'c:\\temp\\kcfirma.csv'
outputPath = 'c:\\temp\\KCtest.txt'
i=0

today = datetime.date.today()
tenDayOfMonth = str(today)[:-2] + '10'
print(tenDayOfMonth)

year = today.year
month = today.month

lastDay = calendar.monthrange(year, month)[1]

lastDayOfTheMonth = str(today)[:-2] + str(lastDay)
print(lastDayOfTheMonth)


with open(inputPath, 'r', errors='ignore') as inFile:
    for line in inFile:
        if i == 0:
            del line
            i+=1
        else:
            line = line.split(';')
            del line[0]
            del line[2]
            del line[2]
            del line[3:5]
            del line[4:]
            temp = line[3]
            line[3] = temp[:-1]
            line3 = line[3]
            line2 = line[2]
            line[3] = line2
            line[2] = line3
            line.insert(2,'')
            line.insert(4,'szt')
            line.insert(5,'1')
            line.insert(5,'1')
            line.insert(5,'1')
            line.insert(5,'1')
            line.append(tenDayOfMonth)
            line.append(lastDayOfTheMonth)
            line.append('0')
            line.append('0')
            line.append('0')
            line.append('')
            line.append('')
            line.append('')
            line.append('')
            line.append('')
            line.append('')
            line.append('')
            line.append('')
            line=';'.join(line)
            print(line)
            fileOut = open(outputPath,'a')
            fileOut.write(line)
            fileOut.write('\n')
            fileOut.close()
