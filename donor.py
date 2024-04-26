class Donor:
    def __init__(self, rowCells):
        self.rowIndex = 0
        self.donorID = ""
        self.firstName = ""
        self.lastName = ""
        self.companyName = ""
        self.eventStatus = ""
        self.attendees = 0
        self.date = ""
        self.type = ""
        self.attribute = ""
        self.headerDict = {
            "DONOR_ID" : "Donor ID",
            "SPOUSE_FIRST" : "Household: Spouse First Name",
            "SPOUSE_LAST" : "Household: Spouse Last Name",
            "PRIMARY_FIRST" : "Household: Primary First Name",
            "PRIMARY_LAST" : "Household: Primary Last Name",
            "COMPANY" : "Company Name",
            "EVENT_STATUS" : "Event Status",
            "ATTENDEES" : "Attendees",
            "DATE" : "Date",
            "SALE_TYPE" : "Type",
            "AMOUNT" : "Amount",
            "PAID" : "Paid",
            "CONNECTION" : "Attribute"
        }
        self.convertRowCellsList(rowCells)

    def incRowIndex(self):
        self.rowIndex += 1

    def convertRowCellsList(self, rowcells, rowindex):
        print("hello world")
        return
    
    
