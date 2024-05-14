from flask import Flask, request, render_template , jsonify
from manager import *

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    table = all_data()
    date = nowdate()

    if request.method == "POST":
        mm = int(request.form.get("mm"))
        motor = int(request.form.get("motor"))
        slave = int(request.form.get("slave"))
        bill = int(request.form.get("bill"))
        print(mm,motor,slave,bill,date)
        seq, ground ,  first = cal(mm,motor,slave,bill)
        update_table(seq,date,mm,motor,slave,bill,ground,first)
        table = all_data()
        return render_template("index.html",tables=table,date=date,F=first,G=ground)
    
    return render_template("index.html",tables=table,date=date)





#app.run()
    