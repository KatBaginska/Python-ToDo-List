from store import load_task, save_task
from datetime import datetime

def add_task():
    tasks = load_task()
    task_title = input('Please Input Task Name: ')
    while True:
        task_status = input('Is the task done already?(y/n) ')
        task_status = task_status.lower()
        if task_status == 'y':
            status = True
            break
        elif task_status == 'n':
            status = False
            break
        else:
            print('Incorrect Value')
    while True:
            task_deadline = input('When you want to do it by? DD-MM-YYYY ')

            try:#AI Suggestion
                deadline_date = datetime.strptime(task_deadline, "%d-%m-%Y")
                today = datetime.today()

                deadline_date = deadline_date.date() #stripping time
                today = today.date()

                if deadline_date< today:
                    print('Deadline cannot be in the past. Please input valid date.')
                else:
                    break
            except ValueError:
                print("Invalid date format. Please use DD-MM-YYYY.")
    task = {
        "title": task_title,
        "status": status,
        "deadline": task_deadline
    }
    tasks.append(task)
    tasks.sort(key=lambda task:datetime.strptime(task["deadline"], "%d-%m-%Y")) #AI Help
    save_task(tasks)

    input("\nPress Enter to return to menu...")
def show_task():
    tasks = load_task()
    if not tasks:
        print('You have no tasks on your list')
    else:
        for index, task in enumerate(tasks):
           
           if task["status"]:
            print(index+1, '[x]', task["title"], '- Due:', task["deadline"])
           else:
            print(index+1, '[ ]', task["title"], '- Due:', task["deadline"])

def delete_task():
    tasks = load_task()
    
    if not tasks:
        print('Not tasks on your list')
        print('\nPress Enter to return to menu...')

    show_task()

    while True:
       del_input = input('Choose a number associated to the task you want to delete: ')

       if not del_input.isdigit():
           print('No To-Do with this number. Please enter valid To-Do number')
           continue
       
       del_number = int(del_input)

       if del_number < 1 or del_number > len(tasks):
            print('No To-Do with this number, try again: ')
            continue
       break

    deleted_task = tasks.pop(del_number - 1)
    save_task(tasks)

    print(f'Task {deleted_task['title']} has been deleted!')
    input('\nPress Enter to return to menu...')
       
def edit_task():
    tasks = load_task()

    if not tasks:
      print('No tasks on your To-Do List')
      return
   
    show_task()

    while True:
        user_task = input("Enter number assiociated to the To-Do you want to edit: ")

        if not user_task.isdigit(): #AI Suggestion
           print("Please enter valid To-Do number: ")
           continue

        task_number = int(user_task)

        if task_number < 1 or task_number > len(tasks):
            print('There is no task with this number, try again')
            continue
        break

    py_number = tasks[task_number - 1]
    print("You selected:", py_number["title"])

    while True:
        user_input = input('Which part of To-Do you want to change? Title, status or Deadline: ')
        user_input = user_input.lower()

        if user_input in ["title", "status", "deadline"]:
           break
        else:
           print("Invalid choice. Please provide valid title, status or deadline.")
           continue
    if user_input == 'title':
        while True:
            new_title = input('Please add new title: ').strip() #removes spaces

            if new_title == "":
                print("Title cannot be empty, input title: ")
                continue
            else:
                py_number["title"] = new_title
                break
    elif user_input == 'status':
        while True:
            new_status = input('Is to-do completed? y/n')
            new_status = new_status.lower()

            if new_status == 'y':
                py_number["status"] = True
                break
            elif new_status == 'n':
                py_number["status"] = False
                break
            else:
                print('Incorrect Status')
    elif user_input == 'deadline':
        while True:
            new_deadline = input('What is new deadline? DD-MM-YYYY?')

            try:#AI Suggestion
                deadline_date = datetime.strptime(new_deadline, "%d-%m-%Y")
                today = datetime.today()

                deadline_date = deadline_date.date() #stripping time
                today = today.date()

                if deadline_date< today:
                    print('Deadline cannot be in the past. Please input valid date.')
                else:
                    py_number["deadline"] = new_deadline
                    break
            except ValueError:
                print("Invalid date format. Please use DD-MM-YYYY.")
    
    tasks.sort(key=lambda task:datetime.strptime(task["deadline"], "%d-%m-%Y"))
    save_task(tasks)
    input("\nChanges has been succesful. Press Enter to return to menu...")

