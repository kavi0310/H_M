from application import app, db
from flask import render_template, request, json, Response, redirect, flash, url_for
from application.models import Staff, Registration, Medicine, Test, ViewDetails
from application.forms import LoginForm, PatientRegForm, PatientUpdateForm, MedicineForm, TestForm

PatientDetails  = [{"Patient ID":"1111","Name":"Pragya","Age":"12","Address":"123,Gandhiji Road,Hyderabad","DOJ":"3.3.2019","Type of Room":"single"}, {"Patient ID":"2222","Name":"Abi","Age":"80","Address":"33/3,Nethaji Road,Kolkata","DOJ":"4.5.2019","Type of Room":"single"}, {"Patient ID":"3333","Name":"Shacksi","Age":"55","Address":"13,Lotus Street,Madurai","DOJ":"20.6.2020","Type of Room":"double"}, {"Patient ID":"4444","Name":"Sivanya","Age":"60","Address":"12,Kannayan Street,Goa","DOJ":"30.8.2019","Type of Room":"double"}, {"Patient ID":"5555","Name":"KhiKhu","Age":"36","Address":"4,Sangmang Street,China","DOJ":"12.12.2019","Type of Room":"single"}]

MedicineDetails = [{"medicine_name":"Dupixent","quantity":10,"rate":20,"amount":200}, {"medicine_name":"Otezla","quantity":20,"rate":50,"amount":1000}, {"medicine_name":"Brilinta","quantity":30,"rate":60,"amount":1800}]

TestDetails     = [{"test_name":"ECG","amount":3000}, {"test_name":"CBP","amount":2000}, {"test_name":"Lipid","amount":1500}]

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", index=True )

@app.route("/update")
def update():
    form = PatientUpdateForm()
    if form.validate_on_submit():
        # patient_id    = Registration.objects.count()
        # patient_id    += 1
        patient_id   = form.patient_id.data
        patient_name = form.patient_name.data
        patient_age  = form.patient_age.data
        date_of_join = form.date_of_join.data
        type_of_bed  = form.type_of_bed.data
        address      = form.address.data
        city         = form.city.data
        state        = form.state.data

        registration = Registration(patient_id=patient_id,patient_name=patient_name,patient_age=patient_age,date_of_join=date_of_join,type_of_bed=type_of_bed,address=address,city=city,state=state)
        registration.save()

        #flash("Patient creation initiated successfully")

        flash("Patient details Updated successfully","success")
        return redirect("/viewdetails")
    return render_template("update.html", update=True , form=form, title="Update Patient")    

@app.route("/delete")
def delete():
    return render_template("delete.html", delete=True )

@app.route("/login", methods=['GET','POST'])
def login():
    form =LoginForm()
    if form.validate_on_submit():
        name     = form.name.data
        password = form.password.data
        # if request.form.get("name") == "kavitha":
        staff =Staff.objects(name=name).first()
        # if staff and staff.get_password(password):
        if staff and password == staff.password:
            flash(f"{staff.name}, You are successfully logged in and Now, you are ready to access the "f"{staff.name} page", "success")
            if request.form.get("name") == "Pharmacist":
                return redirect("/pharmacy")
            if request.form.get("name") == "Diagnostic":
                return redirect("/diagnostics")
            if request.form.get("name") == "Admin":
                return redirect("/viewdetails")

        else:
            flash("Sorry! Incorrect Username or Password.", "danger")
            return redirect("/login")
    return render_template("login.html",title="Login", form=form, login=True)



@app.route("/registration", methods=['GET','POST'])
def registration():
    form = PatientRegForm()
    if form.validate_on_submit():
        # patient_id    = Registration.objects.count()
        # patient_id    += 1
        patient_id   = form.patient_id.data
        patient_name = form.patient_name.data
        patient_age  = form.patient_age.data
        date_of_join = form.date_of_join.data
        type_of_bed  = form.type_of_bed.data
        address      = form.address.data
        city         = form.city.data
        state        = form.state.data

        registration = Registration(patient_id=patient_id,patient_name=patient_name,patient_age=patient_age,date_of_join=date_of_join,type_of_bed=type_of_bed,address=address,city=city,state=state)
        registration.save()

        #flash("Patient creation initiated successfully")

        flash("You are Submitted the patient medicine form!","success")
        return redirect("/viewdetails")
    
    return render_template("registration.html", title="Patient Registration", registration=True, form=form)



@app.route("/viewdetails", methods=['GET','POST'])
def viewdetails():
    classes = Registration.objects.all()
    return render_template("viewdetails.html",PatientDetails=classes, viewdetails=True )


@app.route("/pharmacy", methods=['GET','POST'])
def pharmacy():
    # form = MedicineForm()
    # if form.validate_on_submit():
    #     medicine_name = form.medicine_name.data
    #     quantity      = form.quantity.data
    #     rate          = form.rate.data
    #     amount        = form.amount.data

    #     medicine = Medicine(medicine_name=medicine_name, quantity=quantity, rate=rate, amount=amount)
    #     medicine.save()
    #     flash("Patient Pharmacy details updated successfully")

    classes = Medicine.objects.all()
    return render_template("pharmacy.html", MedicineDetails=MedicineDetails, pharmacy=True)
    

@app.route("/diagnostics", methods=['GET','POST'])
def diagnostics():
    classes = Test.objects.all()
    return render_template("diagnostics.html", TestDetails=classes, diagnostics=True)

@app.route("/billing")
def billing():
    return render_template("billing.html", billing=True)    


@app.route("/api/")
@app.route("/api/<idx>")
def api(idx=None):
    if(idx == None):
        jdata = PatientDetails
    else:
        jdata = PatientDetails[int(idx)]
    
    return Response(json.dumps(jdata), mimetype="application/json")

@app.route("/staff")
def staff():
    #  Stakeholder(user_id=1, name="Admin", password="admin@123").save()
    #  Stakeholder(user_id=2, name="Pharmacist", password="pharmacist@123").save()
    #  Stakeholder(user_id=3, name="Diagnostic", password="diagnostic@123").save()
    staffs = Staff.objects.all()
    return render_template("staff.html", staffs=staffs)

@app.route("/medicine", methods=['GET','POST'])
def medicine():
    medicine_name = request.form.get('medicine_name')
    quantity      = request.form.get('quantity')
    rate          = request.form.get('rate')
    amount        = request.form.get('amount')
    #  medicines  = Medicine.objects.all()
    return render_template("medicine.html", medicine=True, data={"medicine_name":medicine_name,"quantity":quantity,"rate":rate,"amount":amount})

@app.route("/test", methods=['GET','POST'])
def test():
    test_name     = request.form.get('test_name')
    amount        = request.form.get('amount')
    # tests       = Test.objects.all()
    return render_template("test.html", test=True, data={"test_name":test_name,"amount":amount})