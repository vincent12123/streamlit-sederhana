import streamlit as st
from datetime import datetime, timedelta
import pandas as pd

# set default time format
time_format = '%Y-%m-%d %H:%M:%S'

# create empty dataframe to store tasks
tasks_df = pd.DataFrame(columns=['Task', 'Due Date', 'Status'])

# define function to add task
def add_task(task, due_date):
    global tasks_df
    new_task = pd.DataFrame({'Task': [task], 'Due Date': [due_date], 'Status': ['Incomplete']})
    tasks_df = tasks_df.append(new_task, ignore_index=True)
    tasks_df.to_csv('tasks.csv', index=False)
    return tasks_df

# define function to mark task as complete
def complete_task(index):
    tasks_df.at[index, 'Status'] = 'Complete'
    tasks_df.to_csv('tasks.csv', index=False)
    return tasks_df

# load tasks from csv file
tasks_df = pd.read_csv('tasks.csv')

# create sidebar
st.sidebar.header('Task Manager')

# add task form
st.sidebar.subheader('Add Task')
task = st.sidebar.text_input('Enter task')
due_date = st.sidebar.date_input('Due date')
if st.sidebar.button('Add Task'):
    tasks_df = add_task(task, due_date)
    st.success('Task added successfully!')

# view tasks
st.header('View Tasks')
st.table(tasks_df)

# mark task as complete
if st.button('Mark Task as Complete'):
    task_index = st.number_input('Enter task index', min_value=0, max_value=len(tasks_df)-1, value=0)
    tasks_df = complete_task(task_index)
    st.success('Task marked as complete!')

# view completed tasks
completed_tasks = tasks_df[tasks_df['Status'] == 'Complete']
st.header('Completed Tasks')
st.table(completed_tasks)

# define function to delete task
def delete_task(index):
    global tasks_df
    tasks_df = tasks_df.drop(index, axis=0)
    tasks_df.to_csv('tasks.csv', index=False)
    return tasks_df

# delete task
if st.button('Delete Task'):
    task_index = st.number_input('Enter task index', min_value=0, max_value=len(tasks_df)-1, value=0)
    tasks_df = delete_task(task_index)
    st.success('Task deleted successfully!')

# define function to edit task
def edit_task(index, new_task, new_due_date):
    global tasks_df
    tasks_df.at[index, 'Task'] = new_task
    tasks_df.at[index, 'Due Date'] = new_due_date
    tasks_df.to_csv('tasks.csv', index=False)
    return tasks_df

# edit task
if st.button('Edit Task'):
    task_index = st.number_input('Enter task index', min_value=0, max_value=len(tasks_df)-1, value=0)
    new_task = st.text_input('Enter new task', tasks_df.loc[task_index, 'Task'])
    new_due_date = st.date_input('Enter new due date', tasks_df.loc[task_index, 'Due Date'])
    tasks_df = edit_task(task_index, new_task, new_due_date)
    st.success('Task edited successfully!')

# view tasks by due date
if st.button('View Tasks by Due Date'):
    sorted_tasks = tasks_df.sort_values(by='Due Date')
    st.table(sorted_tasks)

# view tasks by status
if st.button('View Tasks by Status'):
    status = st.selectbox('Select status', ['Incomplete', 'Complete'])
    filtered_tasks = tasks_df[tasks_df['Status'] == status]
    st.table(filtered_tasks)

# define function to add reminder
def add_reminder(index, time):
    due_date = tasks_df.loc[index, 'Due Date']
    reminder_time = datetime.strptime(due_date, time_format) - timedelta(hours=time)
    now = datetime.now()
    if now >= reminder_time:
        st.warning(f"Reminder: Task '{tasks_df.loc[index, 'Task']}' is due soon!")
    else:
        delay = (reminder_time - now).total_seconds()
        st.write(f"Reminder will be shown in {delay} seconds.")
        time.sleep(delay)
        st.warning(f"Reminder: Task '{tasks_df.loc[index, 'Task']}' is due soon!")
        
# set reminder
if st.button('Set Reminder'):
    task_index = st.number_input('Enter task index', min_value=0, max_value=len(tasks_df)-1, value=0)
    reminder_time = st.number_input('Enter reminder time (in hours)', min_value=1, max_value=24, value=1)
    add_reminder(task_index, reminder_time)
