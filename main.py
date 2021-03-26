import json


class CountryLinks:

    def __init__(self, file_name):
        with open(file_name, "r") as f:
            self.countries = json.load(f)
            self.start = -1
            self.end = len(self.countries)

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start == self.end:
            raise StopIteration
        country = self.countries[self.start]
        country_name = country["name"]["common"]
        text = country_name + ' - ' + 'https://en.wikipedia.org/wiki' + '/' + '_'.join(country_name.split())
        return text


with open('country_names.txt', 'w') as country_names_file:
    for country_link in CountryLinks('countries.json'):  # итерируемя по ссылкам
        country_names_file.write(f'{country_link}\n')  # и пишем их в файл


