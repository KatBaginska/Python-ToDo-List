from CRUD import add_task, show_task, edit_task, delete_task, show_undone, mark_done

def menu():
    while True:
        print('Welcome to To-Do Today')
        print('----------------------')
        print('1. Display Exsting Tasks')
        print('2. Add new task')
        print('3. Edit Existing Task')
        print('4. Remove Task')
        print('5. Show only undone tasks')
        print('6. Mark task as done')
        print('7. Exit')
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
        elif option_number == '5':
            show_undone()
            input("\nPress Enter to return to menu...")
        elif option_number == '6':
            mark_done()
        elif option_number == '7':
            print('Goodbye!')
            break
        else:
            print ('Invalid Chice')
menu()