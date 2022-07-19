#Study Time Identifier
#Jeremy Bargy
#3/31/20


def welcome():  #define welcome function

    beginSequence= 'y'       #str
    
    print('\n\t\t\t\tHello Users!\n\t\t\t\t---------------')
    print('Thank you for taking the time to use this program.')
    print('The program was made by Jeremy Bargy.')
    print('Last update March 2020')

    #Display description of program
    print('\n\t\t\t\tInstructions\n\t\t\t\t------------')
    print('The program being used is designed to help students identify their study needs for this semester.\n')
    print('With this information, students can build and develop their own study habits to meet their academic goals.\n\n')
   
    #loop until user had read instructions
    beginSequence = input('Begin program?\n Please enter Y for yes\n')
    while not(beginSequence == 'Y' or beginSequence == 'y') or beginSequence=='' or beginSequence== ' ':
        print('\nError: please read the instructions and enter "Y" for yes to begin: \n')
        beginSequence= input('Begin program? \n\n')

def main():     #define main function
    menuOption = ""
 
    welcome()
    #Program menu for user to pick purchase options
    while menuOption != "C" and menuOption != "c":
        
        menuOption = getMenuOption(menuOption)
    
        if menuOption =="A" or menuOption =="a":
            
            #initialize variables
            STUDYHOURS = "studyHours.txt"
            #check for file
            checkFile(STUDYHOURS)
            
            AcreditTotal = 0
            AstudentCount = 0
            AtotalStudyHours = 0
              
            # Open study hours txt file to read
            studyHoursFile = open('StudyHours.txt', 'r')
        
            #read the student name and validate
            userName = studyHoursFile.readline()
        
            #continue reading with the condition of a user name existing
            while userName != '':

                #validate variable and accumulate count
                userName = validateName(userName)
                AstudentCount = accumuateCount(AstudentCount)

                #read credit hours and validate
                creditHours = studyHoursFile.readline()
                creditHours = creditHours.rstrip('\n')
                creditHours = validateCreditHours(creditHours)
                AcreditTotal += accumulateTotal(creditHours)
                classes = getNumofClasses(creditHours)

                #read desired grade and validate
                grade = studyHoursFile.readline()
                grade = grade.rstrip('\n')
                grade = validateGrade(grade)
            
                #get study hours per class from grade desired
                studyHours = getStudyHours(grade)
                            
                #get total study hours per week 
                TotalStudyHoursPerWeek = getTotalStudyHoursPerWeek(classes, studyHours)
                AtotalStudyHours += accumulateTotal(TotalStudyHoursPerWeek)

                #strip escape character and display results
                userName = userName.rstrip('\n')
                print('\nStudent Name: \t',userName)
                print('Credit Hours: \t',creditHours)
                print('Study Hours Recommended: ',TotalStudyHoursPerWeek)
                print('Desired Grade: \t',grade.upper(),'\n')

                #read next line from file
                userName = studyHoursFile.readline()

            #close file
            studyHoursFile.close()
            
        elif menuOption == "B" or menuOption == "b":

            #initialize variables and check file
            GRADES = "Grades.txt"
            checkFile(GRADES)
            
            BcreditTotal = 0
            BstudentCount = 0
            BtotalStudyHours = 0
        
            # Open grades text file to read
            gradesFile = open('Grades.txt', 'r')
        
            #read the student name and validate
            studentName = gradesFile.readline()
        
            #continue reading with the condition of a user name existing
            while studentName != '':

                #validate variable and accumulate count
                studentName = validateName(studentName)
                BstudentCount = accumuateCount(BstudentCount)

                #read credit hours and validate
                creditHoursB = gradesFile.readline()
                creditHoursB = creditHoursB.rstrip('\n')
                creditHoursB = validateCreditHours(creditHoursB)

                #validate variable and accumulate total
                BcreditTotal += accumulateTotal(creditHoursB)
                classesB = getNumofClasses(creditHoursB)
            
                #get study hours per class from grade desired
                studyHoursB =gradesFile.readline()
                studyHoursB = studyHoursB.rstrip('\n')
                studyHoursB = validateStudyHrs(studyHoursB, creditHoursB)

                #accumulate total
                BtotalStudyHours += accumulateTotal(studyHoursB)

                #use function to get variable
                gradeB = getGrade(classesB, studyHoursB)

                #display output
                studentName = studentName.rstrip('\n')
                print('\nStudent Name: \t',studentName)
                print('Credit Hours: \t',creditHoursB)
                print('Study Hours Allocated: ',studyHoursB)
                print('Possible Grade Earned: \t',gradeB.upper(),'\n')

                #read next line from file
                studentName = gradesFile.readline()

            #close file
            gradesFile.close()
            
            
        else:           #menu option C
            try:        #try operation with counts and totals from menu option A and menu option B
                totalStudents = (AstudentCount + BstudentCount)
                averageCredits = (AcreditTotal + BcreditTotal) / totalStudents
                averageStudyHours = (AtotalStudyHours + BtotalStudyHours) / totalStudents
            except UnboundLocalError:       #error message that files were not read, initializes counts and totals to equal to 0
                print('\nThere is an error reading input for averages.')
                print('Please return to the main menu and read in the appropriate files.\n')
                AstudentCount = 0
                BstudentCount = 0 
                totalStudents = (AstudentCount + BstudentCount)
                AcreditTotal = 0
                BcreditTotal = 0
                averageCredits = 0
                AtotalStudyHours = 0
                BtotalStudyHours = 0
                averageStudyHours = 0

            #display output
            print('\nProgram Averages: ')
            print('--------------------\n')
            print('Total Students: \t', totalStudents)
            print('Average Credit Hours: ', averageCredits)
            print('Average Study Hours: \t', averageStudyHours)
            print('\n\nThanks for using our program!')
            #end program if menu option c is selected


def getMenuOption(menuOption):      #function to get input for menu option and validates
    menuOption = input("\nSelect A -- Determine Hours to Study.\nSelect B -- Determine Grade.\nSelect C -- Display Totals and End the Program.\n")
    #validates the entry. The user has to pick a menu option  
    while menuOption != "A" and menuOption != "a" and menuOption != "B" and menuOption != "b" and menuOption != "C" and menuOption != "c":
        print("\nError: Please enter option A, B,or C.\n")
        menuOption = input("\nSelect A -- Determine Hours to Study.\nSelect B -- Determine Grade.\nSelect C -- Display Totals and Ends the Program.\\nn")
    return menuOption
                
def validateName(userName):     #function to validate passed argument of the user name variable
    try:        #try validation for name
        while(userName.isdigit()):
            print('\nError: incorrect name input')
            print('--------------------------------\n')
            userName =input('Please enter your full name input: \n')
        return userName
    except ValueError: #exception for value error, then asks user to enter a name
        print('Error: There is a value error for name')
        print('---------------------------------------\n')
        userName =input('Please enter your full name input: \n')
        return userName

def validateCreditHours(creditHours):       #function to validate passed argument of the credit hour variable
    try:        #try validation for digit that is divisible by 3 and greater then 3 and less than 18
        while not(int(creditHours.isdigit())) or not(int(creditHours) % 3 ==0) or int(creditHours) > 18 or int(creditHours) < 3 or int(creditHours)== '' or int(creditHours)== ' ':
            print('\nError: incorrect credit hours input')
            print('---------------------------------------\n')
            creditHours = (input('Please enter the credit hours you are currently enrolled in. i.e. Must be between 1 and 6 classes. Or as required, 3 - 18 credit hours. \n\n'))
        creditHours= int(creditHours)
        return creditHours
    except ValueError:      #exception for value error, then asks user to enter valid credit hours
        print('Error: There is a value error for credit hours')
        print('----------------------------------------------\n')
        creditHours = (input('Please enter the credit hours you are currently enrolled in. i.e. Must be between 1 and 6 classes. Or as required, 3 - 18 credit hours. \n\n'))
        while not(int(creditHours.isdigit())) or not(int(creditHours) % 3 ==0 ) or int(creditHours) > 18 or int(creditHours) < 3 or int(creditHours)== '' or int(creditHours)== ' ':
            print('\nError: incorrect credit hours input')
            creditHours = (input('Please enter the credit hours you are currently enrolled in. i.e. Must be between 1 and 6 classes. Or as required, 3 - 18 credit hours. \n\n'))
        creditHours= int(creditHours)
        return creditHours
    
def getNumofClasses(creditHours):       #function to get number of classes from passed argument of credit hours
    CREDITSPERCLASS = 3
    classes = int(creditHours) / CREDITSPERCLASS
    return classes

def validateGrade(grade):       #function to validate passed argument of the grade variable
    try:        #try validation for letter grade between A and F
        while not(grade.isalpha()) or not(grade=='A' or grade=='a' or grade =='B' or grade== 'b' or grade== 'C' or grade== 'c' or grade== 'D' or grade== 'd' or grade== 'F' or grade== 'f') or grade == '' or grade == ' ':
            print('\nError: incorrect grade input')
            print('------------------------------------\n')
            grade= input('Please enter the grade you wish to earn: \n\n')
        return grade
    except ValueError:      #exception for value error, then asks user to enter valid grade
        print('Error: There is a value error for grade')
        print('----------------------------------------\n')
        grade = input('Please enter the grade you wish to earn: \n\n')
        return grade
    
def getStudyHours(grade):       #function to get study hours from passed argument of the grade variable
    studyHours = 0
    if grade == 'A' or grade == 'a':
        studyHours = 15
    elif grade == 'B' or grade == 'b':
        studyHours = 12
    elif grade == 'C' or grade == 'c':
        studyHours = 9
    elif grade == 'D' or grade == 'd':
        studyHours = 6
    else:
        studyHours = 0
    return studyHours

def getTotalStudyHoursPerWeek(classes, studyHours):     #function to get total study hours per week from passed argument of classes and study hour variables
    TotalStudyHoursPerWeek= classes * studyHours
    return TotalStudyHoursPerWeek

def validateStudyHrs(studyHoursB, creditHoursB):        #function to validate study hours with passed arguments of study hours and credit hours
    try:        #try validation for number between 0 and 125
        while not(int(studyHoursB.isdigit())) or int(studyHoursB) < 0 or int(studyHoursB) > 125 or int(studyHoursB)< creditHoursB or int(studyHoursB) == '' or int(studyHoursB) == ' ':
            print('Error: incorrect study hours input')
            print('---------------------------------------\n')
            studyHoursB = input('Please enter in a positve number for your study hours that is more than your credit hours.\n Do not excced 125. You still need time to rest! :\n')
        studyHoursB = int(studyHoursB)
        return studyHoursB
    except ValueError:      #exception for value error, then asks user to enter valid study hours
        print('Error: There is a value error for study hours')
        print('----------------------------------------------\n')
        studyHoursB = input('Please enter in a positve number for your study hours. Do not excced 125. You still need time to rest! :\n')
        return studyHoursB

def getGrade(classesNum, expecthoursofstudy):       #function to get grade from passed arguments of number of classes and expected hours of study
    gradeDesired = ''
    studyhoursperclass = 0
    studyhoursperclass = int(expecthoursofstudy) / classesNum
    
    if studyhoursperclass >= 15:
        gradeDesired = 'A'
    elif studyhoursperclass >= 12:
        gradeDesired = 'B'
    elif studyhoursperclass >= 9:
        gradeDesired = 'C'
    elif studyhoursperclass >= 6:
        gradeDesired = 'D'
    else:
        gradeDesired = 'F'
    return gradeDesired

def checkFile(validateFile):    #define check file function. validates there is a file to read, creates file if none found
    try:
        # Open the file.
        infile = open(validateFile, 'r')

        # Close the file.
        infile.close()
    except IOError:             #for IOerror display message, append file for passed argument variable, close new file
        print('\nAn error occurred trying to read the file. --', validateFile)
        print('Sample data has been provided. Please ask administrator to load the correct files when finished. \n')
        sampleFile = open(validateFile, 'a')
        sampleFile.close()
        
def accumuateCount(countVariable):      #function to accumulate from passed argument of count variable
    countVariable +=1
    return countVariable

def accumulateTotal(accVariable):       #function to accumulate total from passed argument of total variable
    totalVariable = 0
    totalVariable += int(accVariable)
    return int(totalVariable)

main()
