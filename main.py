import json
import tkinter as tk
from tkinter import ttk

# Load your JSON data from a file
with open('teas.json') as f:
    data = json.load(f)

def search_by_name(name):
    for tea in data:
        if tea['Tea Name'].lower() == name.lower():
            return tea
    return None

def search_by_good_to(category):
    teas = [tea for tea in data if category in tea['Good To']]
    teas.sort(key=lambda tea: tea['Good To'][category], reverse=True)
    return teas

def search():
    search_term = search_entry.get()
    search_type = search_type_var.get()
    result.delete(1.0, tk.END)
    if search_type == 'Tea Name':
        tea = search_by_name(search_term)
        if tea:
            result.insert(tk.END, json.dumps(tea, indent=4))
        else:
            result.insert(tk.END, 'No tea found with that name.')
    else:
        teas = search_by_good_to(search_term)
        if teas:
            for tea in teas:
                result.insert(tk.END, json.dumps(tea, indent=4) + '\n\n')
        else:
            result.insert(tk.END, 'No tea found good for that category.')

root = tk.Tk()
root.title('Tea Search')

search_type_var = tk.StringVar(value='Tea Name')
search_type = ttk.Combobox(root, textvariable=search_type_var)
search_type['values'] = ('Tea Name', 'Good To')
search_type.grid(column=0, row=0)

search_entry = ttk.Entry(root)
search_entry.grid(column=1, row=0)

search_button = ttk.Button(root, text='Search', command=search)
search_button.grid(column=2, row=0)

result = tk.Text(root)
result.grid(column=0, row=1, columnspan=3)

root.mainloop()
