from pprint import pprint

class Donor:
    def __init__(self, rowCells, indexMap, headerDict, headerOrder):
        self.rowIndex = 0
        self.properties = dict()
        self.indexMap = indexMap
        self.headerDict = headerDict
        self.headerOrder = headerOrder
        self.convertRowCellsList(rowCells, indexMap)

    def incRowIndex(self):
        self.rowIndex += 1

    def getValueFromKey(self, key, rowCells):
        if (key == "FIRST_NAME") or (key == "LAST_NAME") or (key == "PAID"):
            return
        insideHeaderDict = self.headerDict[key]
        index = self.indexMap[insideHeaderDict["name"]]
        value = rowCells[index]
        return value
    
    def getNames(self, rowCells):
        """Additional processing to check if last names are different
        Takes a list of row cell values and returns a dict of First and Last name"""
        primaryLastIndex = self.indexMap[self.headerDict["PRIMARY_LAST"]["name"]]
        primaryLastValue = rowCells[primaryLastIndex]
        spouseLastIndex = self.indexMap[self.headerDict["SPOUSE_LAST"]["name"]]
        spouseLastValue = rowCells[spouseLastIndex]

        primaryFirstIndex = self.indexMap[self.headerDict["PRIMARY_FIRST"]["name"]]
        primaryFirstValue = rowCells[primaryFirstIndex]
        spouseFirstIndex = self.indexMap[self.headerDict["SPOUSE_FIRST"]["name"]]
        spouseFirstValue = rowCells[spouseFirstIndex]

        if primaryFirstValue is None and primaryLastValue is None:
            return
        
        firstNameList = []
        # no spouse
        if spouseFirstValue is None and spouseLastValue is None:
            return {"first" : primaryFirstValue, "last" : primaryLastValue}
        # same last name
        elif primaryLastValue == spouseLastValue:
            firstNameList.append(spouseFirstValue)
            firstNameList.append("&")
            firstNameList.append(primaryFirstValue)
        # different last name
        elif primaryLastValue != spouseLastValue:
            firstNameList.append(spouseFirstValue)
            firstNameList.append(spouseLastValue)
            firstNameList.append("&")
            firstNameList.append(primaryFirstValue)

        firstName = " ".join(firstNameList)
        lastName = primaryLastValue

        return {"first" : firstName, "last" : lastName}
    
    def getCompany(self):
        """Additional processing for sub donors to get the company name if there is none"""
        return

    def convertRowCellsList(self, rowCells, rowindex):
        for header in self.headerOrder:
            self.properties[header] = self.getValueFromKey(header, rowCells)

        namePair = self.getNames(rowCells)

        if namePair:
            self.properties["FIRST_NAME"] = namePair["first"]
            self.properties["LAST_NAME"] = namePair["last"]


        # for key, value in list(self.properties.items()):
        #     print(key, value)

        return
    
    
