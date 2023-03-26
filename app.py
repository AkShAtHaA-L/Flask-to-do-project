from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

TASKS = []

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'POST':
        if 'action' not in request.form:
            print(request.method)
        
        if request.form['action'] == 'add_new_task':
            TASKS.append(request.form['new_task'])
        
        else:
            task_id = int(request.form['task_id'])
            if request.form['action'] == 'Completed':
                del TASKS[task_id]
            
            elif request.form['action'] == "Delete":
                del TASKS[task_id]
            
            elif request.form['action'] == "edited_task":
                task_id = int(request.form['task_id'])
                new_task = request.form['new_task']

                TASKS[task_id] = new_task
        
        return redirect(url_for('index'))
    else:
        return render_template('index.html',
                           tasks=TASKS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)