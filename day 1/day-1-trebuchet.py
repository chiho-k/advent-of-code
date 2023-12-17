import csv

file = open("calibration value.txt", "r")

firstNumbers = []
lastNumbers = []
fileData = []
for line in file:
    fileData.append(line)
# PART 1
def calibration(list):
    combinedNumbersList = []
    combinedNumbers = 0
    for line in list:
        combinedNumber = 0
        for letter in line:
            try:
                firstNumber = int(letter)
                firstNumbers.append(firstNumber)
                combinedNumber += firstNumber*10
                break
            except:
                continue
        reversedLine = line[::-1]
        for letter in reversedLine:
            try:
                lastNumber = int(letter)
                lastNumbers.append(lastNumber)
                combinedNumber += lastNumber
                break
            except:
                continue
        combinedNumbersList.append(combinedNumber)
        combinedNumbers += combinedNumber
    return combinedNumbers
calibrated = calibration(fileData)
print("Sum of calibration values from Part 1: ", calibrated)

# PART 2
numberWordsFile = open("number words.csv", "r")
numberWordsDict = csv.DictReader(numberWordsFile)
numberWords = []
for row in numberWordsDict:
    numberWords.append(row)

words = []
for row in numberWords:
    words.append(row["word"])

def wordConverter(list):
    newLines = []
    for line in list:
        newLine = line
        for i in range(0, len(newLine)):
            for word in words:
                for row in numberWords:
                    if row["word"] == word:
                        number = row["number"]
                if word in newLine[i:i+len(word)]:
                    newLine = newLine[:i] + number + newLine[i+len(word)-1:]
            else:
                continue
        newLines.append(newLine)
    return newLines

newData = wordConverter(fileData)
calibratedNew = calibration(newData)
print("Sum of calibration values from Part 2: ", calibratedNew)
