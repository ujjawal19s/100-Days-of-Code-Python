from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

# Labels
miles = Label(text="Miles", font=("Arial", 14, "normal"))
miles.grid(row=0, column=2)

km = Label(text="Km", font=("Arial", 14, "normal"))
km.grid(row=1, column=2)

km_value = Label(text="0", font=("Arial", 14, "normal"))
km_value.grid(row=1, column=1)

is_equal_to = Label(text="is equal to", font=("Arial", 14, "normal"))
is_equal_to.grid(row=1, column=0)


# Buttons
def action():
    miles_value = float(entry.get())
    result = round(miles_value * 1.6, 2)
    km_value.config(text=result)


button = Button(width=15, text="Calculate", command=action)
button.grid(row=2, column=1)

# Entry
entry = Entry(width=15)

entry.grid(row=0, column=1)

window.mainloop()
