import matplotlib.pyplot as plt

initial_dist = 100
flash_dist = 30
increment = 0.1

timeDelta = 0.5

speed = 34.4
matches = []

pos = initial_dist
steps = [initial_dist]


while pos > 0:
	pos -= speed/2
	steps.append(pos)
print(steps)
speed = 30


while speed < 500/3.6 :
	steps = [initial_dist]
	pos = initial_dist
	while pos > 0:
		pos -= 2*speed*timeDelta
		if pos < 30 and pos > 0 :
			speed += increment
			pos = -1
			continue
		steps.append(pos)
		if pos < 0 :
			matches.append((speed, steps))
	
	speed += increment

vitesses = [match[0]*3.6 for match in matches]

print(matches)
#print([match[0]*3.6 for match in matches])
plt.plot(vitesses, vitesses, 'b*')
plt.show()