import codecs
import csv
from decimal import Decimal
import wx

app = wx.App()

filename = wx.FileSelector('Choose a CSV file', wildcard='*.csv')

if filename.endswith('.csv'):
    with open(filename, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        results = []
        count1 = []
        count2 = []
        count3 = []
        for row in csvreader:
            if row[0] == 'A':
                new = True
                for result in results:
                    if result[0] == row[33]:
                        pieces = row[10].replace(' ', '').split('\\')
                        result[1] = result[1] + int(pieces[0])
                        result[2] = result[2] + int(pieces[1])
                        result[3] = result[3] + Decimal(row[11])

                        new = False
                        break
                if new:
                    pieces = row[10].replace(' ', '').split('\\')
                    result = [row[33], int(pieces[0]), int(pieces[1]), Decimal(row[11])]
                    results.append(result)
        results.sort()
        with codecs.open(filename[0:-4] + '.txt', 'w', 'utf-8') as f:
            f.write('Valsts \t(Cik vietas iziet) \\ (Cik vietas kopā)\t\tkg\n\n')
            for result in results:
                if result[1] and result[2] >= 6 or result[0] == "GB" or result[0] == "CH" or result[0] == "RS":
                    f.write(result[0] + '\t' + str(result[1]) + ' \\ ' + str(result[2]) + '\t\t\t' + str(result[3]) + '\n')
                else:
                    count1.append(int(result[1]))
                    count2.append(int(result[2]))
                    count3.append(float(result[3]))
            f.write('\n\nSūtījumi uz mix-paletes - ' + str(sum(count1))+'/'+str(sum(count1))+'\t\t\t   '+str(round(sum(count3), 2))+' kg' + '\n' + 'Valsts \t(Cik vietas iziet) \\ (Cik vietas kopā)\t\tkg\n\n')
            for result in results:
                if result[1] and result[2] < 6:
                    if result[0] is not ["GB""CH""RS"]:
                        f.write(result[0] + '\t' + str(result[1]) + ' \\ ' + str(result[2]) + '\t\t\t' + str(result[3]) + '\n')
app.MainLoop()