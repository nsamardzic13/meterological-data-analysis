from WorldWeatherPy import RetrieveByAttribute, DetermineListOfAttributes
import os


api_key = 'db9df7dfdaea4e0da13192716223108'    # wuwtpaffvtuxqasdtq@kvhrr.com



my_attributes = DetermineListOfAttributes(api_key, True).retrieve_list_of_options()

"""
Sve opcije - rezultat komande iznad:
'sunrise', 'sunset', 'moonrise', 'moonset', 'moon_phase', 'moon_illumination', 
'time', 'tempC', 'tempF', 'windspeedMiles', 'windspeedKmph', 'winddirDegree', 'winddir16Point', 
'weatherCode', 'weatherIconUrl', 'weatherDesc', 
'precipMM', 'precipInches', 'humidity', 'visibility', 'visibilityMiles', 
'pressure', 'pressureInches', 'cloudcover', 
'HeatIndexC', 'HeatIndexF', 'DewPointC', 'DewPointF', 'WindChillC', 'WindChillF', 'WindGustMiles', 'WindGustKmph', 
'FeelsLikeC', 'FeelsLikeF', 'uvIndex'
"""

done = ['Umag', 'Novigrad', 'Rovinj', 'Porec', 'Vrsar', 'Pazin', 'Buzet', 'Fazana', 'Pula',
        'Medulin', 'Rabac', 'Opatija', 'Rijeka', 'Kostrena', 'Bakar', 'Kraljevica', 'Crikvenica', 'Delnice',
        'Vrbovsko', 'Ogulin', 'Senj', 'Malinska', 'Baska',
        'Bale', 'Boljun', 'Buje',
        'Funtana', 'Hum', 'Kanfanar', 'Karojba',
        'Labin', 'Lupoglav', 'Medulin', 'Motovun', 'Novigrad',
        'Pazin', 'Porec', 'Premantura', 'Pula', 'Puntera',
        'Racice', 'Radetici', 'Radmani', 'Radosi', 'Radovani', 'Rajici',
        'Rovinj', 'Tar', 'Umag', 'Vodnjan', 'Vrsar', 'Bakar', 'Banjol', 'Bribir', 'Cernik', 'Cres', 'Crikvenica',
        'Delnice', 'Fuzine', 'Drazice',
        'Drenova', 'Hreljin', 'Jadranovo', 'Kampor', 'Kastav', 'Klana', 'Kostrena',
        'Klenovica', 'Kraljevica', 'Krasica', 'Krk', 'Kukuljanovo', 'Lopar',
        'Matulji', 'Mrkopalj', 'Njivice', 'Novi Vinodolski', 'Ogulin', 'Opatija', 'Tribalj',
        'Pag', 'Podhum', 'Predosljica', 'Prempen', 'Prezid', 'Punat', 'Rab', 'Selce', 'Skrad',
        'Supetarska+Draga', 'Vrbnik', 'Volosko']

# istarska = []
#
# istarska = [x for x in istarska if x not in done]

pgz = ['Prezid']

# pgz = [x for x in pgz if x not in done]

# for curr_location in istarska:
#     curr_location += ''
for curr_location in pgz:
#     curr_location += ''
    ret_df = RetrieveByAttribute(api_key=api_key, attribute_list=['tempC'],
                                 city=curr_location, start_date='2016-10-31', end_date='2021-10-31',
                                 frequency=3, csv_directory='original_data_files/').retrieve_hist_data()




