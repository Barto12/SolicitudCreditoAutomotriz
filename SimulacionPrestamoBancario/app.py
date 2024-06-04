from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def loan_application():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        state = request.form['state']
        country = request.form['country']
        postal_code = request.form['postal_code']
        email = request.form['email']
        income = float(request.form['income'])

        if income >= 30000:
            loan_amount = 50000
        else:
            loan_amount = 20000

        return render_template('result.html', name=name, loan_amount=loan_amount)

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
