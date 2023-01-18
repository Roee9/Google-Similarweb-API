from openpyxl import load_workbook
import pandas as pd
import similarGet
import googleGet
import append
import random
import json
import time
import os

# Make list of words from excel
df = pd.read_excel('advertiserShort.xlsm')
search_list = df['programmeName'].tolist()
print("The search list as seen at the excel file: {0}".format(search_list))

# Get name and first organic URL from google search as a list of tuples
name_URL_tuple_list = googleGet.googleGet(search_list)
print("The (Name,URL) list from Google: {0}".format(name_URL_tuple_list))

# Add the list of tuples to a text file
file = open('List Of Tupels.txt', 'w')
json.dump(name_URL_tuple_list,file)
file.close()

# with open("List Of Names and URLS.txt", "w") as f:
#     f.write(repr(name_URL_tuple_list))


# map1_domain_list = map(lambda mystr: mystr.replace('https://www.','https://'),URL_list)
# map2_domain_list = map(lambda mystr: mystr.replace('https://',''),map1_domain_list)
# domain_list = list(map2_domain_list)
# domain_list = ['botb.com/', 'menkind.co.uk/', 'fragrancedirect.co.uk/', 'boucleme.co.uk/', 'musclefood.com/', 'serenataflowers.com/', 'yoursclothing.co.uk/', 'https://siksilk.com/', 'badrhino.com/', 'omorovicza.com/', 'dorothyperkins.com/', 'asos.com/', 'simplysupplements.co.uk/', 'dunelm.com/', 'standout.co.uk/', 'jdwilliams.co.uk/', 'lookfantastic.com/', 'vodafone.co.uk/mobile/best-sim-only-deals/pay-as-you-go-sim', 'myvitamins.com/', 'everything5pounds.com/', 'alloutdoor.co.uk/', 'mybag.com/', 'foodspring.co.uk/', 'https://find-and-update.company-information.service.gov.uk/company/09476649', 'feelunique.com/', 'sharkclean.com/', 'jacamo.co.uk/', 'retechuk.com/pages/activewear-homepage', 'beautyexpert.com/']
# print("The domain list after 2 maps: {0}".format(domain_list))

# Get data from similar web for each domain URL
# and add data to Excel file
i = 0
for domain in name_URL_tuple_list:
    result_data_dict_for_domain = similarGet.getSimilarwebData(i,name_URL_tuple_list[i][0],name_URL_tuple_list[i][-1])
    while(result_data_dict_for_domain == {}):
        result_data_dict_for_domain = similarGet.getSimilarwebData(i,name_URL_tuple_list[i][0],name_URL_tuple_list[i][-1])
    # print(result_data_dict_for_domain)
    df2 = pd.DataFrame(data=result_data_dict_for_domain, index=[i])
    append.append_df_to_excel('result.xlsx', df2)
    time.sleep(random.randrange(1, 3))
    i = i + 1