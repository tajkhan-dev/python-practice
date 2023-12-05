# Initialize an empty list to store tasks
myTodos = []

# Boolean variable to control the while loop
check = True

# Initialize a global variable 'info' with an empty string
info = " "

# Define a function to add tasks to the 'myTodos' list
def addTodos():
    # Declare 'info' as a global variable to modify it within the function
    global info  

    # Start an infinite loop controlled by the 'check' variable
    while check:
        # Check if the lowercase version of 'info' is "no"
        if info.lower() == "no":
            # Exit the loop if the user does not want to add more tasks
            break
        # Check if the lowercase version of 'info' is "yes"
        elif info.lower() == "yes":
            # Prompt the user to enter a task and add it to the list
            todo = input("Enter a task to do today: ")
            # Prompt the user to decide whether to add more items
            info = input("Do you want to add more items? ")
            # Append the entered task to the 'myTodos' list
            myTodos.append(todo)

    # Return the list of tasks after the user is done
    return myTodos

# Call the 'addTodos' function and store the result in 'data'
data = addTodos()

# Print the final list of tasks
print(data)
