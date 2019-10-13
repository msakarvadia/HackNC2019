cities = [["s",1,0,"c","NE", 71.14,0, "city 1"], ["u", 0,1,"m","NE",85.33,0,'city 2'],["r",1,1,'o',"SE", 100.00,0,'city 3'],["s",1,0,"m", "SW",106.29,0,'city 4'],['u', 0,1,'o','W', 55.08,0,'city 5']]
#Suburban/Urban/Rural, Park y/n, sports y/n, costal/mountain/other, NE/NW/SE/SW/W, cost of living index relative to new york, amount of fulfilled criteria per user, city name


sampleUserInputEntry = ["s", 0, 1, "c", 'NE', "actuary"]
#Suburban/Urban/Rural, Park y/n, sports y/n, costal/mountain/other, NE/NW/SE/SW/W, career of interest


ranked_cities = cities.copy()
#print(ranked_cities)

for i in ranked_cities:
    for j in range(5):
        if i[j] == sampleUserInputEntry[j]:
            i[6]+= 1

ranks = []
for i in ranked_cities:
    ranks.append(i[6])

#print(ranks)
ranks.sort(reverse = True)
#print(ranks)
best_fromUserInput = []

for i in ranks:
    for j in ranked_cities:
        if i == j[6]:
            best_fromUserInput.append(j[7])
            print(j[7] +", rank: "+str(i))
            ranked_cities.remove(j)
