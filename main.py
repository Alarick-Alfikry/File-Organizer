import os, shutil, customtkinter
from tkinter import *
from tkinter import messagebox #Idk why the code still need this even though I previously imported * from ktinter ('^' ?)

# Initialize Tkinter
root = Tk()
root.title("File Organizer")
root.iconbitmap("icon.ico")
root.geometry("800x500")
root.resizable(False, False)

bg = PhotoImage(file="background.png")
bg_label = Label(root, image=bg)
bg_label.place(x=0, y=0)

# The function that will be executed when the button is clicked
def organize_files():
    # Gets the value from the input box
    path = entry.get()
    
    if not os.path.exists(path):
        messagebox.showerror("Error", "Path is invalid")
    else:
        files = os.listdir(path)

        for item in files:
            try:
                filename, extension = os.path.splitext(item)
                extension = extension[1:]

                if os.path.exists(os.path.join(path, extension)):
                    shutil.move(os.path.join(path, item), os.path.join(path, extension, item))
                else:
                    os.makedirs(os.path.join(path, extension))
                    shutil.move(os.path.join(path, item), os.path.join(path, extension, item))

            except FileNotFoundError:
                messagebox.showerror("Error", "File not found")
            except Exception as e:
                messagebox.showerror("Error", f"Error: {e}")

        messagebox.showinfo("Success", "Files organized successfully")

# Create an input box (Entry)
entry = customtkinter.CTkEntry(root, 
        placeholder_text= "Enter Folder Path Here",
        font= ("Helvetica", 20),
        height= 44,
        width= 354,
        fg_color= "#EDEAD4",
        bg_color= "#DAD5A9",
        text_color= "#888888",
        corner_radius= 30)
entry.place(x=44, y=284)

# Create a button to trigger the organize files function
button = customtkinter.CTkButton(root, 
        text= "Organize",
        font= ("Helvetica", 20),
        height= 44,
        width= 170,
        fg_color= "#FF5678",
        bg_color= "#DAD5A9",
        hover_color= "#B70025",
        corner_radius= 30,
        command= organize_files)
button.place(x=136, y=343)

root.mainloop()