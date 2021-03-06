from flask import Flask, request, Response, render_template, redirect, url_for

app = Flask(__name__)

#data structure imports
from data import classGenderTable, nationalityBreakdown, lifeBoatBreakdown

# base String to index hash table
S_iStatus = {"Male": 2, "Child": 1, "Female": 0}
S_iClass = {"First Class": 0, "Second Class": 1, "Third Class": 2}


@app.route('/')
def index():
    return redirect(url_for(demographics))


@app.route('/demo', methods=["GET", "POST"])
def demographics():
    #gather request info if any
    status_req = str(request.form.get("status"))
    cls_req = str(request.form.get("class"))
    if status_req and cls_req != "None":
        cls = S_iClass[cls_req]
        status = S_iStatus[status_req]
        return redirect(url_for("info",cls =cls, status =status))#send all relevant info to 'info'

    return render_template('demo.html')


@app.route('/info/<int:cls>/<int:status>', methods=["GET", "POST"])
def info(cls, status):
    # gather request info if any
    nationality_req = str(request.form.get("nation"))
    lifeboat_req = str(request.form.get("lb"))
    if nationality_req and lifeboat_req != "None":
        return redirect(url_for("results", cls = cls, status= status, nationality=nationality_req, lifeboat= lifeboat_req))#send all relevant info to 'results'

    return render_template("info.html", nation_table = nationalityBreakdown, lb_table =lifeBoatBreakdown, cls = cls, status= status)#renders page depending on prior info

@app.route("/results/<int:cls>/<int:status>/<string:nationality>/<string:lifeboat>", methods=["GET", "POST"])
def results(cls, status, nationality,lifeboat):
    chance = classGenderTable[cls][status] * nationalityBreakdown[cls][nationality] * lifeBoatBreakdown[cls][lifeboat]#
    return str(chance)

if __name__ == '__main__':
    app.run()
