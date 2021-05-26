import datetime
import locale
import pytz
dt = datetime.datetime.now()
print("{}:{}:{}".format(dt.hour,dt.minute,dt.second))
print("{}/{}/{}".format(dt.day,dt.month,dt.year))

dt.isoformat()
print(dt.strftime("%A %d %B %m %Y %I:%M"))
locale.setlocale(locale.LC_ALL,'es-AR')
print(dt.strftime("%A %d de %B %m del %Y %I:%M"))
print(dt.strftime("%A %d de %B %m del %Y -> %H:%M"))

t = datetime.timedelta(days=14, hours=4, seconds=1000)
dentro_de_dos_semanas = dt + t
print(dentro_de_dos_semanas.strftime("%A %d de %B %m del %Y -> %H:%M"))
for tz in pytz.all_timezones:
    print(tz)

zona_horaria = datetime.datetime.now(pytz.timezone("Asia/Tokyo"))
print(zona_horaria.strftime("%A %d de %B %m del %Y -> %H:%M"))
