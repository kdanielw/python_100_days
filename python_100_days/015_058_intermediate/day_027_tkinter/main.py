import tkinter

def mile_to_km():
    mile_value = float(mile_entry.get())
    km_value = mile_value * 1.609
    converted_km.config(text=f"{km_value}")

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

mile_entry = tkinter.Entry(width=10)
mile_entry.grid(row=0, column=1)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_to = tkinter.Label(text="is equal to")
is_equal_to.grid(row=1, column=0)

converted_km = tkinter.Label(text="0")
converted_km.grid(row=1, column=1)

km_label = tkinter.Label(text="Km")
km_label.grid(row=1, column=2)

calculate_button = tkinter.Button(text="Calculate", command=mile_to_km)
calculate_button.grid(row=2, column=1)

window.mainloop()
