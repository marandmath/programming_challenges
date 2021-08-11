#One more solution using the re module
# https://www.reddit.com/r/adventofcode/comments/3vmltn/day_6_solutions/cxov4hk/?utm_source=reddit&utm_medium=web2x&context=3

lights = [[0]*1000 for i in range(1000)] #Alternative to using Numpy
with open('input.txt') as f:
	s = f.read()

def prepare(l):
	if 'on' in l:
		f = lambda x: 1    #1+x
		l = l.replace('turn on ', '')
	elif 'off' in l:
		f = lambda x: 0    #max(x-1, 0)
		l = l.replace('turn off ', '')
	elif 'toggle' in l:
		f = lambda x: x+1%2    #x + 2
		l = l.replace('toggle ', '')
	return l, f

def dorange(lights, start, end, fn):
	for i in range(start[0], end[0] + 1):
		for j in range(start[1], end[1] + 1):
			lights[i][j] = fn(lights[i][j])

def day6(lights, instr):
	for l in instr:
		f = None
		l, f = prepare(l)
		l = l.split(' through ')
		start = [i for i in map(int, l[0].split(','))]
		end = [i for i in map(int, l[1].split(','))]
		dorange(lights, start, end, f)

print(sum(map(sum, l)))