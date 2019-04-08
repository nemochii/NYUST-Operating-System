import json
import tkinter as tk
from tkinter import filedialog
from data import data_infor
from function import function

window = tk.Tk()
window.withdraw()
file_path = filedialog.askopenfilename(filetypes = [("JSON files", "*.json")])

with open(file_path, 'r') as f:
	jdata = json.load(f)

data_list = []
buf = []
for p in jdata:
	for d in jdata[p]:
		buf.append(jdata[p][d])
	data_list.append(data_infor(p, buf[0], buf[1], buf[2], buf[3]))
	buf.clear()

function(data_list, jdata)