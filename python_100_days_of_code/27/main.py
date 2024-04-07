import tkinter as tk 

window = tk.Tk()
window.title(f"Mile to Km Convertor")
window.minsize(width=100, height=100)

def convert_mile_to_km():
    miles = box_entry.get() or 0
    output_kms['text'] = str(1.5 * int(miles))

frame = tk.Frame(master=window)
frame.pack()

box_entry = tk.Entry(master=frame)
box_entry.pack()
btn_calculate = tk.Button(master=frame, text='Calculate', command=convert_mile_to_km)
btn_calculate.pack()
label_miles = tk.Label(master=frame, text="Miles")
label_miles.pack()
label_kms = tk.Label(master=frame, text="Kms")
label_kms.pack()

# Output 
output_kms = tk.Label(master=frame, text="0.0")
output_kms.pack()

if __name__ == "__main__":
    window.mainloop()