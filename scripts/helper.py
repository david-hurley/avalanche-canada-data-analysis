# ----------------------------------------------------
# scrapes historical Avalanche Canada conditions and forecast conditions and problem text
#
# author David Hurley
# email hurleyldave@gmail.com
# ----------------------------------------------------

import pandas as pd
import time
from selenium import webdriver

def scrape(dates, region):
    """ Scrape current and forecast conditions and problem text from AvalancheCanada.ca historical page """

    # empty list for current, current+1, current+2 forecast conditions and text problems
    current_conditions = []
    current_plus_1_conditions = []
    current_plus_2_conditions = []
    problem_conditions = []

    # initialize selenium web driver
    base_url = 'https://www.avalanche.ca/forecasts/archives/{}/{}'
    driver = webdriver.Firefox()
    driver.get(base_url.format(region, dates[0]))
    time.sleep(3)  # slight pause for driver to load

    # scrape avalanche canada data for each date
    for date in dates:

        date_plus_1 = (pd.to_datetime(date) + pd.Timedelta('1 days')).strftime('%Y-%m-%d')  # tomorrows date
        date_plus_2 = (pd.to_datetime(date) + pd.Timedelta('2 days')).strftime('%Y-%m-%d')  # day after tomorrows date

        # locate relevant avalanche data in web driver, this is hard coded to the page JavaScript
        alpine_element = driver.find_elements_by_xpath(
            "//*[@id='app']//*[@transform = 'translate(385 211)']//*[@x = '70']")
        treeline_element = driver.find_elements_by_xpath(
            "//*[@id='app']//*[@transform = 'translate(405 261)']//*[@x = '70']")

        belowtree_element = driver.find_elements_by_xpath(
            "//*[@id='app']//*[@transform = 'translate(425 311)']//*[@x = '70']")

        forecast_element = driver.find_elements_by_xpath(
            "//*[@id='app']//*[@class='_2tSd']//*[@class='Xgfa undefined _2j-o _2iRE']")

        problem_element = driver.find_elements_by_xpath("//*[@id='app']//*[@class='_1rb7']")

        # if no conditions exist then insert empty to list
        if not alpine_element or not treeline_element or not belowtree_element or not forecast_element:
            current_conditions.append([date])
            current_plus_1_conditions.append([date_plus_1])
            current_plus_2_conditions.append([date_plus_2])
            problem_conditions.append([])
        else:
            # if conditions exist then parse data
            alpine_conditions = [condition.text for condition in alpine_element]
            treeline_conditions = [condition.text for condition in treeline_element]
            belowtree_conditions = [condition.text for condition in belowtree_element]
            future_conditions = [condition.text for condition in forecast_element]
            problems = [prob.text for prob in problem_element]

            # store data for current and forecast conditions and problem text, split based on output format from page
            current_conditions.append([date, alpine_conditions[0].split(' - ')[-1], int(alpine_conditions[0].split(' - ')[0]),
                                       treeline_conditions[0].split(' - ')[-1], int(treeline_conditions[0].split(' - ')[0]),
                                       belowtree_conditions[0].split(' - ')[-1], int(belowtree_conditions[0].split(' - ')[0])])

            current_plus_1_conditions.append(
                [date_plus_1, future_conditions[0].split(' - ')[-1], int(future_conditions[0].split(' - ')[0]),
                 future_conditions[1].split(' - ')[-1], int(future_conditions[1].split(' - ')[0]),
                 future_conditions[2].split(' - ')[-1], int(future_conditions[2].split(' - ')[0])])

            current_plus_2_conditions.append(
                [date_plus_2, future_conditions[3].split(' - ')[-1], int(future_conditions[3].split(' - ')[0]),
                 future_conditions[4].split(' - ')[-1], int(future_conditions[4].split(' - ')[0]),
                 future_conditions[5].split(' - ')[-1], int(future_conditions[5].split(' - ')[0])])

            problem_conditions.append(problems)

        # slight pause for driver to load
        driver.get(base_url.format(region, date_plus_1))
        time.sleep(5)

    driver.quit()  # close selenium driver

    return current_conditions, current_plus_1_conditions, current_plus_2_conditions, problem_conditions
