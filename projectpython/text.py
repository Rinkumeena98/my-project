import streamlit as st

def task_management():
    st.title("Task Management App")
    
    # Initialize session state for tasks if not already initialized
    if "tasks" not in st.session_state:
        st.session_state.tasks = []

    # User interface for adding initial tasks
    total_task = st.number_input("How many tasks would you like to add?", min_value=1, value=5, step=1)

    # Display current tasks in a list
    st.subheader("Current Tasks:")
    st.write(st.session_state.tasks)

    # Section to add initial tasks
    for i in range(1, total_task + 1):
        task_name = st.text_input(f"Enter task {i}", key=f"task_{i}")
        if task_name:
            st.session_state.tasks.append(task_name)
            st.write(f"Task '{task_name}' added.")

    # Display tasks again after adding initial tasks
    st.subheader("Today's Tasks:")
    st.write(st.session_state.tasks)

    # Task management operations (Add, Update, Delete, View, Exit)
    operation = st.radio("Choose an operation", options=["Add", "Update", "Delete", "View", "Exit"])

    if operation == "Add":
        add_task = st.text_input("Enter task to add:")
        if st.button("Add Task") and add_task:
            st.session_state.tasks.append(add_task)
            st.success(f"Task '{add_task}' has been successfully added.")

    elif operation == "Update":
        if st.session_state.tasks:
            update_task = st.selectbox("Select task to update:", st.session_state.tasks)
            new_task = st.text_input(f"Enter the new task for '{update_task}':")
            if st.button("Update Task") and new_task:
                idx = st.session_state.tasks.index(update_task)
                st.session_state.tasks[idx] = new_task
                st.success(f"Task '{update_task}' has been updated to '{new_task}'.")
        else:
            st.warning("There are no tasks to update.")

    elif operation == "Delete":
        if st.session_state.tasks:
            delete_task = st.selectbox("Select task to delete:", st.session_state.tasks)
            if st.button("Delete Task"):
                st.session_state.tasks.remove(delete_task)
                st.success(f"Task '{delete_task}' has been deleted.")
        else:
            st.warning("There are no tasks to delete.")

    elif operation == "View":
        st.subheader("Tasks List:")
        st.write(st.session_state.tasks)

    elif operation == "Exit":
        st.stop()

# Run the task management app
task_management()