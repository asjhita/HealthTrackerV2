import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pandas as pd
from datetime import datetime
import os
import random

# Initialize data storage
DATA_PATH = "data/workouts.csv"
os.makedirs("data", exist_ok=True)

if not os.path.exists(DATA_PATH):
    df = pd.DataFrame(columns=['Date', 'Activity', 'Duration', 'Notes'])
    df.to_csv(DATA_PATH, index=False)

def load_data():
    return pd.read_csv(DATA_PATH)

def save_data(df):
    df.to_csv(DATA_PATH, index=False)

def log_workout():
    date = date_var.get()
    activity = activity_var.get()
    duration = duration_var.get()
    notes = notes_entry.get("1.0", tk.END).strip()

    df = load_data()
    new_entry = pd.DataFrame({
        'Date': [date],
        'Activity': [activity],
        'Duration': [duration],
        'Notes': [notes]
    })
    df = pd.concat([df, new_entry], ignore_index=True)
    save_data(df)
    messagebox.showinfo("Success", "Workout logged successfully!")
    refresh_data()

def refresh_data():
    df = load_data()
    for row in tree.get_children():
        tree.delete(row)
    for index, row in df.iterrows():
        tree.insert("", "end", values=(row['Date'], row['Activity'], row['Duration'], row['Notes']))

def export_data():
    df = load_data()
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if file_path:
        df.to_csv(file_path, index=False)
        messagebox.showinfo("Export", f"Data exported successfully to {file_path}")

# Tkinter GUI setup
root = tk.Tk()
root.title("Fitness Tracker")

main_frame = ttk.Frame(root, padding="10")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Log New Workout Section
log_frame = ttk.LabelFrame(main_frame, text="Log New Workout", padding="10")
log_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(log_frame, text="Date:").grid(row=0, column=0, sticky=tk.W)
date_var = tk.StringVar(value=datetime.now().strftime("%Y-%m-%d"))
date_entry = ttk.Entry(log_frame, textvariable=date_var)
date_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

ttk.Label(log_frame, text="Activity Type:").grid(row=1, column=0, sticky=tk.W)
activity_var = tk.StringVar()
activity_combobox = ttk.Combobox(log_frame, textvariable=activity_var)
activity_combobox['values'] = ["Running", "Walking", "Cycling", "Swimming", "Weight Training", "Yoga", "Other"]
activity_combobox.grid(row=1, column=1, sticky=(tk.W, tk.E))

ttk.Label(log_frame, text="Duration (minutes):").grid(row=2, column=0, sticky=tk.W)
duration_var = tk.IntVar(value=30)
duration_spinbox = ttk.Spinbox(log_frame, from_=1, textvariable=duration_var)
duration_spinbox.grid(row=2, column=1, sticky=(tk.W, tk.E))

ttk.Label(log_frame, text="Notes:").grid(row=3, column=0, sticky=tk.W)
notes_entry = tk.Text(log_frame, height=4, width=40)
notes_entry.grid(row=3, column=1, sticky=(tk.W, tk.E))

log_button = ttk.Button(log_frame, text="Log Workout", command=log_workout)
log_button.grid(row=4, column=0, columnspan=2, pady=10)

# Recent Workouts Section
recent_frame = ttk.LabelFrame(main_frame, text="Recent Workouts", padding="10")
recent_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

columns = ("Date", "Activity", "Duration", "Notes")
tree = ttk.Treeview(recent_frame, columns=columns, show='headings')
for col in columns:
    tree.heading(col, text=col)
tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Export Button
export_button = ttk.Button(main_frame, text="Export to CSV", command=export_data)
export_button.grid(row=2, column=0, pady=10)

# Refresh data on startup
refresh_data()

root.mainloop()