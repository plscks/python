craft = {}
craft.setdefault('carving knife', []).append('+4xp / +2AP')
craft.setdefault('carving knife', []).append('1 Chunk of Steel')
craft.setdefault('chainsaw', []).append('+14xp / +7AP')
craft.setdefault('chainsaw', []).append('2 Chunk of Steel')
craft.setdefault('chainsaw', []).append('1 Length of Chain')
craft.setdefault('chainsaw', []).append('2 Bag of Industrial Plastic')
craft.setdefault('cutlass', []).append('+10xp / +5AP')
craft.setdefault('cutlass', []).append('2 Chunk of Steel')
craft.setdefault('cutlass', []).append('1 Chunk of Brass')
craft.setdefault('hatchet', []).append('+6xp / +3AP')
craft.setdefault('hatchet', []).append('1 Chunk of Iron')
craft.setdefault('hatchet', []).append('1 Piece of Wood')
craft.setdefault('rapier', []).append('+10xp / +5AP')
craft.setdefault('rapier', []).append('2 Chunk of Steel')
craft.setdefault('rapier', []).append('1 Chunk of Iron')
craft.setdefault('sabre', []).append('+10xp / +5AP')
craft.setdefault('sabre', []).append('2 Chunk of Steel')
craft.setdefault('sabre', []).append('1 Chunk of Iron')
craft.setdefault('sword', []).append('+10xp / +5AP')
craft.setdefault('sword', []).append('3 Chunk of Steel')
craft.setdefault('tarnished sword', []).append('+10xp / +5AP')
craft.setdefault('tarnished sword', []).append('2 Chunk of Steel')
craft.setdefault('tarnished sword', []).append('1 Silver Ingot')
craft.setdefault('torch', []).append('+8xp / +4AP')
craft.setdefault('torch', []).append('1 Piece of Wood')
craft.setdefault('torch', []).append('1 Batch of Leather')
craft.setdefault('torch', []).append('1 Length of Rope')
craft.setdefault('torch', []).append('1 Chunk of Brass')
craft.setdefault('chainmail shirt', []).append('+20xp / +10AP')
craft.setdefault('chainmail shirt', []).append('4 Chunk of Steel')
craft.setdefault('fireman\'s jacket', []).append('+10xp / +5AP')
craft.setdefault('fireman\'s jacket', []).append('2 Batch of Leather')
craft.setdefault('fireman\'s jacket', []).append('1 Bag of Industrial Plastic')
craft.setdefault('leather cuirass', []).append('+4xp / +2AP')
craft.setdefault('leather cuirass', []).append('3 Batch of Leather')
craft.setdefault('leather jacket', []).append('+4xp / +2AP')
craft.setdefault('leather jacket', []).append('2 Batch of Leather')
craft.setdefault('plate cuirass', []).append('+20xp / +10AP')
craft.setdefault('plate cuirass', []).append('4 Chunk of Steel')
craft.setdefault('plate cuirass', []).append('2 Batch of Leather')
craft.setdefault('suit of light body armor', []).append('+20xp / +10AP')
craft.setdefault('suit of light body armor', []).append('2 Batch of Leather')
craft.setdefault('suit of light body armor', []).append('3 Bag of Industrial Plastic')
craft.setdefault('suit of military encounter armor', []).append('+30xp / +15AP')
craft.setdefault('suit of military encounter armor', []).append('4 Bag of Industrial Plastic')
craft.setdefault('suit of military encounter armor', []).append('2 Batch of Leather')
craft.setdefault('suit of police riot armor', []).append('+20xp / +10AP')
craft.setdefault('suit of police riot armor', []).append('2 Batch of Leather')
craft.setdefault('suit of police riot armor', []).append('3 Bag of Industrial Plastic')
craft.setdefault('flamethrower', []).append('+16 xp / +8AP')
craft.setdefault('flamethrower', []).append('4 Chunk of Steel')
craft.setdefault('flamethrower', []).append('1 Bag of Industrial Plastic')
craft.setdefault('pistol', []).append('+8xp / +4AP')
craft.setdefault('pistol', []).append('1 Chunk of Brass')
craft.setdefault('pump action shotgun', []).append('+16xp / +8AP')
craft.setdefault('pump action shotgun', []).append('3 Chunk of Steel')
craft.setdefault('pump action shotgun', []).append('1 Chunk of Brass')
craft.setdefault('pump action shotgun', []).append('1 Piece of Wood')
craft.setdefault('rifle', []).append('+16xp / +8AP')
craft.setdefault('rifle', []).append('5 Chunk of Steel')
craft.setdefault('rifle', []).append('1 Chunk of Brass')
craft.setdefault('rifle', []).append('1 Piece of Wood')
craft.setdefault('sub-machine gun', []).append('+12xp / +6AP')
craft.setdefault('sub-machine gun', []).append('2 Chunk of Steel')
craft.setdefault('sub-machine gun', []).append('1 Chunk of Brass')
craft.setdefault('long bow', []).append('+14xp / +7AP')
craft.setdefault('long bow', []).append('3 Piece of Wood')
craft.setdefault('short bow', []).append('+6xp / +3AP')
craft.setdefault('short bow', []).append('1 Piece of Wood')
craft.setdefault('sling', []).append('+8xp / +4AP')
craft.setdefault('sling', []).append('2 Batch of Leather')
craft.setdefault('compound bow', []).append('+10xp / +5AP')
craft.setdefault('compound bow', []).append('2 Piece of Wood')
craft.setdefault('compound bow', []).append('1 Bag of Industrial Plastic')


print(craft['carving knife'])
print(craft['hatchet'])
print(craft['sling'])
print(craft['suit of police riot armor'])
#for f in craft:
#    print(f)
#partlist = list(craft.keys())
#print(partlist)
fullist = '\n•'.join(list(craft.keys()))
#fullist[0] =  '•carving knife'
print('•' + fullist)