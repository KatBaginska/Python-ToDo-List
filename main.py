from CRUD import add_task, show_task, edit_task, delete_task

def menu():
    while True:
        print('Welcome to To-Do Today')
        print('----------------------')
        print('1. Display Exsting Tasks')
        print('2. Add new task')
        print('3. Edit Existing Task')
        print('4. Remove Task')
        print('----------------------')

        option_number = input('Choose number for one of the options:')

        if option_number == '1':
            show_task()
            input("\nPress Enter to return to menu...")
        elif option_number == '2':
            add_task()
        elif option_number== '3':
            edit_task()
        elif option_number == '4':
            delete_task()
        else:
            print ('Invalid Chice')
menu()