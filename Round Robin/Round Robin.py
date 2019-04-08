import json
import copy
import tkinter as tk
from tkinter import filedialog

window = tk.Tk()
window.withdraw()
file_path = filedialog.askopenfilename(filetypes = [("JSON files", "*.json")])

with open(file_path, 'r') as f:
	jdata = json.load(f)

jump = jdata['Quantum']
burst = jdata['BurstTime']
order = jdata['Order']
buf_order = copy.deepcopy(order)

time = 0
check = False
process_count = len(order)

while process_count != 0:
	buf_order = copy.deepcopy(order)
	for p in buf_order:
		if burst[p] > jump:
			for i in range(jump):
				print ("second %d~%d process %s" % (time, time + 1, p))
				time += 1
			burst[p] -= jump
		else:
			for i in range(burst[p]):
				print ("second %d~%d process %s" % (time, time + 1, p))
				time += 1
			process_count -= 1
			order.remove(p)
			
		if process_count != 0:
			print ("===================")