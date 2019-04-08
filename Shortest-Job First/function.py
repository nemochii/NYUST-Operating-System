def function(data_list, jdata):
	time = 0
	buf_time = 0
	process_count = len(jdata)
	processing = []
	check = True

	while process_count != 0:
		for i in data_list:
			if i.a == time:
				processing.append(i)
				data_list.remove(i)
				break
		
		if check:
			check = False
			current = processing[0]
			previous = current

		if len(processing) == 0:
			current = None
			if previous != current:
				print ("Second:%d~%d, Process:%s" % (buf_time, time, previous.name))
				print ("====================")
				buf_time = time

			previous = current
			time += 1
			continue
		else:
			processing.sort(key = lambda process : process.b)	
			current = processing[0]

			if previous != current:
				if previous == None:
					print ("Second:%d~%d, Process:%s" % (buf_time, time, "nothing"))
				else:
					print ("Second:%d~%d, Process:%s" % (buf_time, time, previous.name))
				print ("====================")
				buf_time = time

			if len(processing) == 1 and len(data_list) == 0 and current.b - 1 == 0:
				print ("Second:%d~%d, Process:%s" % (buf_time, time + 1, previous.name))

			current.b -= 1
			if current.b == 0:
				process_count -= 1
				processing.remove(current)

		previous = current
		time += 1