from flask import Flask, request, Response, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/page1/<string:passover>', methods=["GET", "POST"])
def demo(passover):

    return render_template('demo.html', info = passover)

@app.route('/page2', methods=["GET", "POST"])
def chooser():
    cls = 1;
    opt = [{"opt1":1,"opt6969":2,"opt3":3}, {"opt1":4,"crngeeeee":5,"opt3":6}]
    data = request.form.get("option")
    print(str(data))
    if str(data) != "None":
        return redirect(url_for('demo', passover = str(data)))

    return render_template('chooser.html', opts = opt, cls = cls )

if __name__ == '__main__':
    app.run()