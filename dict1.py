# dictionary test file
d = {}
for x in range(1, 10):
    d['string{0}'.format(x)] = 'Hello'
for s in d:
    print(s)
