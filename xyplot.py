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

def bitprint(current_y, x_list, y_list, xfill):
    for index, value in enumerate(x_list):
        if y_list[index] >= current_y :
            print('░'*xfill, end=(' '+'_'*(xfill-1)))
        else:
            print('', end='_'*2*xfill)

def xyplot(dict, x_key, y_key, height):
    y_min = int(min(dict[y_key]))
    y_max = int(max(dict[y_key]))
    y_step = int( (y_max-y_min)/height )
    zfill_max = len(str(y_max))
    x_fill = len(str(dict[x_key][-1]))
    for y_value in sorted(range(y_min, y_max+y_step,y_step), reverse=True):
        print(f'{str(y_value).zfill(zfill_max)}', end='  ')
        bitprint(y_value, dict[x_key], dict[y_key], x_fill)
        print('', end='\n')
    print(' '*zfill_max, sep='', end='  ')
    for i in dict[x_key]:
        print(f'{i}', end=' '*x_fill)
    print('\n')

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
    {'title':'Movie5', 'year':2026, 'rating':'R', 'gross':0}
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
    {'country':'JPN', 'population':126476461,  'lang':'jp', 'urban':92}
    ]

# Lists (lst1 - lst2) are in a similar format to what python's csv module can read
# One way to prepare data for plotting is to make a series of { x:[x1,x2, ..] , y:[y1, y2, ..] }
# Using function series() you can do just that. 
world_data = series(lst2, 'population', 'urban', 'country', 'lang')
movie_data = series(lst1, 'year', 'gross')

# Try replace 'country' by 'lang' or 'urban'
# Also try to change 'height' parameter
xyplot(world_data, 'country', 'population', height=16)

#xyplot(movie_data, 'year', 'gross', height=16)

# Interactive Sinusoidal plot
from time import sleep
from math import sin

start, end = 100, 180
while False: # Change to while True to start the animation. Weights in the sin() formula only to make it look good on a plot
    x_list = [x for x in range(start,end,10)]
    y_list = [(10+10*sin(0.1*x)) for x in x_list]
    d = { 'x': x_list , 'y': y_list }
    xyplot(d, 'x', 'y', 16)
    start += 1
    end += 1
    sleep(0.07)
