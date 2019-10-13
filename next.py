import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]


creds = ServiceAccountCredentials.from_json_keyfile_name("HackNC2019-33fe3c4ca3c2.json", scope)

client = gspread.authorize(creds)

sheet = client.open("DataNEXT").sheet1  # Open the spreadhseet

data = sheet.get_all_records()  # Get a list of all records

#print((data))

cities = [[0]*8]*len(data)
#print(cities)
for i in range(len(data)):
    cities[i][0]=(data[i].get("City Type (S/U/R)"))
    cities[i][1]=(data[i].get("Sports (Y=1/N=0)"))
    cities[i][2]=(data[i].get("Geo Type (C/M/O)"))
    cities[i][3]=(data[i].get("Region (NE/MW/SW/SE/W)"))
    cities[i][4]=(data[i].get("col"))
    cities[i][5]=0
    cities[i][6]=(data[i].get("Average Salary of a CS Graduate"))
    cities[i][7]=(data[i].get("city"))
    
print(cities)

numRows = sheet.row_count  # Get the number of rows in the sheet
#Suburban/Urban/Rural, sports y/n, costal/mountain/other, NE/MW/SE/SW/W, cost of living relative to ny, amount of fulfilled criteria per user, average cs grad salery in the city,city name


sampleUserInputEntry = ["r", "1", "c", 'NE', "1","0"]
#Suburban/Urban/Rural, sports y/n, costal/mountain/other, NE/NW/SE/SW/W, job (ie. data scientist), prefered industry (ie. health)

ny_p_i = [[90000,87934],[98782,120998]] 
#ny_profession_industry_starting_saleries


ranked_cities = [[]]*len(data)
for i in range(len(cities)):
    ranked_cities[i] = cities[i]
#print(ranked_cities)
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
    ranked_cities[x][5] =   str(float(cities[x][5])/ny_avg_cs_grad_sal * 100)

liveable_cities = []

for i in range(len(ranked_cities)):
   if float(ranked_cities[i][5]) < float(ranked_cities[i][5])+ny_p_i_wi[int(sampleUserInputEntry[4])][int(sampleUserInputEntry[5])]:
       liveable_cities.append(ranked_cities[i])


for i in liveable_cities:
    for j in range(4):
        if i[j] == sampleUserInputEntry[j]:
            i[6]+= 1


ranks = []
for i in liveable_cities:
    ranks.append(i[7])

#print(ranks)
ranks.sort(reverse = True)
#print(ranks)
best_fromUserInput = []

for i in ranks:
    for j in liveable_cities:
        if i == j[6]:
            best_fromUserInput.append(j[6])
            print(str(j[7]) +", rank: "+str(i))
            liveable_cities.remove(j)
