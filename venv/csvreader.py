import datetime
import csv

#get operating time and returns opening and closing timing in a tuple of len 4
def get_operating_time (stall_name):
  with open('stall_info\\operating_hours.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=",")
    for row in readCSV:
      if stall_name in row:
        open_hours = int(row[1])
        open_mins = int(row[2])
        close_hours = int(row[3])
        close_mins = int(row[4])
        return (open_hours, open_mins, close_hours, close_mins)
      else:
        continue

def get_menu(stall_name):
  opn_time = get_operating_time(stall_name)
  dtime_now = datetime.datetime.now()  #default datetime
  #dtime_now = dtime_now.replace(day=21, hour=13, minute=0, second=0, microsecond=0)  #for overwriting dtime_now with user input
  dtime_12pm = dtime_now.replace(hour=12, minute=0, second=0, microsecond=0)
  dtime_open = dtime_now.replace(hour=opn_time[0], minute=opn_time[1], second=0, microsecond=0)
  dtime_close = dtime_now.replace(hour=opn_time[2], minute=opn_time[3], second=0, microsecond=0)
  day = str(dtime_now.isoweekday())

  if dtime_now < dtime_12pm:
    meal = "breakfast"
  else:
    meal = "lunch"
  filename = day + "_" + meal + ".csv"

  if dtime_now < dtime_open or dtime_now > dtime_close:
    print("The store is now closed")
  else:
    try:
      with open('stall_info\{}\{}'.format(stall_name, filename)) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=",")
        for row in readCSV:
          print(row)
    except:
      with open('stall_info\{}\default_menu.csv'.format(stall_name)) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=",")
        for row in readCSV:
          print(row)
get_menu("korean")