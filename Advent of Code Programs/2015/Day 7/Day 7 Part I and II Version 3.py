import operator

ops = {	None	:	lambda x: x,
		"NOT"	:	operator.invert,
		"OR"	:	operator.or_,
		"AND"	:	operator.and_,
		"RSHIFT":	operator.rshift,
		"LSHIFT":	operator.lshift }

gates = {}

class Gate:
	def __init__(self, op = None, *inwires):
		self.op = op
		self.inv = [int(x) if x.isdigit() else x for x in inwires]
		self.out = 0000000000000000

	def calculate_out(self):
		if not self.out:
			self.out = ops[self.op](*[x if isinstance(x, int) else gates[x].calculate_out() for x in self.inv]) & 0xFFFF
		return self.out

with open('input.txt') as f:
	for line in f:
		ind, outd = line.strip().split('-> ')
		ind = ind.split()
		if len(ind) == 1:
			gates[outd] = Gate(None, ind[0])
		else:
			gates[outd] = Gate(ind.pop(-2), *ind)
			
	first_answer = gates['a'].calculate_out()

	print("7.1:", first_answer)
 	for _, gate in gates.items():
		gate.out = 0
		gates['b'].out = first_answer
 	print("7.2:", gates['a'].calculate_out())