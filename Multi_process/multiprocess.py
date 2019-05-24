import os
import json
import sys
from multiprocessing import Process, Queue, Pipe, Pool

file_path = sys.argv[1]
with open(file_path, 'r') as f:
	jdata = json.load(f)

def send(q, s_who, message):
	#q.put(message)
	#q.put(os.getpid())
	q.send(message)
	q.send(os.getpid())
	print ("%d %s send %s" % (os.getpid(), s_who, message))

def get(q, s_who, r_who):
	print ("%d %s get %s from process %d %s" % (os.getpid(), r_who, q.recv(), q.recv(), s_who))

if __name__ == '__main__':
	#q = Queue()
	q = Pipe()
	"""
	pool = Pool()
	for s in jdata:
		pool.apply_async(send, args = (q[0], s, jdata[s][1],))
	for s in jdata:
		pool.apply_async(get, args = (q[1], s, jdata[s][0],))

	pool.close()
	pool.join()
	"""
	for s in jdata:
		send_p = Process(target = send, args = (q[0], jdata[s][1], s,))
		send_p.start()
		send_p.join()
	for s in jdata:
		receive_p = Process(target = get, args = (q[1], jdata[s][0], s,))
		receive_p.start()
		receive_p.join()