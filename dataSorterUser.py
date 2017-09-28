#import json
import csv
import math
import sys

def sort(fileN,num1,num2,num3,num4,num5,num6,num7):
    # print(fileN)
    # print(num1)
    # print(num2)
    # print(num3)
    # print(num4)
    # print(num5)
    # print(num6)
    # print(num7)
    data = []
    #Testing variables to be replaced by user input later
    fileName = fileN
    ROYGBIVpercents = [int(num1),int(num2),int(num3),int(num4),int(num5),int(num6),int(num7)]

    #Load in raw data and put into list to be editited later
    with open(fileName) as csvfile:
        fieldnames = ['Country','Val']
        reader = csv.DictReader(csvfile, fieldnames = fieldnames)
        for row in reader:
            data.append( (float(row['Val']),row['Country']) )
            
    data.sort() # Sorts by value smaller->larger   
    data.reverse() # Reverses order, list currently larger->smaller
    #Left with list of tuples sorted in decending order
    #Access Data By...
    #    currTupl = data[0]
    #    print currTupl[0] # Prints Number
    #    print currTupl[1] # Prints String      

    numElem = len(data)
    #Adjust ROYGBIVpercents so that the values contained in th cells represent the number of elements
    #in each percentile bucket
    for i in range(len(ROYGBIVpercents)):
        ROYGBIVpercents[i] = math.ceil(ROYGBIVpercents[i]*.01*numElem)
    dataMOD = []    
    for i in range(len(ROYGBIVpercents)):
        for j in range(int(ROYGBIVpercents[i])):
            if len(data) > 0:
                currTupl = data.pop(0)
                adjustedVal = 7-i
                dataMOD.append ( (int(adjustedVal),currTupl[1]) )
    #Make dictionary where country names are mapped to codes
    codesDict = {}
    codesFile = "countryCodes.csv"
    with open(codesFile) as csvfile2:
        reader2 = csv.DictReader(csvfile2)
        for row in reader2:
            codesDict[row['COUNTRY']] = row['CODE']
            
    # There is an issue with writing entries with strange characters to json file. maybe revisit later        
    # with open('countryDict.txt', 'w') as outfile:  
    #     json.dump(codesDict, outfile)

    #Make final file for mapBuilder.py
    finalFile = open("processedData.csv","w")

    finalFileHeader = "COUNTRY,VALUE,CODE\n"
    finalFile.write(finalFileHeader)
    for i in range(len(dataMOD)):
        currTupl = dataMOD.pop(0)
        try:
            newline = codesDict[currTupl[1]] + "," + str(currTupl[0]) + "," + codesDict[currTupl[1]] + "\n"
            finalFile.write(newline)
        except Exception, e:
            try:
                countryName = currTupl[1].split(" [")[0]
                newline = codesDict[countryName] + "," + str(currTupl[0]) + "," + codesDict[countryName] + "\n"
                finalFile.write(newline)
            except Exception, e:
                try:
                    countryName = currTupl[1].split(" (")[0]
                    newline = codesDict[countryName] + "," + str(currTupl[0]) + "," + codesDict[countryName] + "\n"
                    finalFile.write(newline)
                except Exception, e:
                    try: # TRY REMOVING "THE" FROM COUNTRY NAME UNLESS CONGO
                        countryName = currTupl[1].replace('the', '').replace('The', '')
                        newline = codesDict[countryName] + "," + str(currTupl[0]) + "," + codesDict[countryName] + "\n"
                        finalFile.write(newline)
                    except Exception, e:
                        print(currTupl[1] + " not on map")
        #Maybe try country omitting () and [] in name