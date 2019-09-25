inputPath = 'path'
outputPath = 'path'

delCount = 0
saveCount = 0
i = 0

with open(inputPath,'r', encoding='utf-8') as fileIn:
    for line in fileIn:
        line = line.replace('delisting','nie').replace('listing','tak')\
               .replace('zmiana','nie').replace('\t','').replace(' ','')\
               .replace('gratis','nie')
        line = line.split(';')
        item1 = 'KOMPLEX'
        item2 = 'ZEWNĘTRZNY'
        item3 = 'PUSTEPOLE'
        if item3 in line:
            del line[17]
            line.insert(17,'nie')        
        if (not item1 or not item2 or not item3) in line:
            del line
            delCount +=1
        else:
            del line[0]
            del line[1:17]
            del line[2:]
            line.insert(0,'WEGORZEWO')
            item = 'tak-pakiet'
            if item in line:
                del line
                delCount +=1
            else:
                if i < 2:
                    del line
                    delCount +=1
                    i+=1
                else:
                    line = ';'.join(line)
                    line = line.replace('tak-sztuki','tak')
                    print(line)
                    saveCount +=1

                    fileOut = open(outputPath,'a')
                    fileOut.write(line)
                    fileOut.write('\n')
                    fileOut.close()
                    i+=1

input('Done, saved:%d, deleted:%d' % (saveCount, delCount))        

