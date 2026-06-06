"""
Digital Clock Application
Displays current time in multiple time zones with a clean UI.
"""

import tkinter as tk
from tkinter import font
from datetime import datetime
import pytz
from threading import Thread
import time


class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Clock - Multiple Time Zones")
        self.root.geometry("900x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e1e")
        
        # Define time zones to display
        self.time_zones = [
            ("UTC", "UTC"),
            ("New York", "America/New_York"),
            ("London", "Europe/London"),
            ("Tokyo", "Asia/Tokyo"),
            ("Sydney", "Australia/Sydney"),
            ("Dubai", "Asia/Dubai"),
        ]
        
        # Create main frame
        self.main_frame = tk.Frame(root, bg="#1e1e1e")
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title_font = font.Font(family="Helvetica", size=24, weight="bold")
        title_label = tk.Label(
            self.main_frame,
            text="🕐 Digital Clock",
            font=title_font,
            bg="#1e1e1e",
            fg="#00ff00"
        )
        title_label.pack(pady=(0, 20))
        
        # Create frames for each time zone
        self.clock_frames = {}
        self.time_labels = {}
        self.date_labels = {}
        
        # Create a grid layout
        grid_frame = tk.Frame(self.main_frame, bg="#1e1e1e")
        grid_frame.pack(fill=tk.BOTH, expand=True)
        
        for idx, (city, tz) in enumerate(self.time_zones):
            row = idx // 3
            col = idx % 3
            
            # Create frame for each timezone
            frame = tk.Frame(
                grid_frame,
                bg="#2d2d2d",
                relief=tk.RAISED,
                bd=2
            )
            frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
            
            # City name
            city_font = font.Font(family="Helvetica", size=12, weight="bold")
            city_label = tk.Label(
                frame,
                text=city,
                font=city_font,
                bg="#2d2d2d",
                fg="#00ffff"
            )
            city_label.pack(pady=(10, 5))
            
            # Time display
            time_font = font.Font(family="Courier", size=28, weight="bold")
            time_label = tk.Label(
                frame,
                text="00:00:00",
                font=time_font,
                bg="#2d2d2d",
                fg="#00ff00"
            )
            time_label.pack(pady=10)
            
            # Date display
            date_font = font.Font(family="Helvetica", size=10)
            date_label = tk.Label(
                frame,
                text="",
                font=date_font,
                bg="#2d2d2d",
                fg="#ffff00"
            )
            date_label.pack(pady=(0, 10))
            
            # Store references
            self.clock_frames[tz] = frame
            self.time_labels[tz] = time_label
            self.date_labels[tz] = date_label
        
        # Configure grid weights
        for i in range(2):
            grid_frame.grid_rowconfigure(i, weight=1)
        for i in range(3):
            grid_frame.grid_columnconfigure(i, weight=1)
        
        # Start clock update thread
        self.running = True
        self.update_clock()
    
    def update_clock(self):
        """Update the clock display with current times"""
        if not self.running:
            return
        
        try:
            for city, tz in self.time_zones:
                # Get current time in timezone
                tz_obj = pytz.timezone(tz)
                current_time = datetime.now(tz_obj)
                
                # Format time and date
                time_str = current_time.strftime("%H:%M:%S")
                date_str = current_time.strftime("%a, %b %d, %Y")
                
                # Update labels
                self.time_labels[tz].config(text=time_str)
                self.date_labels[tz].config(text=date_str)
        
        except Exception as e:
            print(f"Error updating clock: {e}")
        
        # Schedule next update
        self.root.after(1000, self.update_clock)
    
    def on_closing(self):
        """Handle window closing"""
        self.running = False
        self.root.destroy()


def main():
    root = tk.Tk()
    clock = DigitalClock(root)
    root.protocol("WM_DELETE_WINDOW", clock.on_closing)
    root.mainloop()


if __name__ == "__main__":
    main()
