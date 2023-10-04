import json
import random


class VenueDistribution:
    venue_day_time_b50 = []

    venue_day_time_a50 = []

    venue_day_time_a120 = []

    venue_day_time_b120 = []

    table_time = []

    w_v_d_t = ""

    days = [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"
    ]

    weeks = ["w"]

    b50_taken = []
    a50_taken = []
    b120_taken = []
    a120_taken = []

    def assign_venue(self, size):
        size = int(size)
        if size < 40:
            data = self.venue_day_time_b50
            rnd_venue_list = random.randint(0, len(data) - 1)
            w_v_d_t = random.choice(data[rnd_venue_list])
            while self.b50_taken.count(w_v_d_t.strip().split(";")[1]) > 19:
                rnd_venue_list = random.randint(0, len(data) - 1)
                w_v_d_t = random.choice(data[rnd_venue_list])
                print("error 21 b50")
            self.b50_taken.append(w_v_d_t.strip().split(";")[1])
            data[rnd_venue_list].remove(w_v_d_t)
            self.w_v_d_t = w_v_d_t
        elif 70 >= size > 40:
            data = self.venue_day_time_a50
            rnd_venue_list = random.randint(0, len(data) - 1)
            w_v_d_t = random.choice(data[rnd_venue_list])
            while self.a50_taken.count(w_v_d_t.strip().split(";")[1]) > 19:
                rnd_venue_list = random.randint(0, len(data) - 1)
                w_v_d_t = random.choice(data[rnd_venue_list])
                print("error 21 a50")
            self.a50_taken.append(w_v_d_t.strip().split(";")[1])
            data[rnd_venue_list].remove(w_v_d_t)
            self.w_v_d_t = w_v_d_t

        elif 150 >= size > 70:
            data = self.venue_day_time_b120
            rnd_venue_list = random.randint(0, len(data) - 1)
            w_v_d_t = random.choice(data[rnd_venue_list])
            while self.b120_taken.count(w_v_d_t.strip().split(";")[1]) > 19:
                rnd_venue_list = random.randint(0, len(data) - 1)
                w_v_d_t = random.choice(data[rnd_venue_list])
                print("error 21 b120")
            self.b120_taken.append(w_v_d_t.strip().split(";")[1])
            data[rnd_venue_list].remove(w_v_d_t)
            self.w_v_d_t = w_v_d_t

        elif size > 150:
            data = self.venue_day_time_a120
            rnd_venue_list = random.randint(0, len(data) - 1)
            w_v_d_t = random.choice(data[rnd_venue_list])
            while self.a120_taken.count(w_v_d_t.strip().split(";")[1]) > 19:
                rnd_venue_list = random.randint(0, len(data) - 1)
                w_v_d_t = random.choice(data[rnd_venue_list])
                print("error 21 a120")
            self.a120_taken.append(w_v_d_t.strip().split(";")[1])
            data[rnd_venue_list].remove(w_v_d_t)
            self.w_v_d_t = w_v_d_t

    def get_wvdt(self, wvdt):
        return wvdt

    def set_venues(self):
        self.venue_b50()
        self.venue_a50()
        self.venue_b120()
        self.venue_a120()

    def venue_b50(self):
        vnb50 = self.load("datas/venueb50.json")
        venuesb50 = [i for i in vnb50.keys()]
        self.venue_day_time_b50 = [[f"{h};{i};{k};{j}" for j in self.get_time(7, 21, 3)] for k in self.days
                                   for i in venuesb50 for h in self.weeks]
        return self.venue_day_time_b50

    def venue_a50(self):
        vna50 = self.load("datas/venuea50.json")
        venuea50 = [i for i in vna50.keys()]
        self.venue_day_time_a50 = [[f"{h};{i};{k};{j}" for j in self.get_time(7, 21, 3)] for k in self.days
                                   for i in venuea50 for h in self.weeks]

        return self.venue_day_time_a50

    def venue_a120(self):
        vna120 = self.load("datas/venuea120.json")
        venuea120 = [i for i in vna120.keys()]
        self.venue_day_time_a120 = [[f"{h};{i};{k};{j}" for j in self.get_time(7, 21, 3)] for k in self.days
                                    for i in venuea120 for h in self.weeks]

        return self.venue_day_time_a120

    def venue_b120(self):
        vnb120 = self.load("datas/venueb120.json")
        venueb120 = [i for i in vnb120.keys()]
        self.venue_day_time_b120 = [[f"{h};{i};{k};{j}" for j in self.get_time(7, 21, 3)] for k in self.days
                                    for i in venueb120 for h in self.weeks]

        return self.venue_day_time_b120

    def get_time(self, time_in, time_out, ranges):
        ti_di = time_out - time_in
        for i in range(int(ti_di / (ranges - 1))):
            times = f"{time_in}:00"
            for j in range(ranges - 1):
                time_in += 1
            times = f"{times}-{time_in}:00"

            self.table_time.append(times)

        return self.table_time

    def load(self, name):
        with open(name, "r") as file:
            initial_data = json.load(file)
        return initial_data


class Timetable:
    timetable = {}

    days = [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"
    ]

    days_dict = {'Monday': 'd1', 'Tuesday': 'd2', 'Wednesday': 'd3', 'Thursday': 'd4', 'Friday': 'd5', 'Saturday': 'd6'}

    weeks = []

    table_time = []

    time_dict = {'7:00-9:00': 't1', '9:00-11:00': 't2', '11:00-13:00': 't3', '13:00-15:00': 't4', '15:00-17:00': 't5',
                 '17:00-19:00': 't6', '19:00-21:00': 't7'}

    venue_day_time_100 = []

    venue_day_time_10 = []

    venue_day_time_b50 = []

    venue_day_time_a50 = []

    venue_day_time_a120 = []

    venue_day_time_b120 = []

    taken_venue_day_list = []

    taken_programme_day = []

    taken_module_day = []

    day_time_id = []

    default_table = {}

    def get_code(self):
        pass

    def get_size(self, text):
        import re

        pattern = r'^(.*?)\s*\((\d+)\)$'

        match = re.match(pattern, text)

        if match:
            extracted_text = match.group(1).strip()
            extracted_number = match.group(2)

            return extracted_number
        else:
            print("No match found.")

    def load(self, name):
        with open(name, "r") as file:
            initial_data = json.load(file)
        return initial_data

    def write(self, data):
        with open("datas/tble.json", "w") as file:
            initial_data = json.dumps(data, indent=4)
            file.write(initial_data)

    def venue_b50(self):
        vnb50 = self.load("datas/venueb50.json")
        venuesb50 = [i for i in vnb50.keys()]
        self.venue_day_time_b50 = [[f"{h};{i};{k};{j}" for j in self.table_time] for k in self.days
                                   for i in venuesb50 for h in self.weeks]
        return self.venue_day_time_b50

    def venue_a50(self):
        vna50 = self.load("datas/venuea50.json")
        venuea50 = [i for i in vna50.keys()]
        self.venue_day_time_a50 = [[f"{h};{i};{k};{j}" for j in self.table_time] for k in self.days
                                   for i in venuea50 for h in self.weeks]

        return self.venue_day_time_a50

    def venue_a120(self):
        vna120 = self.load("datas/venuea120.json")
        venuea120 = [i for i in vna120.keys()]
        venue_day_time_a120 = [[f"{h};{i};{k};{j}" for j in self.table_time] for k in self.days
                               for i in venuea120 for h in self.weeks]

        return venue_day_time_a120

    def venue_b120(self):
        vnb120 = self.load("datas/venueb120.json")
        venueb120 = [i for i in vnb120.keys()]
        self.venue_day_time_b120 = [[f"{h};{i};{k};{j}" for j in self.table_time] for k in self.days
                                    for i in venueb120 for h in self.weeks]

        return self.venue_day_time_b120

    def get_programmes(self):
        programes = self.load("datas/module.json")
        programmes = [i for i in
                      programes.keys()]

        return programmes

    def get_modules(self):
        modules = self.load("datas/module.json")

        modules_lits = [[modules[i][j].strip() for j in modules[i]]
                        for i in modules]

        return modules_lits

    def match_table(self, venue_day_time):
        test = venue_day_time
        day = self.days_dict[test.strip().split(";")[1]]
        time = self.time_dict[test.strip().split(";")[2]]

        dt = f"{day}{time}"

        return dt

    def get_time(self, time_in, time_out, ranges):
        ti_di = time_out - time_in
        for i in range(int(ti_di / (ranges - 1))):
            times = f"{time_in}:00"
            for j in range(ranges - 1):
                time_in += 1
            times = f"{times}-{time_in}:00"

            self.table_time.append(times)

        return self.table_time

    def get_default_table(self):
        default_table = self.load("datas/ble.json")

        return default_table

    def set_venue_day(self):

        self.day_time_id = [f"{i};{j}" for j in self.get_time(7, 21, 3) for i in self.days]

        return self.day_time_id

    def set_venue_day_time(self, venue, programme, module, modul_cnt):

        day_time = random.choice(self.set_venue_day())
        venue_day_time = f"{venue};{day_time}"

        while venue_day_time in self.taken_venue_day_list:
            day_time = random.choice(self.set_venue_day())
            venue_day_time = f"{venue};{day_time}"
            print("ve error", venue_day_time, self.taken_venue_day_list.count(venue_day_time))

        programme_day = f"{programme}{day_time.strip().split(';')[0]}"

        count_prog = self.taken_programme_day.count(programme_day)

        while self.taken_programme_day.count(programme_day) > 3:
            day_time = random.choice(self.set_venue_day())
            venue_day_time = f"{venue};{day_time}"
            programme_day = f"{programme}{day_time.strip().split(';')[0]}"
            # self.set_venue_day_time(venue, programme, module)
            print("pro error", programme)
        module_rept = self.taken_module_day.count(f"{module}{day_time.strip().split(';')[0]}")
        while self.taken_module_day.count(
                f"{programme}{module}{day_time.strip().split(';')[0]}") == 1 and modul_cnt < 8:
            day_time = random.choice(self.set_venue_day())
            venue_day_time = f"{venue};{day_time}"
            programme_day = f"{programme}{day_time.strip().split(';')[0]}"
            # self.set_venue_day_time(venue, programme, module)
            print("modu error", programme, modul_cnt)

        self.taken_module_day.append(f"{programme}{module}{day_time.strip().split(';')[0]}")
        self.taken_venue_day_list.append(venue_day_time)
        self.taken_programme_day.append(programme_day)

        return venue_day_time

    error_list = []

    def set_venue_b21(self):
        venue_distri = VenueDistribution()
        venue_distri.set_venues()
        self.default_table = self.load("datas/tble.json")
        for i in self.default_table:
            # print(i)
            programme_size = self.get_size(i)
            for j in self.default_table[i]:
                venue_distri.assign_venue(programme_size)
                module_venue = venue_distri.w_v_d_t.strip().split(";")[1]
                if i not in self.timetable:
                    self.timetable[i] = {}

                self.timetable[i][j] = {
                    "venue": module_venue,
                    "module": j,
                    "program": i,
                }

        self.write(self.timetable)

    final_table = {}

    def generate_table(self):
        self.set_venue_b21()
        self.default_table = self.load("datas/tble.json")
        for i in self.default_table:
            for j in self.default_table[i]:
                module_count = len(self.default_table[i])
                venue = self.default_table[i][j]["venue"]
                period_one = self.set_venue_day_time(venue, i, j, module_count)
                period_two = self.set_venue_day_time(venue, i, j, module_count)
                period_one_dt = self.match_table(period_one)
                period_two_dt = self.match_table(period_two)

                if i not in self.final_table:
                    self.final_table[i] = {}

                self.final_table[i][j] = {
                    "venue": venue,
                    "module": j,
                    "program": i,
                    "period_one": period_one,
                    "period_two": period_two,
                    "period_one_dt": period_one_dt,
                    "period_two_dt": period_two_dt
                }

        self.write(self.final_table)
        import to_html


