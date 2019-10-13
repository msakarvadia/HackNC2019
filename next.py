import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]


creds = ServiceAccountCredentials.from_json_keyfile_name("HackNC2019-33fe3c4ca3c2.json", scope)

client = gspread.authorize(creds)

sheet = client.open("DataNEXT").sheet1  # Open the spreadhseet

data = sheet.get_all_records()  # Get a list of all records

print(data)

numRows = sheet.row_count  # Get the number of rows in the sheet
#Suburban/Urban/Rural, sports y/n, costal/mountain/other, NE/MW/SE/SW/W, cost of living relative to ny, amount of fulfilled criteria per user, average cs grad salery in the city,city name


sampleUserInputEntry = ["r", 1, "c", 'NE', 1,0]
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

liveable_cities = []

for i in range(len(ranked_cities)):
   if ranked_cities[i][4] < ranked_cities[i][6]+ny_p_i_wi[sampleUserInputEntry[4]][sampleUserInputEntry[5]]:
       liveable_cities.append(ranked_cities[i])

for i in liveable_cities:
    for j in range(4):
        if i[j] == sampleUserInputEntry[j]:
            i[5]+= 1

ranks = []
for i in liveable_cities:
    ranks.append(i[5])

#print(ranks)
ranks.sort(reverse = True)
#print(ranks)
best_fromUserInput = []

for i in ranks:
    for j in liveable_cities:
        if i == j[5]:
            best_fromUserInput.append(j[5])
            print(str(j[7]) +", rank: "+str(i))
            liveable_cities.remove(j)
