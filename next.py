cities = [["s",0,"c","NE", 71.14,0, 89090,"city 1"], ["u", 1,"m","NE",85.33,0,98988,'city 2'],["r",1,'o',"SE", 100.00,0,90289,'city 3'],["s",0,"m", "SW",106.29,0,78908,'city 4'],['u', 1,'o','W', 55.08,0,90067,'city 5']]
#Suburban/Urban/Rural, sports y/n, costal/mountain/other, NE/NW/SE/SW/W, cost of living index relative to new york, amount of fulfilled criteria per user, average cs grad salery in the city,city name


sampleUserInputEntry = ["s", 1, "c", 'NE', 1,0]
#Suburban/Urban/Rural, sports y/n, costal/mountain/other, NE/NW/SE/SW/W, job (ie. data scientist), prefered industry (ie. health)

ny_p_i = [[90000,87934],[98782,120998]] 
#ny_profession_industry_starting_saleries

ranked_cities = cities.copy()
#Suburban/Urban/Rural, sports y/n, costal/mountain/other, NE/NW/SE/SW/W, cost of living index relative to new york, amount of fulfilled criteria per user, avg cs grad salery wage index,city name
#print(ranked_cities)

ny_p_i_wi = ny_p_i.copy() 
#ny professions in different industry starting saleries wage index relative to average cs grad in ny-ny average wi for average cs grads

#all_cities_wi = [0]*len(cities)
#wage index of average cs grads in different cities relative to NY

ny_avg_cs_grad_sal = 89214

for x in range(len(ny_p_i)):
    for y in range(len(ny_p_i[x])):
        ny_p_i_wi[x][y] = ny_p_i[x][y]/ny_avg_cs_grad_sal * 100  - 100

for x in range(len(cities)):
    ranked_cities[x][6] =   cities[x][6]/ny_avg_cs_grad_sal * 100
    for y in range(len(ny_p_i[x])):


print(ny_p_i_wi)


for i in ranked_cities:
    for j in range(4):
        if i[j] == sampleUserInputEntry[j]:
            i[5]+= 1

ranks = []
for i in ranked_cities:
    ranks.append(i[5])

#print(ranks)
ranks.sort(reverse = True)
#print(ranks)
best_fromUserInput = []

for i in ranks:
    for j in ranked_cities:
        if i == j[5]:
            best_fromUserInput.append(j[5])
            print(str(j[5]) +", rank: "+str(i))
            ranked_cities.remove(j)
