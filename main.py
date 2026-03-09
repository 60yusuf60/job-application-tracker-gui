import tkinter as tk
from tkinter import ttk

def main():
    window = tk.Tk()
    window.title("Job Application Tracker")
    window.geometry("500x400")

    label = tk.Label(window, text="Job Application Tracker" , font=("Arial Bold", 16))
    label.pack(pady=20)

    # Company
    company_label = tk.Label(window, text="Company")
    company_label.pack()


    company_entry = tk.Entry(window)
    company_entry.pack()

    # Position
    position_label = tk.Label(window, text="Position")
    position_label.pack()


    position_entry = tk.Entry(window)
    position_entry.pack()

    # Status
    status_label = tk.Label(window, text="Status")
    status_label.pack()

    status_options = ["Applied", "Interview", "Offer", "Rejected"]
    status_dropdown = ttk.Combobox(window, values=status_options)
    status_dropdown.pack()

    # Button
    add_button = tk.Button(window,text="Add Application")
    add_button.pack(pady=10)

    window.mainloop()






if __name__ == "__main__":
    main()
