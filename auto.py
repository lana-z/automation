import os
import shutil

#shutil stands for shell utilities

def create_folder(folder_name):

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"Your new folder {folder_name} is ready to use. 🗂️")

    else: 
        print(f"A folder {folder_name} already exists. ")

create_folder("test_folder")

def delete_user(user, temp):
    # is folder there?
    if not os.path.exists(user):
        print(f"Your folder {user} doesn't seem to exist. Check the user name and try again.")
        return

    if os.path.exists(user):
        
        create_folder(temp)

        for file in os.listdir(user):
            moving_from = os.path.join(user, file)
            moving_to = os.path.join(temp, file)
            shutil.move(moving_from, moving_to)
            print(f"{file} has been moved to {temp} and the user is deleted.👋 Bye {user}.")


        os.rmdir(temp)
        print(f"Your folder {user} has been deleted and folder {temp} containing the deleted user files has been created. 🗂️")

    else:
        print(f"Your folder {folder_name} does not exist. ")
    
delete_user("test_folder", "temp_folder")