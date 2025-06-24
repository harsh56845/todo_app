import requests
import streamlit as st

API_URL = "https://todo-app-1-a5nh.onrender.com"



def get_todos():
    try:
        res = requests.get(f"{API_URL}/todos")
        return res.json()
    except:
        return []

def add_todo(new_task):
    return requests.post(f"{API_URL}/todos",json={"task":new_task})

def deleteTodo(index):
    return requests.delete(f"{API_URL}/todos/{index}")
    
st.title("ToDoey App")    

new_task = st.text_input("Enter Your task")
if st.button("Add task"):
    if new_task:
        add_todo(new_task)
        st.rerun()


st.subheader("Your Tasks:")
todos = get_todos()
for i,todo in enumerate(todos):
    col1,col2 = st.columns([0.8,0.2])
    with col1:
        st.write(f"-{todo['task']}")
    with col2:
        if st.button(f"❌",key=i):
            deleteTodo(i)
            st.rerun()
