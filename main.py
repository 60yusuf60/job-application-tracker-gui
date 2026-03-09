import tkinter as tk
from tkinter import ttk,messagebox
import json
import os

def add_job(company_entry, position_entry, status_dropdown):
    company = company_entry.get()
    position = position_entry.get()
    status = status_dropdown.get()

    if not company or not position or not status:
        messagebox.showwarning("Missing Data","Please fill all required fields")
        return

    job = {
        "company": company,
        "position": position,
        "status": status
    }

    if os.path.exists("jobs.json"):
        with open("jobs.json","r") as f:
            jobs = json.load(f)

    else:
        jobs = []

    jobs.append(job)

    with open("jobs.json","w") as f:
        json.dump(jobs,f,indent=4)

    messagebox.showinfo("Success",f"Job at {company} has been added!")
    company_entry.delete(0, tk.END)
    position_entry.delete(0, tk.END)
    status_dropdown.set("")


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
    add_button = tk.Button(window,text="Add Application",
                           command=lambda: add_job(company_entry, position_entry, status_dropdown))
    add_button.pack(pady=10)

    window.mainloop()






if __name__ == "__main__":
    main()
