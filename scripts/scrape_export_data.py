# ----------------------------------------------------
# scrapes historical Avalanche Canada conditions, historical forecast conditions, and problem text from AvalancheCanada.ca and exports to CSV files
#
# author David Hurley
# email hurleyldave@gmail.com
# date October 08 2020
# ----------------------------------------------------

import json
import pandas as pd
from helper import scrape

# read user inputs
with open('scrape_inputs.json', 'r') as f:
    inputs = json.load(f)

# format list of dates to scrape avy can data for
dates_to_scrape = pd.date_range(inputs['start_date'], inputs['end_date'])
months_to_scrape = [1, 2, 3, 4, 11, 12]  # only scrape months when avalanche canada forecasts
dates_to_scrape = dates_to_scrape[dates_to_scrape.month.isin(months_to_scrape)]

# function to open selenium web driver and scrape avalanche canada data for each specified date
conditions_today, conditions_today_plus1, conditions_today_plus2, problems = scrape(dates_to_scrape, inputs['region'], inputs['show_browser_window'])

# create dataframe of scraped data for today and future dates
column_names = ['date_valid', 'alpine_status', 'alpine_status_code', 'treeline_status', 'treeline_status_code',
            'belowtree_status', 'belowtree_status_code']
conditions_today = pd.DataFrame(conditions_today, columns=column_names)
conditions_today['problems'] = pd.DataFrame(problems)
conditions_today_plus1 = pd.DataFrame(conditions_today_plus1, columns=column_names)
conditions_today_plus2 = pd.DataFrame(conditions_today_plus2, columns=column_names)

# export scraped data to csv files
conditions_today.to_csv('../data/raw/current_avalanche_conditions_' + inputs['region'].replace('-', '_') + '_RAW.csv', index=False)
conditions_today_plus1.to_csv('../data/raw/current_plus1_avalanche_conditions_' + inputs['region'].replace('-', '_') + '_RAW.csv', index=False)
conditions_today_plus2.to_csv('../data/raw/current_plus2_avalanche_conditions_' + inputs['region'].replace('-', '_') + '_RAW.csv', index=False)
