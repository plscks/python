d = {}
recs = input('How many redomendations?: ')
recs = int(recs)
for i in range(recs):
    i = i + 1
    d[i] = input('Rec #' + str(i) + ': ')
    print('Rec ' + str(i) + ': ' + d[i])
