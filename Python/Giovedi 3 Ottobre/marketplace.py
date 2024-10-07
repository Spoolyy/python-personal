from data import administrators, users

users.account_procedure()

if users.userOne['is_admin'] == True: # Dictates menu choices for administrators
    administrators.admin_menu()
else: # Dictates menu choices for basic users
    users.user_menu()