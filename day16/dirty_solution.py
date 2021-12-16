class Packet:
    def __init__(self, v, id, data):
        self.v = v
        self.id = id
        self.data = data
    
    def __repr__(self):
        return str((self.v, self.id, self.data))

def part1(bits):
    _, packet = parse_packet(bits)
    return version_sum(packet)
    
def part2(bits):
    _, packet = parse_packet(bits)
    return solve(packet)

def solve(packet):
    if packet.id == 4:
        return packet.data
    data = [solve(p) for p in packet.data]
    if packet.id == 0:
        return sum(data)
    if packet.id == 1:
        prod = 1
        for p in data:
            prod *= p
        return prod
    if packet.id == 2:
        return min(data)
    if packet.id == 3:
        return max(data)
    if packet.id == 5:
        return 1 if data[0] > data[1] else 0
    if packet.id == 6:
        return 1 if data[0] < data[1] else 0
    if packet.id == 7:
        return 1 if data[0] == data[1] else 0

def version_sum(packet):
    if type(packet.data) == type([]):
        return packet.v + sum(version_sum(p) for p in packet.data)
    return packet.v
    
def parse_packet(bits):
    v = None
    type = None
    
    num = []
    subpackets = []
    
    v = bits[:3]
    bits = bits[3:]
    
    type = bits[:3]
    bits = bits[3:]
    
    if type == '100':
        
        while bits:
            if bits[0] == '1':
                num.append(bits[1:5])
                bits = bits[5:]
            if bits[0] == '0':
                num.append(bits[1:5])
                bits = bits[5:]
                break
    else:
        i = bits[:1]
        bits = bits[1:]
        
        if i == '0':
            l = int(bits[:15], 2)
            bits = bits[15:]
            
            subpacket = bits[:l]
            while subpacket:
                new_bits, new_packet = parse_packet(subpacket)
                subpackets.append(new_packet)
                subpacket = new_bits
            
            bits = bits[l:]
        else:
            l = int(bits[:11], 2)
            bits = bits[11:]
            for _ in range(l):
                new_bits, new_packet = parse_packet(bits)
                subpackets.append(new_packet)
                bits = new_bits
    
    if type == '100':
        return bits, Packet(int(v, 2), int(type, 2), int(''.join(num), 2))
    else:
        return bits, Packet(int(v, 2), int(type, 2), subpackets)

table = {
    '0':  '0000',
    '1':  '0001',
    '2':  '0010',
    '3':  '0011',
    '4':  '0100',
    '5':  '0101',
    '6':  '0110',
    '7':  '0111',
    '8':  '1000',
    '9':  '1001',
    'A':  '1010',
    'B':  '1011',
    'C':  '1100',
    'D':  '1101',
    'E':  '1110',
    'F':  '1111'
}

def hex_to_bin(hex):
    b = []
    for c in hex:
        b.append(table[c])
    return ''.join(b)

def parse(lines):
    lines = hex_to_bin(lines[0])
    return lines

import copy

if __name__ == '__main__':
    file = 'input.txt'
    # file = 'input_sample.txt'
    with open(file, 'r') as f:
        lines = f.read().splitlines()
        f.close()
    lines = parse(lines)
    print(part1(copy.deepcopy(lines)))
    print(part2(copy.deepcopy(lines)))
