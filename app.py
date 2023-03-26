from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

TASKS = []

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'POST':
        TASKS.append(request.form['new_task'])
        return redirect(url_for('index'))
    else:
        return render_template('index.html',
                           tasks=TASKS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)