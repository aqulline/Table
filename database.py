import json


class DataBase:
    def load(self, name):
        with open(name, "r") as file:
            initial_data = json.load(file)
        return initial_data

    def write(self, data, file):
        with open(file, "w") as file:
            initial_data = json.dumps(data, indent=4)
            file.write(initial_data)

    def add_module(self, programme, module_name, module_code):
        data = self.load("datas/module.json")
        new_data = data[programme]
        modules_len = len(new_data)
        final = {f"module{modules_len + 1}": f"{module_code} {module_name}"}
        new_data.update(final)
        data[programme].update(new_data)
        self.write(data, "datas/module.json")
        print(new_data)

    def remove_module(self, programme, module):
        data = self.load("datas/module.json")
        data[programme].__delitem__(module)

        self.write(data, "datas/module.json")

    def edit_venue(self, venue, size):
        data = self.load("datas/venues.json")
        final_size = {'size': size}
        data[venue].update(final_size)

        self.write(data, "datas/venues.json")

    def add_venue(self, venue, size):
        data = self.load("datas/venues.json")
        final_size = {venue: {'size': size}}
        data.update(final_size)

        self.write(data, "datas/venues.json")
