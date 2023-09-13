def getEmpName():
    empName = input("Enter employee name: ")
    return empName

def getHoursWorked():
    hours = float(input("Enter hours"))
    return hours

def getHourlyRate():
    hourlyRate = float(input("Enter hourly rate: "))
    return hourlyRate

def getTaxRate():
    taxRate = float(input("Enter tax rate: "))
    taxRate = taxRate / 100
    return taxRate

def CalcTaxAndNetPay(hours, hourlyRate, taxRate):
    gPay = hours * hourlyRate
    incomeTax = gPay * taxRate
    netPay = gPay - incomeTax
    return gPay, incomeTax, netPay

def printinfo(empName, hours, hourlyRate, gPay, taxRate, incomeTax, netPay):
    print(empName, f"{hours:,.2f}", f"{hourlyRate:,.2f}", f"{gPay:,.2f}", f"{taxRate:,.1%}", f"{incomeTax:,.2f}", f"{netPay:,.2f}")

def PrintTotals(totalEmployess, totalHours, totalGrossPay, totalTax, totalNetPay):
    print(f"\nTotal number of employees: {totalEmployess}")
    print(f"Total hours: {totalHours:,.2f}")
    print(f"Total gross pay: {totalGrossPay:,.2f}")
    print(f"Total Tax: {totalTax:,.2f}")
    print(f"Total net pay: {totalNetPay:,.2f}")
    
if __name__ == "__main__":
    totalEmployees = 0
    totalHours = 0.00
    totalGrossPay = 0.00
    totalTax = 0.00
    totalNetPay = 0.00
    
while True:
    empName = getEmpName()
    if (empName.upper() == "END"):
        break
    hours = getHoursWorked()
    hourlyRate = getHourlyRate()
    taxRate = getTaxRate()
    gPay, incomeTax, netPay = CalcTaxAndNetPay(hours, hourlyRate, taxRate)
    
    printinfo(empName, hours, hourlyRate, gPay, taxRate, incomeTax, netPay)

    totalEmployees += 1
    totalHours += hours
    totalGrossPay += gPay
    totalTax += incomeTax
    totalNetPay += netPay

PrintTotals(totalEmployees, totalHours, totalGrossPay, totalTax, totalNetPay)

def getDatesWorked():
    fromDate = input("Please enter start date in the following format MM/DD/YYYY: ")
    endDate = input("Please enter end date in the following format MM/DD/YYYY: ")
    return fromDate, endDate

def getEmpName():
    empName = input("Enter employee name: ")
    return empName

def getHoursWorked():
    hours = float(input("Enter hours: "))
    return hours

def getHourlyRate():
    hourlyRate = float(input("Enter hourly rate: "))
    return hourlyRate

def getTaxRate():
    taxRate = float(input("Enter tax rate: "))
    taxRate = taxRate / 100
    return taxRate

def CalcTaxAndNetPay(hours, hourlyRate, taxRate):
    gPay = hours * hourlyRate
    incomeTax = gPay * taxRate
    netPay = gPay - incomeTax
    return gPay, incomeTax, netPay

def printInfo(empDetailList):
    totalEmployees = 0
    totalHours = 0.00
    totalGrossPay = 0.00
    totalTax = 0.00
    totalNetPay = 0.00
    for empList in empDetailList:
        fromDate = empList[0]
        endDate = empList[1]
        empName = empList[2]
        hours = empList[3]
        hourlyRate = empList[4]
        taxRate = empList[5]
        
        gPay, incomeTax, netPay = CalcTaxAndNetPay(hours, hourlyRate, taxRate)
        print(fromDate, endDate, empName, f"{hours:,.2f}", f"{hourlyRate:,.2f}", f"{gPay:,.2f}", f"{taxRate:,.1%}", f"{incomeTax:,.2f}", f"{netPay:,.2f}")
        totalEmployees += 1
        totalHours += hours
        totalGrossPay += gPay
        totalTax += incomeTax
        totalNetPay += netPay

        empTotals["totEmp"] = totalEmployees
        empTotals["totHours"] = totalHours
        empTotals["totGross"] = totalGrossPay
        empTotals["totTax"] = totalTax
        empTotals["totNet"] = totalNetPay
        
def printTotals(empTotals):
    print(f'Total Number of Employees: {empTotals["totEmp"]}')
    print(f'Total Hours of Employees:  {empTotals["totHours"]}')
    print(f'Total Gross Pay of Employees:  {empTotals["totGross"]}')
    print(f'Total Tax of Employees:  {empTotals["totTax"]}')
    print(f'Total Net Pay of Employees:  {empTotals["totNet"]}')
    
if __name__ == "__main__":
    empDetailList = []
    empTotals = {}
    while True:
        empName = getEmpName()
        if (empName.lower() == "end"):
            break
        fromDate, endDate = getDatesWorked()
        hours = getHoursWorked()
        hourlyRate = getHourlyRate()
        taxRate = getTaxRate()
        empDetail = []
        empDetail.insert(0, fromDate)
        empDetail.insert(1, endDate)
        empDetail.insert(2, empName)
        empDetail.insert(3, hours)
        empDetail.insert(4, hourlyRate)
        empDetail.insert(5, taxRate)
        empDetailList.append(empDetail)
        
    printInfo(empDetailList)
    printTotals(empTotals)
    
def GetEmpName():
    empName = input("Enter employee name: ")
    return empName

def GetDatesWorked():
    fromDate = input("Enter the start date (mm/dd/yyyy):")
    toDate = input("Enter the end date (mm/dd/yyyy):")
    return fromDate, toDate

def GetHoursWorked():
    hours = float(input("Enter the amount of hours worked: "))
    return hours

def GetHourlyRate():
    hourlyRate = float(input("Enter the hourly rate: "))
    return hourlyRate

def GetTaxRate():
    taxRate = float(input("Enter the tax rate: "))
    return taxRate

def CalcTaxAndNetPay(hours, hourlyRate, taxRate):
    grossPay = hours * hourlyRate
    incomeTax = grossPay * taxRate
    netPay = grossPay - incomeTax
    return grossPay, incomeTax, netPay

def printinfo(EmpDetailList):
    TotEmployees = 0
    TotHours = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    
    for EmpList in EmpDetailList:
        
        fromDate = EmpList[0]
        toDate = EmpList[1]
        empName = EmpList[2]
        hours = EmpList[3]
        hourlyRate = EmpList[4]
        taxRate = EmpList[5]

        grossPay, incomeTax, netPay = CalcTaxAndNetPay(hours, hourlyRate, taxRate)
        print(fromDate, toDate, empName, f"{hours:,.2f}", f"{hourlyRate:,.2f}", f"{grossPay:,.2f}", f"{taxRate:,.1%}", f"{incomeTax:,.2f}", f"{netPay:,.2f}")
    
        TotEmployees += 1
        TotHours += hours
        TotGrossPay += grossPay
        TotTax += incomeTax
        TotNetPay += netPay
    EmpTotals["TotEmp"] =TotEmployees
    EmpTotals["TotHrs"] = TotHours
    EmpTotals["TotGrossPay"] = TotGrossPay
    EmpTotals["TotTax"] = TotTax
    EmpTotals["TotNetPay"] = TotNetPay
    
def PrintTotals(EmpTotals):
    print()
    print(f"Total number of employees: {EmpTotals['TotEmp']}")
    print(f"Total hours worked: {EmpTotals['TotHours']}")
    print(f"Total gross pay: {EmpTotals['TotGrossPay']:,.2f}")
    print(f"Total income tax: {EmpTotals['TotTax']:,.1%}")
    print(f"Total net Pay: {EmpTotals['TotNetPay']:,.2f}")


def WriteEmployeeInformation(employee):
    file = open("employeeinfo.txt", "a")
    file.write('{}|{}|{}|{}|{}|{}|\n'.format(employee[0], employee[1], employee[2], employee[3], employee[4], employee[5]))
    
def GetFromDate():
    valid = False
    fromDate = ""
    
    while not valid:
        fromDate = input("Enter from date (mm/dd/yyyy): ")
        if (len(fromDate.split('/')) !=3 and fromDate.upper() != 'ALL'):
            print("Invalid date format")
        else:
            valid = True
            
    return fromDate

def ReadEmployeeInformation(fromDate):
    empDetailList = []
    
    file = open("employeeinfo.txt", "r")
    data = file.readlines()
    
    condition = True
    
    if fromDate.upper() == 'ALL':
        condition = False
        
    for employee in data:
        employee = [x.strip() for x in employee.strip().split("|")]
        
        if not condition:
            empDetailList.append(employee[0], employee[1], employee[2], float(employee[3]), float(employee[4]), float(employee[5]))
        else:
            if fromDate == employee[0]:
                empDetailList.append(employee[0], employee[1], employee[2], float(employee[3]), float(employee[4]), float(employee[5]))
    return empDetailList

if __name__ == "__main__":
    empDetailList = []
    empDetailList = {}
    
    while True:
        empName = GetEmpName()
        if(empName.upper() == "END"):
            break
        fromDate, toDate = GetDatesWorked()
        hours = GetHoursWorked()
        hourlyRate = GetHourlyRate ()
        taxRate = GetTaxRate ()
        
        print()

        empDetail + [fromDate, toDate, empName, hours, hourlyRate, taxRate]
        WriteEmployeeInformation(empDetail)
    print()
    print()
    fromDate = GetFromDate()
    
    EmpDetailList = ReadEmployeeInformation(fromDate)

    print()
    printinfo(empDetailList)
    print()
    PrintTotals(empTotals)
                                 
                                 
    
    