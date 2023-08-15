from flask import Flask ,request,render_template,jsonify

app = Flask(__name__)

# flask app url routing

@app.route("/")
def hello():

    return "<h1>HELLO WORLD</h1>" 


@app.route("/py/<score>")

def name(score) :

    return "<h2> my name is AWNISH "+score+"</h1>"

@app.route('/form', methods=['GET','POST'])
def form():
    if request.method =="GET":
        return render_template('form.html')
    else:
         maths= float(request.form['maths'])
         phy= float(request.form['physics'])
         chem= float(request.form['chemistry'])
         avg = (maths+phy+chem)/3
         return render_template('form.html',score=avg)

@app.route('/api', methods=['post'])
def sum():
    data=request.get_json()
    a=float(dict(data)['a'])
    b= float(dict(data)['b'])
    return jsonify(a+b)

if __name__=="__main__":

    app.run(debug=True)