import tkinter as tk
from tkinter import ttk,messagebox
import json
import os

def add_job(name_entry, company_entry, position_entry, status_dropdown):
    name = name_entry.get()
    company = company_entry.get()
    position = position_entry.get()
    status = status_dropdown.get()

    if not name or not company or not position or not status:
        messagebox.showwarning("Missing Data","Please fill all required fields")
        return

    job = {
        "name": name,
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
    name_entry.delete(0, tk.END)
    company_entry.delete(0, tk.END)
    position_entry.delete(0, tk.END)
    status_dropdown.set("")


def list_jobs():
    if not os.path.exists("jobs.json"):
        messagebox.showinfo("No Jobs", "No job applications found.")
        return

    with open("jobs.json","r") as f:
        jobs = json.load(f)

    if not jobs:
        messagebox.showinfo("No Jobs", "No job applications found.")
        return


    list_window = tk.Toplevel()
    list_window.title("Job Applications")
    list_window.geometry("400x300")

    for job in jobs:
        name = job.get("name", "")  # Eğer name yoksa boş string
        company = job.get("company", "")
        position = job.get("position", "")
        status = job.get("status", "")
        tk.Label(list_window,
                 text=f"Name: {name}, Company: {company}, Position: {position}, Status: {status}").pack(pady=2)

def main():
    window = tk.Tk()
    window.title("Job Application Tracker")
    window.geometry("500x400")

    label = tk.Label(window, text="Job Application Tracker" , font=("Arial Bold", 16))
    label.pack(pady=20)

    # Name
    name_label = tk.Label(window, text="Name")
    name_label.pack()
    name_entry = tk.Entry(window)
    name_entry.pack()


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

    # Add Application Button
    add_button = tk.Button(window, text="Add Application",
                           command=lambda: add_job(name_entry, company_entry, position_entry, status_dropdown))
    add_button.pack(pady=10)


    # List Applications Button
    list_button = tk.Button(window, text="List Applications", command=list_jobs)
    list_button.pack(pady=10)

    window.mainloop()




if __name__ == "__main__":
    main()
