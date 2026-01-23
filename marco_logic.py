import tkinter as tk
from tkinter import messagebox
import json
import os

# --- LOGIC & DATA (The Backend) ---
DB_FILE = "marco_db.json"

class ParkingSpot:
    def __init__(self, location_name, is_available=False):
        self.location = location_name
        self.is_available = is_available

def load_data():
    if not os.path.exists(DB_FILE):
        default_names = ["Boat Ramp", "Public Library", "Grocery Store", "The Old Dock", "Post Office"]
        return [ParkingSpot(name) for name in default_names]
    try:
        with open(DB_FILE, "r") as f:
            data = json.load(f)
        return [ParkingSpot(d["location"], d["is_available"]) for d in data]
    except:
        return load_data() # Fallback if file is corrupted

def save_data():
    data = [{"location": s.location, "is_available": s.is_available} for s in all_spots]
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

# --- THE VISUAL INTERFACE (The Frontend) ---
def toggle_spot(index):
    spot = all_spots[index]
   
    # Flip the status
    if spot.is_available:
        # If it's open, we are Claiming it (POLO)
        spot.is_available = False
        messagebox.showinfo("POLO!", f"You claimed the spot at:\n{spot.location}")
    else:
        # If it's taken, we are Leaving it (MARCO)
        spot.is_available = True
        messagebox.showinfo("MARCO!", f"You opened up the spot at:\n{spot.location}")
   
    save_data()
    refresh_display()

def refresh_display():
    # Clear old buttons
    for widget in frame_spots.winfo_children():
        widget.destroy()

    # Create new buttons based on data
    for i, spot in enumerate(all_spots):
        color = "#90EE90" if spot.is_available else "#FF7F7F" # Light Green or Light Red
        status_text = "OPEN (Click to Park)" if spot.is_available else "TAKEN (Click to Leave)"
       
        # Create the Card for this spot
        btn = tk.Button(frame_spots,
                        text=f"{spot.location}\n{status_text}",
                        bg=color,
                        font=("Arial", 12, "bold"),
                        height=3,
                        width=40,
                        command=lambda x=i: toggle_spot(x))
        btn.pack(pady=5)

# --- APP STARTUP ---
all_spots = load_data()

root = tk.Tk()
root.title("Marco Parking App")
root.geometry("400x600")

# Header
lbl_title = tk.Label(root, text="MARCO / POLO", font=("Helvetica", 20, "bold"))
lbl_title.pack(pady=20)

# Container for spots
frame_spots = tk.Frame(root)
frame_spots.pack(fill="both", expand=True)

# Initial Draw
refresh_display()

root.mainloop()

 
