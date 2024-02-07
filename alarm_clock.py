import tkinter as tk
from tkinter import ttk
import time
import winsound


class AlarmClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Alarm Clock")

        # Set up variables
        self.alarm_time_var = tk.StringVar()
        self.alarm_set = False

        # Create and pack widgets
        self.create_widgets()

    def create_widgets(self):
        # Logo
        logo_label = ttk.Label(self.root, text="🔔", font=("Arial", 40))
        logo_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Time entry
        time_label = ttk.Label(self.root, text="Set Alarm Time:")
        time_label.grid(row=1, column=0, pady=5)

        time_entry = ttk.Entry(self.root, textvariable=self.alarm_time_var, font=("Arial", 12), width=8)
        time_entry.grid(row=1, column=1, pady=5)

        # Set alarm button
        set_alarm_button = ttk.Button(self.root, text="Set Alarm", command=self.set_alarm)
        set_alarm_button.grid(row=2, column=0, columnspan=2, pady=10)

    def set_alarm(self):
        alarm_time_str = self.alarm_time_var.get()

        try:
            alarm_time = time.strptime(alarm_time_str, "%H:%M")
        except ValueError:
            tk.messagebox.showerror("Error", "Invalid time format. Please use HH:MM.")
            return

        current_time = time.localtime()
        current_time = current_time.tm_hour * 3600 + current_time.tm_min * 60

        alarm_time = alarm_time.tm_hour * 3600 + alarm_time.tm_min * 60

        if alarm_time < current_time:
            tk.messagebox.showwarning("Warning", "Invalid time. Please choose a future time.")
            return

        time_difference = alarm_time - current_time

        self.root.after(time_difference * 1000, self.play_alarm)
        self.alarm_set = True

        tk.messagebox.showinfo("Success", f"Alarm set for {alarm_time_str}")

    def play_alarm(self):
        if self.alarm_set:
            winsound.Beep(1000, 2000)  # Beep at 1000 Hz for 2 seconds
            tk.messagebox.showinfo("Alarm", "Time's up!")
            self.alarm_set = False


if __name__ == "__main__":
    root = tk.Tk()
    app = AlarmClockApp(root)
    root.mainloop()
