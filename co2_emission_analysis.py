import csv
import time
import matplotlib.pyplot as plt

class CO2EmissionAnalysis:
    def __init__(self):
        with open('Emissions.csv', 'rt') as f:
            csv_data = csv.reader(f) # reads a csv file
            dictionary = {row[0]:row[1:] for row in csv_data}
        
        self.dictionary = dictionary
        self.keys = list(self.dictionary.keys())
        self.years = self.dictionary.get('CO2 per capita')
        self.countries = list(self.dictionary.keys())[1:]
    
    def show_data(self):
        for key, val in self.dictionary.items():
            print(f"{key} - {val}")
    
    def data_of_year(self, year):
        if year not in self.years:
            return 'Invalid Year! Try again.'
        
        desired_year = self.years.index(year)
        emmision_list = list()
        for val in self.dictionary.values():
            emmision_list.append(float(val[desired_year]))
        return emmision_list[1:] # this list does not include first value as that would be year

    def summary_of_year(self, year):
        required_list = self.data_of_year(year)

        max_index = required_list.index(max(required_list))+1 # +1 as required list has 1 less value
        min_index = required_list.index(min(required_list))+1 # +1 as required list has 1 less value
        avrg = sum(required_list)/len(required_list)
        
        print(f"\n=> In {year}, countries with minimum and maximum CO2 emission levels were, {self.keys[min_index]} and {self.keys[max_index]} respectively. The average CO2 emissions in {year} were {round(avrg, 2)}.")
    
    def visualize_stats_of(self, coutries: str):
        plot_list = list()
        for name in coutries:
            plot_list.append([float(i) for i in self.dictionary.get(name)])

        plt.suptitle('Year vs Emission in Capita')
        for i in plot_list:
            plt.plot(self.years, i)
        plt.legend(coutries)
        plt.xlabel('Year')
        plt.ylabel(f'Emission in Given Country(s)')
        plt.show()
    
    def extract_data(self, coutries: str):
        adding = [['CO2 per capita'] + self.years]
        for name in coutries:
            adding.append([name] + self.dictionary.get(name))
        
        with open('Emissions_subset.csv', 'w', newline='') as f:
            write_stats = csv.writer(f)
            write_stats.writerows(adding)
        print("Data added in file named, 'Emissions_subset.csv'")

    def is_available(self, countries: list):
        res = True
        for country in countries:
            if country not in self.countries:
                print(f'-> Data for {country} is not available. Each name should be typed again.\n')
                res = False
                break
        return res
    
    def valid_year(self, year: str):
        if not year.isdigit():
            print('-> Invalid year.\n')
            return False
        elif not 1997 <= int(year) <= 2010:
            print(f'-> No data are available for {year}..\n')
            return False
        else:
            return True
