import json


def load(name):
    with open(name, "r") as file:
        initial_data = json.load(file)
    return initial_data


def write(data):
    with open("datas/ue_table.html", "w") as file:
        # initial_data = json.dumps(data, indent=4)
        file.write(data)


# Sample JSON data
data = load("datas/ue.json")

# Start generating the HTML table
html_table = '<table>'

# Iterate through the JSON data to populate the table rows
for program, modules in data.items():
    html_table += f'<thead><tr><th>{program}</th></tr></thead>'
    html_table += '<thead><tr><th>Module</th><th>Venue</th><th>Day</th><th>Time</th><th>Week</th><th>Students Size</th><th>Venue Size</th></tr></thead>'
    for module, details in modules.items():
        html_table += '<tbody>'
        html_table += '<tr>'
        html_table += f'<td>{module}</td>'
        html_table += f'<td>{details["venue"]}</td>'
        html_table += f'<td>{details["day"]}</td>'
        html_table += f'<td>{details["time"]}</td>'
        html_table += f'<td>{details["week"]}</td>'
        html_table += f'<td>{details["students_size"]}</td>'
        html_table += f'<td>{details["venue_size"]}</td>'
        html_table += '</tr>'

# Close the HTML table
html_table += '</tbody></table>'

# Print or save the generated HTML table
print(html_table)

write(html_table)
