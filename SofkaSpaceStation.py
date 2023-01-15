import database as db
import ship_class as sp
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox

def cb_selection(*ComboboxSelected):
    """ Enables and disables GUI widgets depending on the value 
        of the type combobox"""
    lbl_load.grid_remove()
    spin_load.grid_remove()
    lbl_height.grid_remove()
    spin_height.grid_remove()
    lbl_power.grid_remove()
    spin_power.grid_remove()
    lbl_speed.grid_remove()
    spin_speed.grid_remove()
    lbl_capacity.grid_remove()
    spin_capacity.grid_remove()
    lbl_orbit.grid_remove()
    spin_orbit.grid_remove()

    clear_input_optional()

    if cb_type.get() == 'Shuttle':
        lbl_load.grid()
        spin_load.grid()
        lbl_height.grid()
        spin_height.grid()
        lbl_power.grid()
        spin_power.grid()

    elif cb_type.get() == 'Not Tripulated':
        lbl_speed.grid()
        spin_speed.grid()
    
    elif cb_type.get() == 'Tripulated':
        lbl_capacity.grid()
        spin_capacity.grid()
        lbl_orbit.grid()
        spin_orbit.grid()

def get_ship_values():
    """ Calls the get_values() method from ship_class
        returns a list with the values of the widgets"""
    ship = sp.SpaceShip
    ship.name = entry_name.get().upper()
    ship.type = cb_type.get().capitalize()
    ship.country = entry_country.get().capitalize()
    ship.year = int(spin_year.get())
    ship.active = active_state.get()
    ship.weight = int(spin_weight.get())
    ship.trust = int(spin_trust.get())
    ship.fuel = entry_fuel.get().capitalize()
    ship.function = entry_function.get('1.0', tk.END).strip().capitalize()

    ship.load_weight = int(spin_load.get())
    ship.height = int(spin_height.get())
    ship.power = int(spin_power.get())
    
    ship.speed = int(spin_speed.get())

    ship.capacity = int(spin_capacity.get())
    ship.orbit_height = int(spin_orbit.get())
    return sp.get_values(ship)

def add_ship():
    """Add a ship with the values from get_ship_values() to the database"""
    if entry_name.get() != '':
        db.insert_ship(db.db_file, get_ship_values())
    else:
        messagebox.showinfo('Error','"Name" field cannot be Null')

def filter_db():
    """ Filter DB data and displays it"""
    curr_values = get_ship_values()
    tree.delete(*tree.get_children())
    value_ref = ['name', 'type', 'country', 'year', 'active', 'weight', 'trust',
                'fuel', 'function', 'load_weight', 'height', 'power', 'speed', 
                'capacity', 'orbit_height']
    filter_query = """SELECT * FROM ship"""
    flag_start = 0
    for i in range(0,len(curr_values)):
        if curr_values[i] == '' or curr_values[i] == 0:
            pass
        else:
            if flag_start != 0:
                filter_query += ' AND'
            else:
                filter_query += ' WHERE'
            flag_start = 1
            if i in [3,5,6]:
                filter_query += " {} == {}".format(value_ref[i],
                                                 curr_values[i])
            else:
                filter_query += " {} == '{}'".format(value_ref[i],
                                                 curr_values[i])
    # print(filter_query)

    con1 = db.create_connection(db.db_file)
    cur1 = con1.cursor()
    cur1.execute(filter_query)
    rows = cur1.fetchall()
    for row in rows:
        tree.insert("", tk.END, values=row)
    con1.close()

def display_db():
    """Display full DB"""
    tree.delete(*tree.get_children())
    con1 = db.create_connection(db.db_file)
    cur1 = con1.cursor()
    cur1.execute("SELECT * FROM ship")
    rows = cur1.fetchall()
    for row in rows:
        tree.insert("", tk.END, values=row)
    con1.close()

def clear_input_optional():
    """ Clears optional widgets values"""
    try:
        spin_load.set(0)
        spin_height.set(0)
        spin_power.set(0)
        spin_speed.set(0)
        spin_capacity.set(0)
        spin_orbit.set(0)
    except:
        pass 

def clear_input():
    """ Clears basic widgets values"""
    try:
        entry_name.delete(0,'end')
        cb_type.set('')
        entry_country.delete(0,'end')
        spin_year.set(0)
        active_state.set(False)
        spin_weight.set(0)
        spin_trust.set(0)
        entry_fuel.delete(0,'end')
        entry_function.delete('1.0','end')
        clear_input_optional()
        tree.delete(*tree.get_children())
    except:
        pass

# Root Window
root = tk.Tk()
root.title('Sofka Space Station')
root.geometry('1150x480')

# Paned frames
p = ttk.Panedwindow(root, orient='vertical', width=1130, height=470)
f1 = ttk.Labelframe(p, text='Data', width=1130, height=300, borderwidth=5)
f2 = ttk.Labelframe(p, text='Database', width=1130, height=200, borderwidth=5)
p.add(f1)
p.add(f2)

# Name
lbl_name = ttk.Label(f1, text='Name:')
lbl_name.grid(column=0, row=0, sticky=tk.NW)

entry_name = ttk.Entry(f1,width=23, state='enabled')
entry_name.grid(column=1, row=0, sticky=tk.NW)
entry_name.focus()

# Type
lbl_type = ttk.Label(f1, text='Type:')
lbl_type.grid(column=0, row=1, sticky=tk.NW)

var_cb = tk.StringVar()
cb_type = ttk.Combobox(f1, text='Test containter', 
                        width=20, textvariable=var_cb)
cb_type['values'] = ('',
                    'Basic',
                    'Shuttle', 
                    'Not Tripulated', 
                    'Tripulated')
cb_type['state']='readonly'
cb_type.current(0)
cb_type.bind('<<ComboboxSelected>>', cb_selection)
cb_type.grid(column=1, row=1, sticky=tk.NW)

# Country
lbl_country = ttk.Label(f1, text='Country:')
lbl_country.grid(column=0, row=2, sticky=tk.NW)

entry_country = ttk.Entry(f1,width=23, state='enabled')
entry_country.grid(column=1, row=2, sticky=tk.NW)

# Year
lbl_year = ttk.Label(f1, text='Year:')
lbl_year.grid(column=0, row=3, sticky=tk.NW)

year = tk.IntVar()
# year.set(0)
spin_year = ttk.Spinbox(f1, from_=0, to=999999, width=5, textvariable=year)
spin_year.grid(column=1,row=3, sticky=tk.NW)

# Active
lbl_active = ttk.Label(f1, text='Active:')
lbl_active.grid(column=0, row=4, sticky=tk.NW)

active_state = tk.StringVar()
# active_state.set(False)
cb_active = ttk.Combobox(f1, text='Test containter', 
                        width=20, textvariable=active_state)
cb_active['values'] = ('',
                    'Active',
                    'Inactive')
cb_active['state']='readonly'
cb_active.current(0)
cb_active.grid(column=1, row=4, sticky=tk.NW)

# Weight
lbl_weight = ttk.Label(f1, text='Weight:')
lbl_weight.grid(column=2, row=0, sticky=tk.NW)

weight = tk.IntVar()
# weight.set(0)
spin_weight = ttk.Spinbox(f1, from_=0, to=999999, width=5, textvariable=weight)
spin_weight.grid(column=3,row=0, sticky=tk.NW)

# Trust
lbl_trust = ttk.Label(f1, text='Trust:')
lbl_trust.grid(column=2, row=1, sticky=tk.NW)

trust = tk.IntVar()
# trust.set(0)
spin_trust = ttk.Spinbox(f1, from_=0, to=999999, width=5, textvariable=trust)
spin_trust.grid(column=3,row=1, sticky=tk.NW)

# Fuel
lbl_fuel = ttk.Label(f1, text='Fuel:')
lbl_fuel.grid(column=2, row=2, sticky=tk.NW)

entry_fuel = ttk.Entry(f1,width=23, state='enabled')
entry_fuel.grid(column=3, row=2, sticky=tk.NW)

# Function
lbl_function = ttk.Label(f1, text='Function:')
lbl_function.grid(column=2, row=3, sticky=tk.NW)

entry_function = scrolledtext.ScrolledText(f1, 
                                            width=23,  
                                            height=2)
entry_function.grid(column=3, row=3, sticky=tk.NW, rowspan=2)

# Load
lbl_load = ttk.Label(f1, text='Load:')
lbl_load.grid(column=4, row=0, sticky=tk.NW)

load = tk.IntVar()
spin_load = ttk.Spinbox(f1, from_=0, to=999999, width=5, textvariable=load)
spin_load.grid(column=5,row=0, sticky=tk.NW)

# Height
lbl_height = ttk.Label(f1, text='Height:')
lbl_height.grid(column=4, row=1, sticky=tk.NW)

height = tk.IntVar()
# height.set(0)
spin_height = ttk.Spinbox(f1, from_=0, to=999999, width=5, textvariable=height)
spin_height.grid(column=5,row=1, sticky=tk.NW)

# Power
lbl_power = ttk.Label(f1, text='Power:')
lbl_power.grid(column=4, row=2, sticky=tk.NW)

power = tk.IntVar()
# power.set(0)
spin_power = ttk.Spinbox(f1, from_=0, to=999999, width=5, textvariable=power)
spin_power.grid(column=5,row=2, sticky=tk.NW)

# Speed
lbl_speed = ttk.Label(f1, text='Speed:')
lbl_speed.grid(column=4, row=0, sticky=tk.NW)

speed = tk.IntVar()
# speed.set(0)
spin_speed = ttk.Spinbox(f1, from_=0, to=999999, width=5, textvariable=speed)
spin_speed.grid(column=5,row=0, sticky=tk.NW)

# Capacity
lbl_capacity = ttk.Label(f1, text='Capacity:')
lbl_capacity.grid(column=4, row=0, sticky=tk.NW)

capacity = tk.IntVar()
# capacity.set(0)
spin_capacity = ttk.Spinbox(f1, from_=0, to=999999, width=5, 
                            textvariable=capacity)
spin_capacity.grid(column=5,row=0, sticky=tk.NW)

# Orbit
lbl_orbit = ttk.Label(f1, text='Orbit:')
lbl_orbit.grid(column=4, row=1, sticky=tk.NW)

orbit = tk.IntVar()
# height.set(0)
spin_orbit = ttk.Spinbox(f1, from_=0, to=999999, width=5, textvariable=orbit)
spin_orbit.grid(column=5,row=1, sticky=tk.NW)

# Add button
btn_add = tk.Button(f1, text="Add", command=lambda : add_ship())
btn_add.grid(column=6, row=0, pady=10)

# Filter button
btn_filter = tk.Button(f1, text="Filter", 
                command=lambda : filter_db())
btn_filter.grid(column=6, row=1, pady=10)

# Clear button
btn_clear = tk.Button(f1, text="Clear", command=lambda : clear_input())
btn_clear.grid(column=6, row=2, pady=10)

# DataBase Display
column_width = 150
tree = ttk.Treeview(f2, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7", 
                                "c8", "c9", "c10", "c11", "c12", "c13", 
                                "c14", "c15"), show='headings',
                                selectmode='browse' )
tree.column("#1", anchor=tk.CENTER, width=120)
tree.heading("#1", text="Name")
tree.column("#2", anchor=tk.CENTER, width=75)
tree.heading("#2", text="Type")
tree.column("#3", anchor=tk.CENTER, width=100)
tree.heading("#3", text="Country")
tree.column("#4", anchor=tk.CENTER, width=50)
tree.heading("#4", text="Year")
tree.column("#5", anchor=tk.CENTER, width=50)
tree.heading("#5", text="Active")
tree.column("#6", anchor=tk.CENTER, width=50)
tree.heading("#6", text="Weight")
tree.column("#7", anchor=tk.CENTER, width=50)
tree.heading("#7", text="Trust")
tree.column("#8", anchor=tk.CENTER, width=column_width)
tree.heading("#8", text="Fuel")
tree.column("#9", anchor=tk.CENTER, width=column_width)
tree.heading("#9", text="Function")
tree.column("#10", anchor=tk.CENTER, width=50)
tree.heading("#10", text="Load")
tree.column("#11", anchor=tk.CENTER, width=50)
tree.heading("#11", text="Height")
tree.column("#12", anchor=tk.CENTER, width=50)
tree.heading("#12", text="Power")
tree.column("#13", anchor=tk.CENTER, width=50)
tree.heading("#13", text="Speed")
tree.column("#14", anchor=tk.CENTER, width=60)
tree.heading("#14", text="Capacity")
tree.column("#15", anchor=tk.CENTER, width=50)
tree.heading("#15", text="Orbit")
tree.grid(column=0, row=0, padx=10)

# Display all button
btn_display_db = tk.Button(f2, text="Display all DB", 
                command=lambda : display_db())
btn_display_db.grid(column=0, row=1, pady=10)

for widget in f1.winfo_children():
    widget.grid(padx=3, pady=3)

p.grid(column=0, row=0, padx=5)

def main():
    db.main()
    cb_selection()
    root.mainloop()

if __name__ == '__main__':
    main()