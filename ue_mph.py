import json
import random

mph = [['w1;MPH 01 - B 22;Monday;07:00-08:00', 'w1;MPH 01 - B 22;Monday;08:00-08:30',
        'w1;MPH 01 - B 22;Monday;08:30-09:30', 'w1;MPH 01 - B 22;Monday;09:30-10:00',
        'w1;MPH 01 - B 22;Monday;10:00-11:00', 'w1;MPH 01 - B 22;Monday;11:00-11:30',
        'w1;MPH 01 - B 22;Monday;11:30-12:30', 'w1;MPH 01 - B 22;Monday;12:30-13:00',
        'w1;MPH 01 - B 22;Monday;13:00-14:00', 'w1;MPH 01 - B 22;Monday;14:00-14:30',
        'w1;MPH 01 - B 22;Monday;14:30-15:30', 'w1;MPH 01 - B 22;Monday;15:30-16:00',
        'w1;MPH 01 - B 22;Monday;16:00-17:00', 'w1;MPH 01 - B 22;Monday;17:00-17:30',
        'w1;MPH 01 - B 22;Monday;17:30-18:30'],
       ['w2;MPH 01 - B 22;Monday;07:00-08:00', 'w2;MPH 01 - B 22;Monday;08:00-08:30',
        'w2;MPH 01 - B 22;Monday;08:30-09:30', 'w2;MPH 01 - B 22;Monday;09:30-10:00',
        'w2;MPH 01 - B 22;Monday;10:00-11:00', 'w2;MPH 01 - B 22;Monday;11:00-11:30',
        'w2;MPH 01 - B 22;Monday;11:30-12:30', 'w2;MPH 01 - B 22;Monday;12:30-13:00',
        'w2;MPH 01 - B 22;Monday;13:00-14:00', 'w2;MPH 01 - B 22;Monday;14:00-14:30',
        'w2;MPH 01 - B 22;Monday;14:30-15:30', 'w2;MPH 01 - B 22;Monday;15:30-16:00',
        'w2;MPH 01 - B 22;Monday;16:00-17:00', 'w2;MPH 01 - B 22;Monday;17:00-17:30',
        'w2;MPH 01 - B 22;Monday;17:30-18:30'],
       ['w1;MPH 01 - B 22;Tuesday;07:00-08:00', 'w1;MPH 01 - B 22;Tuesday;08:00-08:30',
        'w1;MPH 01 - B 22;Tuesday;08:30-09:30', 'w1;MPH 01 - B 22;Tuesday;09:30-10:00',
        'w1;MPH 01 - B 22;Tuesday;10:00-11:00', 'w1;MPH 01 - B 22;Tuesday;11:00-11:30',
        'w1;MPH 01 - B 22;Tuesday;11:30-12:30', 'w1;MPH 01 - B 22;Tuesday;12:30-13:00',
        'w1;MPH 01 - B 22;Tuesday;13:00-14:00', 'w1;MPH 01 - B 22;Tuesday;14:00-14:30',
        'w1;MPH 01 - B 22;Tuesday;14:30-15:30', 'w1;MPH 01 - B 22;Tuesday;15:30-16:00',
        'w1;MPH 01 - B 22;Tuesday;16:00-17:00', 'w1;MPH 01 - B 22;Tuesday;17:00-17:30',
        'w1;MPH 01 - B 22;Tuesday;17:30-18:30'],
       ['w2;MPH 01 - B 22;Tuesday;07:00-08:00', 'w2;MPH 01 - B 22;Tuesday;08:00-08:30',
        'w2;MPH 01 - B 22;Tuesday;08:30-09:30', 'w2;MPH 01 - B 22;Tuesday;09:30-10:00',
        'w2;MPH 01 - B 22;Tuesday;10:00-11:00', 'w2;MPH 01 - B 22;Tuesday;11:00-11:30',
        'w2;MPH 01 - B 22;Tuesday;11:30-12:30', 'w2;MPH 01 - B 22;Tuesday;12:30-13:00',
        'w2;MPH 01 - B 22;Tuesday;13:00-14:00', 'w2;MPH 01 - B 22;Tuesday;14:00-14:30',
        'w2;MPH 01 - B 22;Tuesday;14:30-15:30', 'w2;MPH 01 - B 22;Tuesday;15:30-16:00',
        'w2;MPH 01 - B 22;Tuesday;16:00-17:00', 'w2;MPH 01 - B 22;Tuesday;17:00-17:30',
        'w2;MPH 01 - B 22;Tuesday;17:30-18:30'],
       ['w1;MPH 01 - B 22;Wednesday;07:00-08:00', 'w1;MPH 01 - B 22;Wednesday;08:00-08:30',
        'w1;MPH 01 - B 22;Wednesday;08:30-09:30', 'w1;MPH 01 - B 22;Wednesday;09:30-10:00',
        'w1;MPH 01 - B 22;Wednesday;10:00-11:00', 'w1;MPH 01 - B 22;Wednesday;11:00-11:30',
        'w1;MPH 01 - B 22;Wednesday;11:30-12:30', 'w1;MPH 01 - B 22;Wednesday;12:30-13:00',
        'w1;MPH 01 - B 22;Wednesday;13:00-14:00', 'w1;MPH 01 - B 22;Wednesday;14:00-14:30',
        'w1;MPH 01 - B 22;Wednesday;14:30-15:30', 'w1;MPH 01 - B 22;Wednesday;15:30-16:00',
        'w1;MPH 01 - B 22;Wednesday;16:00-17:00', 'w1;MPH 01 - B 22;Wednesday;17:00-17:30',
        'w1;MPH 01 - B 22;Wednesday;17:30-18:30'],
       ['w2;MPH 01 - B 22;Wednesday;07:00-08:00', 'w2;MPH 01 - B 22;Wednesday;08:00-08:30',
        'w2;MPH 01 - B 22;Wednesday;08:30-09:30', 'w2;MPH 01 - B 22;Wednesday;09:30-10:00',
        'w2;MPH 01 - B 22;Wednesday;10:00-11:00', 'w2;MPH 01 - B 22;Wednesday;11:00-11:30',
        'w2;MPH 01 - B 22;Wednesday;11:30-12:30', 'w2;MPH 01 - B 22;Wednesday;12:30-13:00',
        'w2;MPH 01 - B 22;Wednesday;13:00-14:00', 'w2;MPH 01 - B 22;Wednesday;14:00-14:30',
        'w2;MPH 01 - B 22;Wednesday;14:30-15:30', 'w2;MPH 01 - B 22;Wednesday;15:30-16:00',
        'w2;MPH 01 - B 22;Wednesday;16:00-17:00', 'w2;MPH 01 - B 22;Wednesday;17:00-17:30',
        'w2;MPH 01 - B 22;Wednesday;17:30-18:30'],
       ['w1;MPH 01 - B 22;Thursday;07:00-08:00', 'w1;MPH 01 - B 22;Thursday;08:00-08:30',
        'w1;MPH 01 - B 22;Thursday;08:30-09:30', 'w1;MPH 01 - B 22;Thursday;09:30-10:00',
        'w1;MPH 01 - B 22;Thursday;10:00-11:00', 'w1;MPH 01 - B 22;Thursday;11:00-11:30',
        'w1;MPH 01 - B 22;Thursday;11:30-12:30', 'w1;MPH 01 - B 22;Thursday;12:30-13:00',
        'w1;MPH 01 - B 22;Thursday;13:00-14:00', 'w1;MPH 01 - B 22;Thursday;14:00-14:30',
        'w1;MPH 01 - B 22;Thursday;14:30-15:30', 'w1;MPH 01 - B 22;Thursday;15:30-16:00',
        'w1;MPH 01 - B 22;Thursday;16:00-17:00', 'w1;MPH 01 - B 22;Thursday;17:00-17:30',
        'w1;MPH 01 - B 22;Thursday;17:30-18:30'],
       ['w2;MPH 01 - B 22;Thursday;07:00-08:00', 'w2;MPH 01 - B 22;Thursday;08:00-08:30',
        'w2;MPH 01 - B 22;Thursday;08:30-09:30', 'w2;MPH 01 - B 22;Thursday;09:30-10:00',
        'w2;MPH 01 - B 22;Thursday;10:00-11:00', 'w2;MPH 01 - B 22;Thursday;11:00-11:30',
        'w2;MPH 01 - B 22;Thursday;11:30-12:30', 'w2;MPH 01 - B 22;Thursday;12:30-13:00',
        'w2;MPH 01 - B 22;Thursday;13:00-14:00', 'w2;MPH 01 - B 22;Thursday;14:00-14:30',
        'w2;MPH 01 - B 22;Thursday;14:30-15:30', 'w2;MPH 01 - B 22;Thursday;15:30-16:00',
        'w2;MPH 01 - B 22;Thursday;16:00-17:00', 'w2;MPH 01 - B 22;Thursday;17:00-17:30',
        'w2;MPH 01 - B 22;Thursday;17:30-18:30'],
       ['w1;MPH 01 - B 22;Friday;07:00-08:00', 'w1;MPH 01 - B 22;Friday;08:00-08:30',
        'w1;MPH 01 - B 22;Friday;08:30-09:30', 'w1;MPH 01 - B 22;Friday;09:30-10:00',
        'w1;MPH 01 - B 22;Friday;10:00-11:00', 'w1;MPH 01 - B 22;Friday;11:00-11:30',
        'w1;MPH 01 - B 22;Friday;11:30-12:30', 'w1;MPH 01 - B 22;Friday;12:30-13:00',
        'w1;MPH 01 - B 22;Friday;13:00-14:00', 'w1;MPH 01 - B 22;Friday;14:00-14:30',
        'w1;MPH 01 - B 22;Friday;14:30-15:30', 'w1;MPH 01 - B 22;Friday;15:30-16:00',
        'w1;MPH 01 - B 22;Friday;16:00-17:00', 'w1;MPH 01 - B 22;Friday;17:00-17:30',
        'w1;MPH 01 - B 22;Friday;17:30-18:30'],
       ['w2;MPH 01 - B 22;Friday;07:00-08:00', 'w2;MPH 01 - B 22;Friday;08:00-08:30',
        'w2;MPH 01 - B 22;Friday;08:30-09:30', 'w2;MPH 01 - B 22;Friday;09:30-10:00',
        'w2;MPH 01 - B 22;Friday;10:00-11:00', 'w2;MPH 01 - B 22;Friday;11:00-11:30',
        'w2;MPH 01 - B 22;Friday;11:30-12:30', 'w2;MPH 01 - B 22;Friday;12:30-13:00',
        'w2;MPH 01 - B 22;Friday;13:00-14:00', 'w2;MPH 01 - B 22;Friday;14:00-14:30',
        'w2;MPH 01 - B 22;Friday;14:30-15:30', 'w2;MPH 01 - B 22;Friday;15:30-16:00',
        'w2;MPH 01 - B 22;Friday;16:00-17:00', 'w2;MPH 01 - B 22;Friday;17:00-17:30',
        'w2;MPH 01 - B 22;Friday;17:30-18:30'],
       ['w1;MPH 01 - B 22;Saturday;07:00-08:00', 'w1;MPH 01 - B 22;Saturday;08:00-08:30',
        'w1;MPH 01 - B 22;Saturday;08:30-09:30', 'w1;MPH 01 - B 22;Saturday;09:30-10:00',
        'w1;MPH 01 - B 22;Saturday;10:00-11:00', 'w1;MPH 01 - B 22;Saturday;11:00-11:30',
        'w1;MPH 01 - B 22;Saturday;11:30-12:30', 'w1;MPH 01 - B 22;Saturday;12:30-13:00',
        'w1;MPH 01 - B 22;Saturday;13:00-14:00', 'w1;MPH 01 - B 22;Saturday;14:00-14:30',
        'w1;MPH 01 - B 22;Saturday;14:30-15:30', 'w1;MPH 01 - B 22;Saturday;15:30-16:00',
        'w1;MPH 01 - B 22;Saturday;16:00-17:00', 'w1;MPH 01 - B 22;Saturday;17:00-17:30',
        'w1;MPH 01 - B 22;Saturday;17:30-18:30'],
       ['w2;MPH 01 - B 22;Saturday;07:00-08:00', 'w2;MPH 01 - B 22;Saturday;08:00-08:30',
        'w2;MPH 01 - B 22;Saturday;08:30-09:30', 'w2;MPH 01 - B 22;Saturday;09:30-10:00',
        'w2;MPH 01 - B 22;Saturday;10:00-11:00', 'w2;MPH 01 - B 22;Saturday;11:00-11:30',
        'w2;MPH 01 - B 22;Saturday;11:30-12:30', 'w2;MPH 01 - B 22;Saturday;12:30-13:00',
        'w2;MPH 01 - B 22;Saturday;13:00-14:00', 'w2;MPH 01 - B 22;Saturday;14:00-14:30',
        'w2;MPH 01 - B 22;Saturday;14:30-15:30', 'w2;MPH 01 - B 22;Saturday;15:30-16:00',
        'w2;MPH 01 - B 22;Saturday;16:00-17:00', 'w2;MPH 01 - B 22;Saturday;17:00-17:30',
        'w2;MPH 01 - B 22;Saturday;17:30-18:30']]


def write(data):
    with open("datas/ue.json", "w") as file:
        initial_data = json.dumps(data, indent=4)
        file.write(initial_data)


def load(name):
    with open(name, "r") as file:
        initial_data = json.load(file)
    return initial_data


vnue = load("datas/venuea120.json")

data = load("datas/Ue.json")

tl = len(mph)
for i in data:
    for k in data[i]:
        for j in data[i][k]:
            size = data[i][k]["students_size"]
            vsize = data[i][k]["venue_size"]
            vname = data[i][k]["venue"]
            week = data[i][k]["week"]
            day = data[i][k]["day"]
            time = data[i][k]["time"]
            prog = data[i][k]["program"]

            conc = f"{week};{vname};{day};{time}"

            if "MPH" in conc:
                cnt = mph.count(conc)
                sas = [g for g in mph if conc in g]
                if len(sas) > 0:
                    mph[mph.index(sas[0])].remove(conc)
                    # print(prog,mph[mph.index(sas[0])])
already = []

new_data = {}

for i in data:
    for k in data[i]:
        for j in data[i][k]:
            size = data[i][k]["students_size"]
            vsize = data[i][k]["venue_size"]
            vname = data[i][k]["venue"]
            week = data[i][k]["week"]
            day = data[i][k]["day"]
            time = data[i][k]["time"]
            prog = data[i][k]["program"]
            module = data[i][k]["module"]

            conc = f"{week};{vname};{day};{time}"

            if int(size) - int(vsize) > 10 and int(size) >= 200:

                if prog not in already:
                    vnl = random.choice(mph)
                    vnee = random.choice(vnl)

                    mph[mph.index(vnl)].remove(vnee)

                    w, v, d, t = vnee.strip().split(";")[0], vnee.strip().split(";")[1], vnee.strip().split(";")[2], \
                        vnee.strip().split(";")[3]

                    svn = vnue[v]["size"]

                    already.append(prog)
                    if prog not in new_data:
                        new_data[prog] = {}

                    new_data[prog][module] = {
                        "venue": v,
                        "day": d,
                        "time": t,
                        "week": w,
                        "module": module,
                        "program": prog,
                        "students_size": size,
                        "venue_size": svn
                    }
            else:
                if prog not in already:
                    if prog not in new_data:
                        new_data[prog] = {}

                    new_data[prog][module] = {
                        "venue": vname,
                        "day": day,
                        "time": time,
                        "week": week,
                        "module": module,
                        "program": prog,
                        "students_size": size,
                        "venue_size": vsize
                    }

write(new_data)
