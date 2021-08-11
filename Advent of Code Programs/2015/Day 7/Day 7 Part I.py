import operator
global gates

ops = {	None	:	None,
		"NOT"	:	operator.invert,
		"OR"	:	operator.or_,
		"AND"	:	operator.and_,
		"RSHIFT":	operator.rshift,
		"LSHIFT":	operator.lshift }

# A dictionary of all the gates with keys being the lowercase name of each wire
# and its value is its corresponding CURRENT value
gates = {}

# We are going to model the gates through a class which is very convenient for
# these type of problems

class Gate:
    
    def __init__(self, operation = None, *inwires): # Here we use the asterisk 
    # notation because we dont know how many input wires we are going to pass
    # to each instance of this class (could be 0, 1 or 2 wires) (*)                            
        self.operation = operation
        # The input value will be put in a list for the sole reason that we 
        # mentioned above at note (*)
        self.input_value = [int(x) if x.isdigit() else x for x in inwires]
        self.output_value = 0 # It will become apparent from the next method
                              # that this value here should be FALSE
    
    # Due to the nature of the instructions this will have to be a reccursive
    # method
    def calculate_output_value(self):
        """Calculating the output value of each instance of Gate that is then
        passed to a wire"""
        if not self.output_value:
            self.output_value = ops[self.operation](*[x if isinstance(x, int) else gates[x].calculate_output_value() for x in self.input_value]) & 0xFFFF
            #                ^ Because this is a recursive method this is nee-
            # ded because we calculate in a sequence the passing of the value
            # of each gate to a subsequent wire and so on. Also the instruction
            # in the case of right and left shifts or in the case of direct
            # assignment of integral value can be an integer!
            return self.output_value
        
        
with open("input.txt") as f_obj: 
    instructions = f_obj.readlines()

for line in instructions:
    [inval , outwire] = line.strip().split('-> ')
    inval = inval.split()
    if len(inval) == 1: #Could be a direct value assignement or an identity re-
                        #assignement so .isdigit() here will raise and except-
                        #ion (quite possibly, due to the second reason stated)
        gates[outwire] = Gate(None, outwire)
    else:                              #     v have to unpack, to not deal with lists
        gates[outwire] = Gate(inval.pop(-2), *inval)
        #                           ^^ even if the operation is NOT or anything
        # else. Due to the structure of the instructions, we have to put a -2!
        # We also .pop that operation so we are left with the wire(s)

value_a = gates['a'].calculate_output_value()    
print(f"The final value of the wire 'a' is: {value_a}")


