lst1 = [
    {'title':'Movie1', 'year':2016, 'rating':'R', 'gross':200},
    {'title':'Movie2', 'year':2017, 'rating':'PG', 'gross':400},
    {'title':'Movie3', 'year':2018, 'rating':'PG-13', 'gross':600},
    {'title':'Movie4', 'year':2019, 'rating':'G', 'gross':800},
    {'title':'Movie5', 'year':2020, 'rating':'R', 'gross':950},
    {'title':'Movie5', 'year':2021, 'rating':'PG', 'gross':300},
    {'title':'Movie5', 'year':2022, 'rating':'PG-13', 'gross':700},
    {'title':'Movie5', 'year':2024, 'rating':'G', 'gross':990},
    {'title':'Movie5', 'year':2023, 'rating':'G', 'gross':1000},
    {'title':'Movie5', 'year':2025, 'rating':'R', 'gross':100},
    {'title':'Movie5', 'year':2026, 'rating':'R', 'gross':0},
    ]

lst2 = [
    {'country':'CHN', 'population':1439323776, 'lang':'ch', 'urban':61},
    {'country':'IND', 'population':1380004385, 'lang':'in', 'urban':35},
    {'country':'USA', 'population':331002651,  'lang':'en', 'urban':83},
    {'country':'IDN', 'population':273523615,  'lang':'id', 'urban':56},
    {'country':'PAK', 'population':220892340,  'lang':'pk', 'urban':35},
    {'country':'BRA', 'population':212559417,  'lang':'pt', 'urban':88},
    {'country':'NGA', 'population':206139589,  'lang':'en', 'urban':52},
    {'country':'BGD', 'population':164689383,  'lang':'bd', 'urban':39},
    {'country':'RUS', 'population':145934462,  'lang':'ru', 'urban':74},
    {'country':'MEX', 'population':128932753,  'lang':'es', 'urban':84},
    {'country':'JPN', 'population':126476461,  'lang':'jp', 'urban':92},
    ]

class stats():
    """ Some basic statistical analysis tools, all of them have been written a million times already, nothing new."""
    def clean(list_of_dicts, key, min=0, max=0):
        """Cleans numeric/string data. Takes a list of dictionaries, a key and (min/max) if it's numeric data, returns cleaned data"""
        if type(list_of_dicts[0][key]) == int or type(list_of_dicts[0][key]) == float:
            list_of_dicts = [x for x in list_of_dicts if max > x[key] > min]
        elif type(list_of_dicts[0][key]) == str:
            list_of_dicts = [x for x in list_of_dicts if x[key] != '']
        return list_of_dicts
    def histogram(list_of_dicts, key):
        """takes a list of dictionaries and a key, returns the recurrunce of values of this column (dict)."""
        count = {}
        for row in list_of_dicts:
            try:
                count[ row[key] ] += 1
            except:
                count[ row[key] ] = 1
        return count
    def average(list_of_dicts, key, start=0, end=0):
        """Takes a list of dictionaries and a key, returns an arithmatic average of all desired key values in the list (float)."""
        if start == 0 and end == 0:
            start, end = 0, len(list_of_dicts)
        else:
            pass
        accumlated = 0
        for i in range(start, end):
            accumlated += list_of_dicts[i][key]
        return accumlated/(end-start)
    def headers(list_of_dicts):
        """Takes a list of dictionaries, returns a list of the keys (headers) of the first row of data (list)."""
        headers = list(list_of_dicts[0].keys())
        return headers
    def series(list_of_dicts, *keys):
        """Takes a list of dictionaries, *keys (multiple),
        or one dictionary {x1:y1, x2:y2, ..} --> {x:[x1, x2, ..],y:[y1, y2, ..]}
        returns a dictionary of {key:list, ..} of series data (dict)."""
        if keys==():
            one_dict = list_of_dicts
            series = { 'x':[ key for key, value in one_dict.items() ] , 'y':[ value for key, value in one_dict.items() ] }
        else:
            series = { x:[] for x in keys }
            for row in list_of_dicts:
                for key, value in series.items():
                    value.append(row[key])
        return series
    def resample(dict, x_key, y_key, width=20):
        x_min = min(dict[x_key])
        x_max = max(dict[x_key])
        step = int( (x_max-x_min)/width )
        dict2 = {x_key:[], y_key:[]}
        for sample in range(width):
            accum_x, accum_y = 0, 0
            for i in range(sample, step):
                accum_x += dict[x_key][i]
                accum_y += dict[y_key][i]
            dict2[x_key].append(accum_x)
            dict2[y_key].append(accum_y)
        return dict2
    def bitprint(current_y, x_list, y_list, xfill):
        for index, value in enumerate(x_list):
            if y_list[index] >= current_y :
                print('░'*xfill, end=(' '+'_'*(xfill-1)))
            else:
                print('', end='_'*2*xfill)
    def xyplot(dict, x_key, y_key, height):
        y_min = min(dict[y_key])
        y_max = max(dict[y_key])
        y_step = int( (y_max-y_min)/height )
        zfill_max = len(str(y_max))
        x_fill = len(str(dict[x_key][0]))
        for y_value in sorted(range(y_min, y_max+y_step,y_step), reverse=True):
            print(f'{str(y_value).zfill(zfill_max)}', end='  ')
            stats.bitprint(y_value, dict[x_key], dict[y_key], x_fill)
            print('', end='\n')
        print(' '*zfill_max, sep='', end='  ')
        for i in dict[x_key]:
            print(f'{i}', end=' '*x_fill)
        print('\n')
    def convert(list_of_dicts, keys_type, *keys):
        for row in list_of_dicts:
            for key in keys:
                row[key] = keys_type(row[key])
            

#print( stats.histogram(lst, 'year') )
#print( stats.average(lst, 'gross') )
#print(stats.clean(lst, 'gross', 400, 900)) # Numeric cleaning and clipping
#print('---------------------------')
#print(stats.clean(lst, 'rating')) # String cleaning
#print(stats.headers(lst)) # Headers of the data
#stats.convert_to(lst, str, 'year', 'gross')
#print(lst[:2])
#print('---------------------------')
#stats.convert_to(lst, int, 'year', 'gross')
#print(lst[:2])
xy = stats.series(lst1, 'year', 'gross')
stats.xyplot(xy, 'year', 'gross', 16)
#from time import sleep
#while True:
#    xy = stats.series(lst, 'year', 'gross')
#    stats.xyplot(xy, 'year', 'gross')
#    lst[10]['gross'] +=100
#    sleep(0.5)

#import csv
#with open('R-rated Horror Movies-appended.csv','r') as csv_file:
#    reader = csv.DictReader(csv_file)
#    big_list = []
#    for row in reader:
#        big_list.append(dict(row))
    
#print( big_list[0] )
#stats.convert(big_list, int, 'Year')
#one_dict = stats.histogram(big_list, 'Year')
#one_dict = dict(sorted( one_dict.items()))

#series = stats.series(one_dict)
#stats.xyplot(series, 'x', 'y')
#print(one_dict)
#print ('------------------')