import re

class Source:
    
    def __init__(self, signal):
        self.signal = signal
        self.connect_to = None
        
    def activate(self):
        return self.signal
    
    def deactivate(self):
        pass
    
    def __repr__(self):
        return f"Source({self.signal})"
        

class Wire:
    
    def __init__(self, label):
        self.label = label
        self.signal = None
        self.connect_from = None
        self.connect_to = None
        
    def __repr__(self):
        return f"{self.label}: {self.signal}"
    
    def activate(self):
        if self.signal is None:
            self.signal = self.connect_from.activate()
        return self.signal
    
    def deactivate(self):
        if self.signal is not None:
            self.connect_from.deactivate()
            self.signal = None
        
    

class Gate:
    
    def __init__(self, kind, bits=None):
        self.kind = kind
        self.bits = bits
        self.inputs = list()
        self.output = None
        self.signal = None
        
    def activate(self):
        if self.signal is None:
            match self.kind:
                case "NOT":
                    self.signal = ~self.inputs[0].activate()
                case "AND":
                    self.signal = self.inputs[0].activate() & self.inputs[1].activate()
                case "OR":
                    self.signal = self.inputs[0].activate() | self.inputs[1].activate()
                case "LSHIFT":
                    self.signal = self.inputs[0].activate() << self.bits
                case "RSHIFT":
                    self.signal = self.inputs[0].activate() >> self.bits
        return self.signal
    
    def deactivate(self):
        if self.signal is not None:
            for input_object in self.inputs:
                input_object.deactivate()
            self.signal = None
            
    def repr(self):
        return f"{self.kind.title()}({self.signal})"
    
wires = dict()

# First we just create the wires and worry about the gates later

for line in open("day07.in"):
    for label in re.findall(r"([a-z]+)", line):
        if label not in wires:
            wires[label] = Wire(label)
        
# Now we create the gates and connect the wires
for line in open("day07.in"):
    line = line.strip()
    gatedef, out = line.split(" -> ")
    if "AND" in gatedef:
        gate = Gate("AND")
        input1, input2 = gatedef.split(" AND ")
        if input1 in wires:
            wire1 = wires[input1]
        else:
            wire1 = Source(int(input1))
        if input2 in wires:
            wire2 = wires[input2]
        else:
            wire2 = Source(int(input2))
        wire1.connect_to = gate
        wire2.connect_to = gate
        outwire = wires[out]
        outwire.connect_from = gate
        gate.inputs = [wire1, wire2]
        gate.output = outwire
    elif "OR" in gatedef:
        gate = Gate("OR")
        input1, input2 = gatedef.split(" OR ")
        if input1 in wires:
            wire1 = wires[input1]
        else:
            wire1 = Source(int(input1))
        if input2 in wires:
            wire2 = wires[input2]
        else:
            wire2 = Source(int(input2))
        wire1.connect_to = gate
        wire2.connect_to = gate
        outwire = wires[out]
        outwire.connect_from = gate
        gate.inputs = [wire1, wire2]
        gate.output = outwire
    elif "NOT" in gatedef:
        gate = Gate("NOT")
        inputlabel = gatedef.removeprefix("NOT ")
        if inputlabel in wires:
            wire = wires[inputlabel]
        else:
            wire = Source(int(inputlabel))
        wire.connect_to = gate
        outwire = wires[out]
        outwire.connect_from = gate
        gate.inputs = [wire]
        gate.output = outwire
    elif "LSHIFT" in gatedef:
        inputlabel, bits = gatedef.split(" LSHIFT ")
        gate = Gate("LSHIFT", int(bits))
        if inputlabel in wires:
            wire = wires[inputlabel]
        else:
            wire = Source(int(inputlabel))
        wire.connect_to = gate
        outwire = wires[out]
        outwire.connect_from = gate
        gate.inputs = [wire]
        gate.output = outwire
    elif "RSHIFT" in gatedef:
        inputlabel, bits = gatedef.split(" RSHIFT ")
        gate = Gate("RSHIFT", int(bits))
        if inputlabel in wires:
            wire = wires[inputlabel]
        else:
            wire = Source(int(inputlabel))
        wire.connect_to = gate
        outwire = wires[out]
        outwire.connect_from = gate
        gate.inputs = [wire]
        gate.output = outwire
    elif gatedef in wires:
        wire = wires[gatedef]
        outwire = wires[out]
        wire.connect_to = outwire
        outwire.connect_from = wire
    else:
        wires[out].connect_from = Source(int(gatedef))

a_signal = wires['a'].activate()
print(a_signal)

wires['a'].deactivate()

wires['b'].connect_from = Source(a_signal)

a_signal = wires['a'].activate()
print(a_signal)