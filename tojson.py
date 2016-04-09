def to_date_time(day, month, year):
    return "%02d.%02d.%04d" % (day, month, year)

def to_int_with_default(value):
    try:
        return int(value)
    except:
        return 0

def to_float_with_default(value):
    try:
        return float(value)
    except:
        return 0.0

def to_json_int_array(label, values):
    to_int = lambda value: str(to_int_with_default(value))
    return to_json_array(label, values, to_int)

def to_json_float_array(label, values):
    to_int = lambda value: str(to_float_with_default(value))
    return to_json_array(label, values, to_int)

def to_json_string_array(label, values):
    to_int = lambda value: "'" + value + "'"
    return to_json_array(label, values, to_int)

def to_json_array(label, values, my_func):
    s = "['" + label + "', "
    for value in values:
        s += my_func(value) + ","
    s += "],\n"
    return s

fh = open('airquality.csv')
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
