import pickle

amps = [{'make': 'Peavey', 'model': 'Classic 20', 'output': 15}, {'make': 'Peavey', 'model': 'Rage 108', 'output': 12}, {'make': 'Crate', 'model': 'GX 212', 'output': 120}]

with open('save.p', 'wb') as f:
    print "wrote save.p"
    pickle.dump(amps, f)

with open('save.p', 'rb') as f:
    pickled_amps = pickle.load(f)

print amps == pickled_amps
