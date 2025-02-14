import requests
import json
from statistics import mean
from collections import defaultdict

# List out my states from the united states of america!!! #PATRIOTISM
state_codes = [
    'ar', 'as', 'az', 'ca', 'co', 'ct', 'dc', 'de', 'fl', 'ga', 'gu', 'hi', 'ia', 'id', 
    'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'me', 'mi', 'mn', 'mo', 'mp', 'ms', 'mt', 
    'nc', 'nd', 'ne', 'nh', 'nj', 'nm', 'nv', 'ny', 'oh', 'ok', 'or', 'pa', 'pr', 'ri', 
    'sc', 'sd', 'tn', 'tx', 'ut', 'va', 'vi', 'vt', 'wa', 'wi', 'wv', 'wy'
]

# Data pull to get data (really the stats) about covid 
def fetch_state_data(state_code):
    url = f'https://api.covidtracking.com/v1/states/{state_code}/daily.json'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data for {state_code}")
        return None

#Dose the math to make the caulation from the stats pull
def calculate_statistics(state_data):
    new_cases = []
    dates_with_cases = []
    monthly_cases = defaultdict(int)
    
    max_new_cases = 0
    max_new_cases_date = ''
    most_recent_no_new_cases = None

    for entry in state_data:
        date = str(entry['date'])
        new_case = entry['positiveIncrease']
        
        # Finds new data (coivd cases)-"cough cough"
        new_cases.append(new_case)
        if new_case > 0:
            dates_with_cases.append(date)
        
        # Monthly Cluster or group
        month = date[:6]  # Year and month in format YYYYMM
        monthly_cases[month] += new_case
        
        # finds and traces new cases - "o I can't taste"
        if new_case > max_new_cases:
            max_new_cases = new_case
            max_new_cases_date = date
        
        # Traces most recent with no new cases - "now I'm vaccinated "
        if new_case == 0:
            most_recent_no_new_cases = date
    
   # Maths the AVG for all new cases - "cough cough"
    avg_new_cases = mean(new_cases) if new_cases else 0

    # Maths month with highest and lowest new cases
    max_month = max(monthly_cases, key=monthly_cases.get)
    min_month = min(monthly_cases, key=monthly_cases.get)

    # Makes it estetically pleaseing - eye candy format
    max_month_year = f"{max_month[:4]}-{max_month[4:]}"
    min_month_year = f"{min_month[:4]}-{min_month[4:]}"
    
    return avg_new_cases, max_new_cases_date, most_recent_no_new_cases, max_month_year, min_month_year

# Function to run the entire process for each individual state (Teaxs is still the best state though)
def main():
    for state_code in state_codes:
        state_data = fetch_state_data(state_code)
        
        if state_data:
            # Save to JSON data to a file
            with open(f"{state_code}.json", 'w') as json_file:
                json.dump(state_data, json_file, indent=4)
            
            # Maths the statistics for the state
            avg_new_cases, max_new_cases_date, most_recent_no_new_cases, max_month_year, min_month_year = calculate_statistics(state_data)
            
            # Print my findings "boom" (arm fold)
            print(f"Covid confirmed cases statistics for {state_code.upper()}:")
            print(f"  Average number of new daily confirmed cases: {avg_new_cases:.2f}")
            print(f"  Date with the highest new number of covid cases: {max_new_cases_date}")
            print(f"  Most recent date with no new covid cases: {most_recent_no_new_cases}")
            print(f"  Month and Year with the highest new number of covid cases: {max_month_year}")
            print(f"  Month and Year with the lowest new number of covid cases: {min_month_year}")
            print('-' * 80)

# Runs the program
if __name__ == "__main__":
    main()

