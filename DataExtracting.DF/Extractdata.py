#<------------------------------------Required Packages----------------------------->

import pandas as pd 
import json
import os

#<-------------------------------------------------Extracting Data From Json File ----------------------------------------------------------------------------------->

# This is direct the path to get the datas as the states
path = "C:/Users/Welcome/OneDrive/Documents/phonepe/pulse/data/aggregated/transaction/country/india/state/"
all_states = os.listdir(path)
dclm = {'State':[],'Year':[],'Quater':[],'Transaction_type':[],'Transaction_count':[],'Transaction_amount':[]}
for i in all_states:
    pi = path+i+"/"
    agg_yr =os.listdir(pi)
    for j in agg_yr:
        pj = pi+j+"/"
        agg_yr_lis=os.listdir(pj)
        for k in agg_yr_lis:
            pk = pj+k
            data = open(pk,'r')
            d = json.load(data)
            for x in d['data']['transactionData']:
                Name=x['name']
                count=x['paymentInstruments'][0]['count']
                amount=x['paymentInstruments'][0]['amount']
                dclm['Transaction_type'].append(Name)
                dclm['Transaction_count'].append(count)
                dclm['Transaction_amount'].append(amount)
                dclm['State'].append(i)
                dclm['Year'].append(j)
                dclm['Quater'].append(int(k.strip('.json')))
agg_trans=pd.DataFrame(dclm)
# Successfully DataFrame created
agg_trans
# agg_trans to_csv("agg_trans.csv")   * this for convert Dataframe to csv file.
#<-------------------------------------------------------------------------------------------------------------------------------------------->

# This is direct the path to get the datas as the states
path = "C:/Users/Welcome/OneDrive/Documents/phonepe/pulse/data/aggregated/user/country/india/state/"
allstates = os.listdir(path)
mclm = {'State':[],'Year':[],'Quater':[],'Brand':[],'Brand_count':[],'Brand_percentage':[]}
for i in allstates:
    pi = path+i+"/"
    all_yr=os.listdir(pi)
    for j in all_yr:
        pj= pi+j+"/"
        all_yr_lis=os.listdir(pj)
        for k in all_yr_lis:
            pk = pj+k
            data = open(pk,'r')
            d = json.load(data)
            try:
                for x in d['data']["usersByDevice"]:
                    brand=x['brand']
                    count=x['count']
                    percentage=x['percentage']
                    mclm['Brand'].append(brand)
                    mclm['Brand_count'].append(count)
                    mclm['Brand_percentage'].append(percentage)
                    mclm['State'].append(i)
                    mclm['Year'].append(j)
                    mclm['Quater'].append(int(k.strip('.json')))
            except:
                pass
agg_user = pd.DataFrame(mclm)
# Successfully DataFrame created
agg_user
# agg_user to_csv("agg_user.csv")   * this for convert Dataframe to csv file.
#<------------------------------------------------------------------------------------------------------------------------------------------------------>

# This is direct the path to get the datas as the states
path = "C:/Users/Welcome/OneDrive/Documents/phonepe/pulse/data/map/transaction/hover/country/india/state/"
all_states=os.listdir(path)
xclm = {'State':[],'Year':[],'Quater':[],'District':[],'Transaction_count':[],'Transaction_amount':[]}
for i in all_states:
    pi = path+i+"/"
    all_yr=os.listdir(pi)
    for j in all_yr:
        pj = pi+j+"/"
        all_yr_lis=os.listdir(pj)
        for k in all_yr_lis:
            pk = pj+k
            data = open(pk,'r')
            d = json.load(data)
            try:
                for x in d['data']['hoverDataList']:
                    district=x['name']
                    count=x['metric'][0]['count']
                    amount=x['metric'][0]['amount']
                    xclm['District'].append(district)
                    xclm['Transaction_count'].append(count)
                    xclm['Transaction_amount'].append(amount)
                    xclm['State'].append(i)
                    xclm['Year'].append(j)
                    xclm['Quater'].append(int(k.strip('.json')))
            except:
                pass
map_trans = pd.DataFrame(xclm)
# Successfully DataFrame created
map_trans
# map_trans to_csv("map_trans.csv")   * this for convert Dataframe to csv file.
#<--------------------------------------------------------------------------------------------------------------------------------------------------------->

# This is direct the path to get the datas as the states
path = "C:/Users/Welcome/OneDrive/Documents/phonepe/pulse/data/map/user/hover/country/india/state/"
all_states = os.listdir(path)
sclm = {'State':[],'Year':[],'Quater':[],'District':[],'Registered_user':[],'App_opening':[]}
for i in all_states:
    p_i = path+i+"/"
    year = os.listdir(p_i)
    for j in year:
        p_j = p_i+j+"/"
        file = os.listdir(p_j)
        for k in file:
            p_k = p_j+k
            Data = open(p_k, 'r')
            D = json.load(Data)
            try:
                for z in D['data']["hoverData"]:
                    district = z
                    registered_user =  D['data']["hoverData"][z]["registeredUsers"]
                    app_opening = D['data']["hoverData"][z]["appOpens"]
                    sclm['District'].append(district)
                    sclm['Registered_user'].append(registered_user)
                    sclm['App_opening'].append(app_opening)
                    sclm['State'].append(i)
                    sclm['Year'].append(j)
                    sclm['Quater'].append(int(k.strip('.json')))
            except:
                pass       
map_user = pd.DataFrame(sclm)
# Successfully DataFrame created
map_user
# map_user to_csv("map_user.csv")   * this for convert Dataframe to csv file.
##<----------------------------------------------------------------------------------------------------------------------------------------------->

# This is direct the path to get the datas as the states
path = "C:/Users/Welcome/OneDrive/Documents/phonepe/pulse/data/top/transaction/country/india/state/"
all_states = os.listdir(path)
fclm = {'State': [], 'Year': [], 'Quater': [], 'District': [],
    'Transaction_count': [], 'Transaction_amount': []}
for i in all_states:
    pi = path+i+"/"
    year = os.listdir(pi)
    for j in year:
        pj = pi+j+"/"
        file = os.listdir(pj)
        for k in file:
            pk = pj+k
            Data = open(pk, 'r')
            D = json.load(Data)
            for z in D['data']["districts"]:
                district = z['entityName']
                count = z['metric']['count']
                amount = z['metric']['amount']
                fclm['District'].append(district)
                fclm['Transaction_count'].append(count)
                fclm['Transaction_amount'].append(amount)
                fclm['State'].append(i)
                fclm['Year'].append(j)
                fclm['Quater'].append(int(k.strip('.json')))
top_trans = pd.DataFrame(fclm)
# Successfully DataFrame created
top_trans
# top_trans to_csv("top_trans.csv")   * this for convert Dataframe to csv file.
#<--------------------------------------------------------------------------------------------------------------------------------------------->

# This is direct the path to get the datas as the states
path = "C:/Users/Welcome/OneDrive/Documents/phonepe/pulse/data/top/user/country/india/state/"
all_states = os.listdir(path)
lclm = {'State':[],'Year':[],'Quater':[],'Districts':[],'Registeredusers':[]}
for i in all_states:
    pi = path+i+"/"
    allyr = os.listdir(pi)
    for j in allyr:
        pj = pi+j+"/"
        allfiles = os.listdir(pj)
        for k in allfiles:
            pk = pj+k
            Data = open(pk, 'r')
            d = json.load(Data)
            for x in d["data"]["districts"]:
                districts = x["name"]
                users = x["registeredUsers"]
                lclm["Districts"].append(districts)
                lclm["Registeredusers"].append(users)
                lclm["State"].append(i)
                lclm["Year"].append(j)
                lclm["Quater"].append(int(k.strip(".json")))
top_user = pd.DataFrame(lclm)
# Successfully DataFrame created
top_user
# top_user to_csv("top_user.csv")   * this for convert Dataframe to csv file.
#<---------------------------------------------------------------------------------