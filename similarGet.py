# from fake_useragent import UserAgent
import pycountry
import requests
import random
import json
import time

def getSimilarwebData(index, name, domain_for_query):
    result_data_dict = {
        "Name": name,
        "First Organic URL" : domain_for_query,
        "Monthly Visits": 0,
        "Top Country Traffic": "",
        "Total Traffic Percent": 0,
        "Search Traffic Percent": 0
    }
    url = "https://data.similarweb.com/api/v1/data"

    # Domain to get data from
    query = {'domain': domain_for_query}

    # Headers to mimic the browser
    # ua = UserAgent()
    # headers = {'User-Agent':str(ua.chrome)}
    # print(headers)

    headers = {
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36', Itay's
        #  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62',
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
         'cookie': '.DEVICETOKEN.SIMILARWEB.COM=SSGTLpQSk07RyJkFip3PG3B6q9MytjCX; _vwo_uuid=J48B22449B664BFD9E5BCEA5C34F07989; _ga=GA1.2.618333746.1628122923; _hjid=306976aa-3b0e-4532-8027-6a4a0537d3be; _wingify_pc_uuid=909cddb463fb4abfaffef197b92c0652; wingify_donot_track_actions=0; sgID=867681af-574a-0a6b-d21f-9207c45964ed; sw_extension_installed=1628125422720; _pxvid=f856ac23-f588-11eb-8acc-0242ac120007; __qca=P0-1917421963-1628125423269; _BEAMER_USER_ID_zBwGJEbQ32550=c21c1f3b-550e-4519-9780-55cd275c4f99; _BEAMER_FIRST_VISIT_zBwGJEbQ32550=2021-08-05T01:12:08.264Z; _vwo_uuid_v2=D11677409833BA6E0D1D5769236634407|282a4e9ec7fca6ccf2b1253e15886ca2; __utma=107333120.618333746.1628122923.1628126643.1628126643.1; _pk_ref.1.fd33=%5B%22%22%2C%22%22%2C1635418213%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; sc_is_visitor_unique=rx8617147.1635418214.CD5D626E0C414F1B1E3880EF1AB1B9C4.4.4.4.4.4.4.4.4.4; _uetvid=fa84e730f58811eb851a73eb34b2dc76; _pk_id.1.fd33=1975ae28c1405010.1628122924.4.1635418224.1635418213.; mp_7ccb86f5c2939026a4b5de83b5971ed9_mixpanel=%7B%22distinct_id%22%3A%2010417679%2C%22%24device_id%22%3A%20%2217b13b0414a41f-09d4b9c21ff62-2343360-240000-17b13b0414bb56%22%2C%22url%22%3A%20%22https%3A%2F%2Fwww.similarweb.com%2F%22%2C%22language%22%3A%20%22en-us%22%2C%22section%22%3A%20%22home%22%2C%22sub_section%22%3A%20%22page%22%2C%22sub_sub_section%22%3A%20%22%22%2C%22page_id%22%3A%20%22marketintelligence.marketresearch.appmarketanalysis.homepage.title%22%2C%22last_event_time%22%3A%201635418224137%2C%22%24search_engine%22%3A%20%22google%22%2C%22utm_source%22%3A%20%22adwords%22%2C%22utm_medium%22%3A%20%22paid%22%2C%22utm_campaign%22%3A%20%22gs_sch_brand_similar_il%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%2C%22site_type%22%3A%20%22corp%22%2C%22session_id%22%3A%20%222d7e980f-f278-4f51-bc05-aa5b2b5ac5b7%22%2C%22session_first_event_time%22%3A%20%222021-10-28T10%3A50%3A14.806Z%22%2C%22sgId%22%3A%20%22867681af-574a-0a6b-d21f-9207c45964ed%22%2C%22%24user_id%22%3A%2010417679%2C%22ui_generation%22%3A%20%22%22%2C%22ab_test_variation_id%22%3A%20%223%22%2C%22subSection%22%3A%20%22details%22%2C%22account_status%22%3A%20%22Trial%2FFro%22%2C%22is_sw_user%22%3A%20false%2C%22sw_extention%22%3A%20true%2C%22first_time_visitor%22%3A%20false%7D',
         'sec-ch-ua':  'Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98'

    }

    response = requests.get(url = url, params = query, headers = headers)
    print("{0}) The response for '{1}' from SimilarWeb is: {2}".format(index,name,response))
    # print("{0}) The response for '{1}' from SimilarWeb is: {2}".format(index,name,response.text))
    try:
        data_dict = response.json()
    except ValueError:
        print("Decoding JSON has failed, I am waiting 1 minute and trying again...")
        print("Meanwhile, go manually to https://data.similarweb.com/api/v1/data?domain={0} and mark you are not a bot.".format(query['domain']))
        time.sleep(random.randrange(41, 59))
        result_data_dict = {}
        return result_data_dict

    if(data_dict == {}):
        return {
        "Name" : name,
        "First Organic URL" : domain_for_query,
        "Monthly Visits": "Not Enough Data.",
        "Top Country Traffic": "Not Enough Data.",
        "Total Traffic Percent": "Not Enough Data.",
        "Search Traffic Percent": "Not Enough Data."
    }
    # print("The json doctinary returned from SimilarWeb for {0} is: {1}".format(domain_for_query , data_dict))
    # print("Data For The Domain {0}:".format(domain_for_query))

    # First Country
    first_country_numeric_code = data_dict['TopCountryShares'][0]['Country']
    if(first_country_numeric_code < 100 and first_country_numeric_code >= 10):
        numeric_string = '0' + str(first_country_numeric_code)
    elif(first_country_numeric_code < 10 and first_country_numeric_code > 0):
        numeric_string = '00' + str(first_country_numeric_code)
    else:
        numeric_string = str(first_country_numeric_code)
    # print("the numeric string of the country: {0}".format(numeric_string))
    current_country = pycountry.countries.get(numeric=numeric_string).name
    result_data_dict["Top Country Traffic"] = current_country
    # print(current_country)
    first_country_decimal = data_dict['TopCountryShares'][0]['Value']
    # first_country_percent = round(first_country_decimal,4)
    first_country_percent = round((first_country_decimal*100), 2)
    # print(str(first_country_percent) + "%")
    first_country_percent_string = (str(first_country_percent))
    result_data_dict["Total Traffic Percent"] = first_country_percent
    # print('{0} - {1}%'.format(current_country, first_country_percent_string))

    # Monthly Visits
    estimated_monthly_visits = list(data_dict['EstimatedMonthlyVisits'].items())[-1]
    # estimated_monthly_visits_short = round((estimated_monthly_visits[1]/1000000), 2)
    # print(str(Estimated_Monthly_Visits_short) + "M")
    # estimated_monthly_visits_short_string = str(estimated_monthly_visits_short)
    # estimated_monthly_visits_string = str(estimated_monthly_visits[1])
    estimated_monthly_visits_result = estimated_monthly_visits[1]
    # print('Monthly Visits: {0}'.format(estimated_monthly_visits_string)) 
    result_data_dict["Monthly Visits"] = estimated_monthly_visits_result

    # Search Traffic
    search_raffic_data = data_dict['TrafficSources']['Search']
    search_raffic_percent = round((search_raffic_data*100), 2)
    search_raffic_percent_string = str(search_raffic_percent)
    # print('Search Traffic: {0}%'.format(search_raffic_percent_string))
    result_data_dict["Search Traffic Percent"] = search_raffic_percent
    # print('______________________________________________________')
    return result_data_dict