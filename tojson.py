''' Creates from a day, month and year value a date-string which will be the
    x-axis of visualisation '''
def to_date_time(day, month, year):
    return "%02d.%02d.%04d" % (day, month, year)

''' Convert a string value into an int. the case of an error use 0 as default '''
def to_int_with_default(value):
    try:
        return int(value)
    except:
        return 0

''' Convert a string value into a float. the case of an error use 0.0 as default '''
def to_float_with_default(value):
    try:
        return float(value)
    except:
        return 0.0

''' Convert a list of values to a string representing a json array of int values '''
def to_json_int_array(label, values):
    s = "['" + label + "', "
    for value in values:
        s += str(to_int_with_default(value)) + ","
    s += "],\n"
    return s

''' Convert a list of values to a string representing a json array of float values '''
def to_json_float_array(label, values):
    s = "['" + label + "', "
    for value in values:
        s += str(to_float_with_default(value)) + ","
    s += "],\n"
    return s

''' Convert a list of values to a string representing a json array of string values '''
def to_json_string_array(label, values):
    s = "['" + label + "', "
    for value in values:
        s += "'" + value + "',"
    s += "],\n"
    return s

# input csv file containing the raw data
fh = open('airquality.csv')
# data exported as json
fh_out = open('airquality.json', 'w')

ozones = []
solars = []
winds = []
temps = []
date_times = []
first = True

for line in fh:
    # skip first line (which is the csv header line)
    if first:
        first = False
        continue

    # fill lists with column data
    (id, ozone, solar, wind, temp, month, day) = line.strip().split(',')
    # compose from the day and month a date string
    date_time = to_date_time(int(day), int(month), 1973)
    ozones.append(ozone)
    solars.append(solar)
    winds.append(wind)
    temps.append(temp)
    date_times.append(date_time)

fh_out.write('raw_data = [\n')
fh_out.write(to_json_string_array('x', date_times))
fh_out.write(to_json_int_array('Ozon', ozones))
fh_out.write(to_json_int_array('Solar R', solars))
fh_out.write(to_json_float_array('Wind', winds))
fh_out.write(to_json_int_array('Temp', temps))
fh_out.write('];\n')

fh.close()
fh_out.close()
