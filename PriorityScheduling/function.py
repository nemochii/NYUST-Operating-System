def function(data_list, jdata):
	time = 0
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
				print ("====================")

			previous = current
			print ("second %d~%d nothing is processing" % (time, time + 1))
			time += 1
			continue
		else:
			processing.sort(key = lambda process : process.p)	
			current = processing[0]
			if previous != current:
				print ("====================")

			print ("second %d~%d process %s" % (time, time + 1, current.name))
			
			current.b -= 1
			if current.b == 0:
				process_count -= 1
				processing.remove(current)

		previous = current
		time += 1