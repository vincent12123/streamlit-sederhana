import streamlit as st
from datetime import datetime, timedelta
import pandas as pd

# set default time format
time_format = '%Y-%m-%d %H:%M:%S'

# create empty dataframe to store tasks
tasks_df = pd.DataFrame(columns=['Task', 'Due Date', 'Status'])

# define function to add task
def add_task(task, due_date):
    new_task = pd.DataFrame({'Task': [task], 'Due Date': [due_date], 'Status': ['Incomplete']})
    tasks_df = tasks_df.append(new_task, ignore_index=True)
    tasks_df.to_csv('tasks.csv', index=False)
    return tasks_df

# define function to mark task as complete
def complete_task(index):
    tasks_df.at[index, 'Status'] = 'Complete'
    tasks_df.to_csv('tasks.csv', index=False)
    return tasks_df

# define function to schedule task
def schedule_task(task, due_date, reminder):
    due_datetime = datetime.combine(due_date, datetime.min.time()) + timedelta(hours=reminder)
    st.write(f'Scheduling task "{task}" on {due_datetime.strftime(time_format)}')
    # insert code here to schedule task using a third-party library or service
    # for example: using the "schedule" library to schedule the task to run at the specified time

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

# schedule task form
st.sidebar.subheader('Schedule Task')
task = st.sidebar.text_input('Enter task')
due_date = st.sidebar.date_input('Due date')
reminder = st.sidebar.slider('Reminder (hours before due date)', 0, 24, 1)
if st.sidebar.button('Schedule Task'):
    schedule_task(task, due_date, reminder)
    st.success('Task scheduled successfully!')
