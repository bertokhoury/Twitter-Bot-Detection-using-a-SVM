from tkinter import *
from tkinter import filedialog

#Initialize Tkinter
root = Tk()
root.title("Twitter Bot Detector")

#GUI functions for buttons, etc.
def output(string):
    output_text.config(state=NORMAL)
    output_text.insert(END, string + "\n")
    output_text.config(state=DISABLED)

def browsecsvfile():
    return filedialog.askopenfilename(
        initialdir="/",
        title="Select file",
        filetypes=(("CSV files", "*.csv"), ("All files", "*.*")))

def browsedir():
    return filedialog.askdirectory()

#Commands
def handle_test():
    output("Starting test with handle: " + handle.get())
    pass

def csv_test():
    output("Starting test with CSV data at: " + csv_file.get())
    pass

def rept_tick():
    if save_rept.get() > 0:
        output("Report tickbox checked")
    else:
        output("Report tickbox unchecked")
    
def csv_browse():
    file = browsecsvfile()
    csv_file.set(file)
    output("Set CSV file location")

def rept_browse():
    directory = browsedir()
    rept_dir.set(directory)
    output("Set report output directory")
    
#Create layout
#Window frame
frame = Frame(root, padx=5, pady=5)
frame.grid(row=0, column=0, sticky=N+S+E+W)
Grid.columnconfigure(root, 0, weight=1)
Grid.rowconfigure(root, 0, weight=1)

#Configure window frame grid
for x in range(2):
    Grid.columnconfigure(frame, x, weight=1)
Grid.rowconfigure(frame, 8, weight=1)

#Handle field
handle = StringVar()
handle_lbl = Label(frame, text="Twitter user handle:")
handle_entry = Entry(frame, textvariable=handle)
handle_lbl.grid(row=0, column=0, sticky=W)
handle_entry.grid(row=1, column=0, sticky=W+E)
##Handle button subfield
handle_btn_frame = Frame(frame, padx=5)
handle_test_btn = Button(handle_btn_frame, text = "Test", command=handle_test, padx=5)
handle_btn_frame.grid(row=1, column=1, sticky=W+E)
handle_test_btn.grid(row=0, column=0, padx=5)

#CSV field
csv_file = StringVar()
csv_lbl = Label(frame, text="CSV file (multi-user):")
csv_entry = Entry(frame, textvariable=csv_file)
csv_lbl.grid(row=2, column=0, sticky=W)
csv_entry.grid(row=3, column=0, sticky=W+E)
##CSV button subfield
csv_btn_frame = Frame(frame, padx=5)
csv_test_btn = Button(csv_btn_frame, text = "Test", command=csv_test, padx=5)
csv_browse_btn = Button(csv_btn_frame, text = "Browse...", command=csv_browse, padx=5)
csv_btn_frame.grid(row=3, column=1, sticky=W+E)
csv_test_btn.grid(row=0, column=0, padx=5)
csv_browse_btn.grid(row=0, column=1, padx=5)

#Report field
rept_dir = StringVar()
save_rept = IntVar()
rept_tick = Checkbutton(frame, anchor=E, text = "Save report to file", command=rept_tick, variable=save_rept)
rept_label = Label(frame, text="Report file destination folder:")
rept_entry = Entry(frame, textvariable=rept_dir)
rept_tick.grid(row=4, column=0, sticky=W)
rept_label.grid(row=5, column=0, sticky=W)
rept_entry.grid(row=6, column=0, sticky=W+E)
#Report button subfield
rept_btn_frame = Frame(frame, padx=5)
rept_browse_btn = Button(rept_btn_frame, text = "Browse...", command=rept_browse, padx=5)
rept_btn_frame.grid(row=6, column=1, sticky=W+E)
rept_browse_btn.grid(row=0, column=0, padx=5)

#Output field
output_label = Label(frame, text="Output log:")
output_text = Text(frame, height=3, width=60, state=DISABLED)
output_label.grid(row=7, column=0, sticky=W)
output_text.grid(row=8, column=0, columnspan=2, sticky=N+E+S+W)

#Run once everything is initialized
root.mainloop()

