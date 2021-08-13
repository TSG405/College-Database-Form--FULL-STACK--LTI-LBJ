import csv
from flask import Flask,render_template,request,Response,jsonify

app=Flask(__name__)   

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/addstudent", methods =["GET", "POST"])
def addstudent():
    if request.method == "POST":
        Student_ID=request.form.get("studentid")
        Student_Name=request.form.get("studentname")
        Gender=request.form.get('gender')
        DateOfBirth=request.form.get("dateofbirth")
        City=request.form.get("city")
        State=request.form.get("state")
        EmailId=request.form.get("email")
        Qualification=request.form.get("qualification")
        Stream=request.form.get("stream")
        data=[Student_ID,Student_Name,Gender,DateOfBirth,City,State,EmailId,Qualification,Stream]
        with open('students.csv', 'a', newline='') as csvfile:
            fieldnames = ['Student ID','Student Name','Gender','DateOfBirth','City','State','EmailId','Qualification','Stream']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'Student ID': Student_ID,'Student Name': Student_Name,'Gender': Gender, 
            'DateOfBirth': DateOfBirth ,'City': City, 'State': State,'EmailId': EmailId, 'Qualification': Qualification,
            'Stream': Stream})
        return render_template('index.html')
    else:
        return render_template('add-student.html')

@app.route("/searchstudent",methods =["GET", "POST"])
def searchstudent():
    rows=0
    tstate=False
    if request.method == "POST":
        Student_ID=request.form.get("Search")
        print(Student_ID)
        with open('students.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Student ID']==str(Student_ID):
                    rows=row
        tstate=True
        return render_template('search-student.html',row=rows,tstate=tstate)
    else:
        return render_template('search-student.html',row=rows,tstate=tstate)

@app.route("/displaystudents")
def displaystudents():
    rows=[]
    with open('students.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            rows.append(row)
    return render_template('display-students.html',rows=rows)

if __name__=='__main__':
    app.run(debug=True)


@CODED BY TSG405, 2021
