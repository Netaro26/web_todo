import streamlit as st
import functions

todos = functions.get_todos()

def get_todos():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("MY-TODO")
st.subheader("This is my todo app")
st.write("App to increase your productivity")

for index, todo in enumerate(todos):       # enumerate is used to get the index of the todo item in the list
    checkbox = st.checkbox(todo, key=todo) # key=todo is used to make sure that each checkbox has a unique key
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo] # delete the checkbox from the session state
        st.rerun() # rerun the app to update the UI

st.text_input(label="Enter a todo", placeholder="Add new todo...", 
              on_change=get_todos, key="new_todo")  

