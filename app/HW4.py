from flask import Flask, render_template, request
import datetime, json
app = Flask(__name__)

@app.route("/", methods=['post', 'get'])

def home():
 message = ''
 if request.method == 'POST':
    
    #define all fields
    fname1 = request.form.get('fname1')
    lname1 = request.form.get('lname1')
    smoking1 = request.form.get('smoking1')
    ID1 = request.form.get('ID1')
    BDate1 = request.form.get('BDate1')
    fname2 = request.form.get('fname2')
    lname2 = request.form.get('lname2')
    smoking2 = request.form.get('smoking2')
    ID2 = request.form.get('ID2')
    BDate2 = request.form.get('BDate2')
    fname3 = request.form.get('fname3')
    lname3 = request.form.get('lname3')
    smoking3 = request.form.get('smoking3')
    ID3 = request.form.get('ID3')
    BDate3 = request.form.get('BDate3')
    
    #validations:

    #define validation function for First and Last name
    def NameValid(Name):
     Name = Name.replace(" ","")
     if len(Name)==0:
       message = "*Missing Name"
       return message
     if len(Name)!=0:
      if Name.isalpha()==False:
        message = '*Name must include letters only'
        return message
      else:
        message = ""
        return message
    
    #define function to capitalize first letter
    def CapLet(Name):
      Name = Name.title()
      return Name


    #define validation function for ID number 
    def IdValid(ID):
      if len(ID)==0:
        message = '*Missing ID Value'
        return message
      if ID.isdigit()==False:
        message = '*ID has to include numbers only'
        return message
      if len(ID)>9:
        message = '*Too long ID number'
        return message
      if len(ID) == 9:
        message = ''
        return message

    #define function to add 0's before short ID
    def AddZero(ID):
      if len(ID)<9 and len(ID)!=0:
        while len(ID)<9:
          ID = "0" + ID
      return ID

    #define bool function for Is_Smoking question
    def IsSmoke(Smoke):
      x=int(Smoke)
      return bool(x)

    #define function for birth date validation
    #check that employee is older then 18
    def BDay(BD):
     try:
      BD1=datetime.datetime.strptime(BD, "%Y-%m-%d")
      today = datetime.datetime.now()
      adult = datetime.datetime.now().replace(today.year-18)
     except:
      message = '*Missing Date'
      return message
     if BD1 > adult:
      message = '*Wrong date'
      return message
     else:
      message = ''
      return message

    
    #define function to convert birth date to dd/mm/yyy format
    def BDFormat(BD):
     try:
      BDnewFormat=datetime.datetime.strptime(BD, "%Y-%m-%d").strftime("%d/%m/%Y")
     except:
       return BD
     return BDnewFormat
    
    #Convert birth date to dd/mm/yyy format
    BD1=BDFormat(BDate1)
    BD2=BDFormat(BDate2)
    BD3=BDFormat(BDate3)
       
    # #error message definitions for colunms 1-2, all rows (Names)
    message11 = NameValid(fname1)
    message12 = NameValid(lname1)
    message21 = NameValid(fname2)
    message22 = NameValid(lname2)
    message31 = NameValid(fname3)
    message32 = NameValid(lname3)

    #capitalize first letter
    lname1 = CapLet(lname1)
    fname1 = CapLet(fname1)
    lname2 = CapLet(lname2)
    fname2 = CapLet(fname2)
    lname3 = CapLet(lname3)
    fname3 = CapLet(fname3)

    #error message definitions for colunm 4, all rows (ID number)
    message14 = IdValid(ID1)
    message24 = IdValid(ID2)
    message34 = IdValid(ID3)

    #add 0 before ID
    ID1 = AddZero(ID1)
    ID2 = AddZero(ID2)
    ID3 = AddZero(ID3)

    #error message for birth date
    message15 = BDay(BDate1)
    message25 = BDay(BDate2)
    message35 = BDay(BDate3)


    #check if smoking
    smoke1=str(IsSmoke(smoking1))
    smoke2=str(IsSmoke(smoking2))
    smoke3=str(IsSmoke(smoking3))

    #create final message
    messagefinal=''
    messageerror=''
    results = bool(message11)+bool(message12)+bool(message14)+bool(message15)+bool(message21)+bool(message22)+bool(message24)+bool(message25)+bool(message31)+bool(message32)+bool(message34)+bool(message35)
    if results==0:
      messagefinal = "Registration Form submitted successfully"
    else:
      messageerror = "*****Please check, you have problem with data in " + str(results) + " fields.*****"

    #create nested dictionary
    worklist = {
    "Employee#1" : {
      "First Name" : fname1,
      "Last Name" : lname1,
      "Is Smoking" : smoke1,
      "ID number" : ID1,
      "Birth Date" : BD1
    },
    "Employee#2" : {
      "First Name" : fname2,
      "Last Name" : lname2,
      "Is Smoking" : smoke2,
      "ID number" : ID2,
      "Birth Date" : BD2
    },
    "Employee#3" : {
      "First Name" : fname3,
      "Last Name" : lname3,
      "Is Smoking" : smoke3,
      "ID number" : ID3,
      "Birth Date" : BD3
    }
}

    #create json file
    JSON = json.dumps(worklist)
    
    #create data file
    file1=open("data.txt","w")
    text=JSON
    file1.write(text)
    file1.close()

    
    #page after submit:
    return render_template('HW4.html',smoke1=smoke1, smoke2=smoke2, smoke3=smoke3, messageerror=messageerror, messagefinal=messagefinal, ID1=ID1, ID2=ID2, ID3=ID3, fname1=fname1, lname1=lname1, fname2=fname2, lname2=lname2,fname3=fname3, lname3=lname3, BD1=BD1, BD2=BD2, BD3=BD3, smoking1=smoking1, smoking2=smoking2, smoking3=smoking3, message15=message15, message25=message25, message35=message35, message11=message11, message12=message12,message21=message21,message22=message22,message31=message31,message32=message32, message14=message14, message24=message24, message34=message34)
    


 return render_template('HW4.html')

if __name__ == "__main__":
 app.run(host="0.0.0.0", port=8080, debug=True)

