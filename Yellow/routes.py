from flask import render_template, url_for, flash, redirect, request
from Yellow import app, db
from Yellow.forms import RecordForm
from Yellow.models import Record

@app.route("/")
@app.route("/index")
def home():
    return render_template('index.html',title="Home")

@app.route("/build_database")
def build_database():
    db.create_all()
    db.session.commit()
    return render_template('index.html',title='Home')

@app.route("/add_record", methods=['GET', 'POST'])
def add_record():
    form = RecordForm()
    if form.validate_on_submit():
        record = Record(companyname = form.companyname.data, email = form.email.data, phone = form.phone.data, address = form.address.data, city = form.city.data, state = form.state.data, zip = form.zip.data)
        print(record)
        # add the new record to the database
        db.session.add(record)
        db.session.commit()
        flash(f'Record created for {form.companyname.data}!', 'success')
        # go to the landing page
        return redirect(url_for("home"))

    # render the sign up page
    return render_template('add_record.html', title='Add Record', form=form)

@app.route("/display_records")
def display():
    Records = Record.query.all()
    for record in Records:
        print(record)
    return render_template('display_records.html',title='Display', Records = Records)


@app.route("/update_record/<int:record_id>/", methods=['GET', 'POST'])
def update_record(record_id):
    record = Record.query.get_or_404(record_id)
    form = RecordForm()
    form.submit.label.text = 'Update Item'
    if form.validate_on_submit():
        record.companyname = form.companyname.data
        record.email = form.email.data
        record.address = form.address.data
        record.phone = form.phone.data
        record.city = form.city.data
        record.state = form.state.data
        record.zip = form.zip.data

        db.session.commit()
        flash('Your product has been updated!', 'success')
        return redirect(url_for('display'))
    elif request.method == 'GET':
        form.companyname.data = record.companyname
        form.email.data = record.email
        form.address.data = record.address
        form.city.data = record.city
        form.state.data = record.state
        form.zip.data = record.zip
        form.phone.data = record.phone

    return render_template('add_record.html', title='Update Product',
                           form=form, legend='Update Product', update=1)
@app.route("/delete_record/<int:record_id>/", methods=['GET', 'POST'])
def delete_record(record_id):
    record = Record.query.filter_by(id=record_id).first()

    db.session.delete(record)
    db.session.commit()

    flash('The item was sucsessfully deleted from the database.', 'success')
    return redirect(url_for('display'))