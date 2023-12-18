import tkinter as tk
from tkinter import messagebox
import pandas as pd

def add_patient():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_entry.get()
    hospital_num = hospital_entry.get()
    department = department_entry.get()
    blood_group = blood_entry.get()

    patient = {
        'Name': name,
        'Age': age,
        'Gender': gender,
        'Admission Number': hospital_num,
        'Department': department,
        'Blood Group': blood_group
    }

    patients.append(patient)
    update_excel()
    messagebox.showinfo("Success", "Patient added successfully!")

    # Reset entry fields
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    gender_entry.delete(0, tk.END)
    hospital_entry.delete(0, tk.END)
    department_entry.delete(0, tk.END)
    blood_entry.delete(0, tk.END)

def update_excel():
    # Create a DataFrame from the patients list
    df = pd.DataFrame(patients)

    # Save the DataFrame to an Excel file
    df.to_excel(r"C:\Users\User\Desktop\patient_data.xlsx", index=False)

def view_patients():
    if not patients:
        messagebox.showinfo("Information", "No patients registered yet.")
    else:
        patient_list = "\n".join([
            f"Name: {patient['Name']}, Age: {patient['Age']}, Gender: {patient['Gender']}, Admission Number: {patient['Admission Number']}, Department: {patient['Department']}, Blood Group: {patient['Blood Group']}"
            for patient in patients
        ])
        messagebox.showinfo("List of Patients", patient_list)

def search_patient():
    search_name = search_entry.get().lower()
    found_patients = [
        patient for patient in patients if patient['Name'].lower() == search_name
    ]

    if not found_patients:
        messagebox.showinfo("Information", "No matching patients found.")
    else:
        patient_list = "\n".join([
            f"Name: {patient['Name']}, Age: {patient['Age']}, Gender: {patient['Gender']}, Admission Number: {patient['Admission Number']}, Department: {patient['Department']}, Blood Group: {patient['Blood Group']}"
            for patient in found_patients
        ])
        messagebox.showinfo("Matching Patients", patient_list)

# Create the main window
root = tk.Tk()
root.title("Patient Management System")
root.geometry("800x600")  # Set initial size of the window

# Add background canvas
background_canvas = tk.Canvas(root, bg='green', width=800, height=600)
background_canvas.pack(fill=tk.BOTH, expand=True)

# Add logo
logo_image = tk.PhotoImage(file=r"C:\Users\User\Desktop\Nitda.png")
logo_label = tk.Label(background_canvas, image=logo_image, bg='green')
logo_label.pack(pady=70)

# Create and initialize the patients list
patients = []

# Create and place widgets
tk.Label(background_canvas, text="Patient Management System", font=("Helvetica", 32, "bold"), bg='green', fg='white').pack()

tk.Label(background_canvas, text="Name:", bg='green', fg='white').pack()
name_entry = tk.Entry(background_canvas, width=40)  # Set the width to make the entry wider
name_entry.pack()

tk.Label(background_canvas, text="Age:", bg='green', fg='white').pack()
age_entry = tk.Entry(background_canvas, width=40)  # Set the width to make the entry wider
age_entry.pack()

tk.Label(background_canvas, text="Gender:", bg='green', fg='white').pack()
gender_entry = tk.Entry(background_canvas, width=40)  # Set the width to make the entry wider
gender_entry.pack()

tk.Label(background_canvas, text="Admission Number:", bg='green', fg='white').pack()
hospital_entry = tk.Entry(background_canvas, width=40)  # Set the width to make the entry wider
hospital_entry.pack()

tk.Label(background_canvas, text="Department:", bg='green', fg='white').pack()
department_entry = tk.Entry(background_canvas, width=40)  # Set the width to make the entry wider
department_entry.pack()

tk.Label(background_canvas, text="Blood Group:", bg='green', fg='white').pack()
blood_entry = tk.Entry(background_canvas, width=40)  # Set the width to make the entry wider
blood_entry.pack()

tk.Button(background_canvas, text="Add Patient", command=add_patient, bg="#4CAF50", fg="white").pack()  # Set button color
tk.Button(background_canvas, text="View Patients", command=view_patients, bg="#008CBA", fg="white").pack()  # Set button color
tk.Button(background_canvas, text="Search Patient", command=search_patient, bg="#FFD700").pack()  # Set button color

tk.Label(background_canvas, text="Enter patient's name to search:", bg='green', fg='white').pack()
search_entry = tk.Entry(background_canvas, width=40)  # Set the width to make the entry wider
search_entry.pack()

# Start the Tkinter event loop
root.mainloop()
