import tkinter
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x400")

next = tkinter.Frame(root)



def intro_page():
    next.pack(fill='both', expand=1)
    frame.pack_forget()


    
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Wallpaper++", text_font=("Roboto", 24))
label.pack(pady=12, padx=10)

label2 = customtkinter.CTkLabel(master=frame, text="The future of wallpapers", text_font=("Roboto", 12))
label2.pack(pady=5, padx=10)

button = customtkinter.CTkButton(master=frame, text="Get started", command=intro_page)
button.pack(pady=60, padx=10)

root.mainloop()
