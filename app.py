from flask import Flask, render_template, request, jsonify, redirect, url_for, abort
import sqlite3

app = Flask(__name__)

TASKS = []

@app.route("/tasks", methods=['GET','POST'])
def index():
    if request.method == 'POST':        
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

@app.route("/tasks/<int:id>", methods=['GET'])
def get_tasks_by_id(id):
    conn = sqlite3.connect('todo-database.db')
    cur = conn.cursor()

    get_query = f"SELECT * from TO_DO_TASKS where USER_ID='{id}'"
    tasks = cur.execute(get_query).fetchall()
    print(tasks)
    conn.close()
    
    return render_template('index.html', tasks=tasks)

@app.route("/tasks/<int:id>", methods=['POST'])
def action_tasks_by_id(id):
    conn = sqlite3.connect('todo-database.db')
    cur = conn.cursor()
    if request.form['action'] == 'add_new_task':
        #insert into database
        new_task = request.form['new_task']
        insert_task = f"INSERT INTO TO_DO_TASKS(TASK_NAME, USER_ID) values(?,?)"
        cur.execute(insert_task, (new_task,id,))
        conn.commit()
    
    elif request.form['action'] == "Delete":
        pass
        #delete from database
    elif request.form['action'] == 'Completed':
        pass
        #strike-through or delete
    elif request.form['action'] == "edited_task":
        pass
        #update the task
    
    conn.close()
    return redirect(url_for('get_tasks_by_id', id=id))


@app.route("/", methods=['GET', 'POST'])
def home_page():
    if request.method == 'POST':
        conn = sqlite3.connect('todo-database.db')
        cur = conn.cursor()
        
        if request.form['action'] == 'login_into':
            user_name = request.form['user_name']
            password = request.form['password']

            search_user = f"SELECT * from TO_DO_USERS where USERNAME='{user_name}' AND PASSWORD='{password}';"
            result = cur.execute(search_user)
            row = result.fetchone()
            conn.close()
            if not row:
                return render_template('message.html', message="USER NOT FOUND!! Please register first.")
            else:
                return redirect(url_for('get_tasks_by_id'))
        
        elif request.form['action'] == "register_into":
            user_name = request.form['user_name']
            password = request.form['password']
            email = request.form['email']
            try:
                insert_user = f"INSERT INTO TO_DO_USERS(USERNAME,PASSWORD,EMAIL) values(?,?,?)"
                cur.execute(insert_user, (user_name, password, email))
                conn.commit()
                conn.close()
                return render_template('message.html', message="USER CREATED!! Please login again.")
            except Exception as e:
                return render_template('message.html', message="SOME ERROR, USER NOT CREATED!!")
    else:
        return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)