import csv

gotCsv = 'got.csv'
scriptOut = 'gotScript.txt'

with open(gotCsv, mode='r') as csvFile:
    with open(scriptOut, mode'w' as script):
        reader = csv.DictReader(csvFile)
        cols = []
        lineNum = 0
        for row in reader:
            if lineNum == 0:
                cols = row
            else:
                if row['character'] != 'DEFAULT':
                    continue
                script.write(row['character'])    
                script.write(row['utterance'])
                script.write()
            lineNum += 1
