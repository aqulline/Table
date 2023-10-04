import json


def load(name):
    with open(name, "r") as file:
        initial_data = json.load(file)
    return initial_data


dt = [f"d{j}t{i}" for i in range(1, 8) for j in range(1, 7)]

data = load("datas/tble.json")
count = 0
temp_code = {}
v_dt = {}
with open("datas/table.html", "w") as html_file:
    html_file.write("<html>\n")
    html_file.write("<head>\n")
    html_file.write("<title>Timetable</title>\n")
    html_file.write \
        ("<style>table {width: 100%;border-collapse: collapse;}th, td {border: 1px solid #ddd;text-align: left;padding: 8px;}th {background-color: #f2f2f2;}.day-header {background-color: #ddd;}</style>\n")
    html_file.write("</head>\n")
    html_file.write("<body>\n")
    html_file.write("<h1>NATIONAL INSTITUTE OF TRANSPORT TEST 2 TIMETABLE FOR ACADEMIC YEAR 2022_2023</h1>\n")

    for program in data:
        html_file.write(f"<h2>{program}</h2>\n")
        html_file.write("<table>\n")
        html_file.write("<thead>\n")
        html_file.write(
            "<tr><th>day/time</th><th>t1</th><th>t2</th><th>t3</th><th>t4</th><th>t5</th><th>t6</th><th>t7</th></tr>\n")
        html_file.write("</thead>")
        html_file.write("<tbody>\n")

        # print(data[program])
        for i in data[program]:
            period_one = data[program][i]["period_one_dt"]
            period_two = data[program][i]["period_two_dt"]

            if period_one not in temp_code:
                temp_code[period_one] = {}

            temp_code[period_one] = i

            if period_two not in temp_code:
                temp_code[period_two] = {}

            temp_code[period_two] = i

        for i in range(1, 7):
            html_file.write("<tr>\n")
            html_file.write(f"<td>d{i}</td>\n")
            for k in range(1, 8):
                count += 1
                conc = f"d{i}t{count}"
                conc2 = f"d{i}t{count}"
                if conc in temp_code:
                    html_file.write(f"<td>{temp_code[conc]}</td>\n")
                else:
                    html_file.write(f"<td>{conc}</td>\n")
            count = 0
            html_file.write("</tr>\n")
        temp_code = {}
        html_file.write("</tbody>\n")
        html_file.write("</table/> \n")
    html_file.write("</body></html>")
