cities = [["s",0,"c","NE", 71.14,0, "city 1"], ["u", 1,"m","NE",85.33,0,'city 2'],["r",1,'o',"SE", 100.00,0,'city 3'],["s",0,"m", "SW",106.29,0,'city 4'],['u', 1,'o','W', 55.08,0,'city 5']]
#Suburban/Urban/Rural, sports y/n, costal/mountain/other, NE/NW/SE/SW/W, cost of living index relative to new york, amount of fulfilled criteria per user, city name


sampleUserInputEntry = ["s", 1, "c", 'NE', 1,0]
#Suburban/Urban/Rural, sports y/n, costal/mountain/other, NE/NW/SE/SW/W, job (ie. data scientist), prefered industry (ie. health)

ny_p_i = [[30,34],[92,98]] 
#ny_profession_industry_starting_saleries

ny_p_i_wi = [[],[]]
#ny professions in different industry starting saleries wage index relative to average cs grad in ny

avg_cs_grad_sal = 89214

for x in range(len(ny_p_i)):
    for y in range(len(ny_p_i[x])):
        ny_p_i_wi[x][y] = ny_p_i[x][y]/avg_cs_grad_sal * 100

ranked_cities = cities.copy()
#print(ranked_cities)

for i in ranked_cities:
    for j in range(4):
        if i[j] == sampleUserInputEntry[j]:
            i[5]+= 1

ranks = []
for i in ranked_cities:
    ranks.append(i[5])

print(ranks)
ranks.sort(reverse = True)
print(ranks)
best_fromUserInput = []

for i in ranks:
    for j in ranked_cities:
        if i == j[5]:
            best_fromUserInput.append(j[6])
            print(j[6] +", rank: "+str(i))
            ranked_cities.remove(j)
