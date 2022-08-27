def get_positions(n):
	pos = [ 0, 0, 0]
	pos1 = (n+1)%3
	pos2 = ((n+1)/3)%3
	pos3 = ((n+1)/9)%3
	if pos1 == 1:
		pos[0] = 0
	elif pos1 == 2:
		pos[0] = 1
	else:
		pos[0] = 2
	if pos2 == 1:
		pos[1] = 0
	elif pos2 == 2:
		pos[1] = 1
	else:
		pos[1] = 2
	if pos3 == 1:
		pos[2] = 0
	elif pos3 == 2:
		pos[2] = 1
	else:
		pos[2] = 2
		
	return (pos[0],pos[1],pos[2])
	
print(get_positions(3))
		
	
