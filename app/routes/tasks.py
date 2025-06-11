from flask import Blueprint,render_template,request,redirect,url_for,flash,session
from app import db
from app.models import Task

tasks_bp=Blueprint('tasks',__name__)

@tasks_bp.route('/')
def view_tasks(): # when user logs in,we fetch the tasks from db and then render those tasks using html template
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    
    tasks=Task.query.all()
    return render_template('tasks.html',tasks=tasks)

@tasks_bp.route('/add',methods=["GET","POST"]) # Letting user add their tasks after login
def add_task():
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    
    title=request.form.get('title')
    if title:
        new_task=Task(title=title,status='Pending')
        db.session.add(new_task)
        db.session.commit()
        flash('Task added successfully','success')
    return redirect(url_for('tasks.view_tasks'))

@tasks_bp.route('/toggle/<int:task_id',method=["POST"])
def toggle_status(task_id):
    task=Task.query.get(task_id)
    if task:
        if task.status=='Pending':
            task.status=='Working'
        elif task.status=='Working':
            task.status=='Done'
        else:
            task.status=='Pending'
        db.session.commit()
    return redirect(url_for('tasks.view_tasks'))