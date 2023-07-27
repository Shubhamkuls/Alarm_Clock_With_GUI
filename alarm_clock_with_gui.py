import tkinter as tk
from tkinter import messagebox
import time
import winsound

def set_alarm():
    alarm_time = entry.get()
    try:
        alarm_h, alarm_m = map(int, alarm_time.split(":"))
        if not (0 <= alarm_h < 24 and 0 <= alarm_m < 60):
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Invalid time format. Please use HH:MM (24-hour format).")
        return

    while True:
        current_time = time.strftime("%H:%M")
        if current_time == alarm_time:
            messagebox.showinfo("Alarm", "Time's up! Wake up!")
            winsound.Beep(1000, 2000)  # Beep for 2 seconds (optional sound effect)
            break
        time.sleep(1)

# Create the main application window
app = tk.Tk()
app.title("Alarm Clock")

# Label
label = tk.Label(app, text="Enter alarm time (HH:MM):")
label.pack(pady=10)

# Entry for alarm time
entry = tk.Entry(app, font=("Arial", 18))
entry.pack(pady=10)

# Button to set the alarm
set_button = tk.Button(app, text="Set Alarm", command=set_alarm)
set_button.pack(pady=20)

# Run the main loop
app.mainloop()