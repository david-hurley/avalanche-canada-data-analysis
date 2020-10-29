# Avalanche Canada data analysis toolkit

The Avalanche Canada data analysis toolkit is a collection of Python files for retrieving, processing, and visualizing [historically forecasted Avalanche Canada](https://www.avalanche.ca/forecasts/archives) danger ratings for select forecast regions and dates. Specifically, this toolkit provides a method to scrape danger rating data and examines danger rating statistics and anamolies between current day and 1- and 2-day out forecasted dagner ratings. 

## Overview
### Key Terms
* Current Conditions - the present days danger ratings as forecasted by Avalanche Canada
* Current Plus1 Conditions - tomorrows danger ratings (i.e. one day ahead of current conditions) as forecasted by Avalanche Canada
* Current Plus2 Conditions - day after tomorrows danger ratings (i.e. two days ahead of current conditions) as forecasted by Avalanche Canada
* Forecast Anamoly - percentage of time that a 1- or 2-day out forecasted danger rating differs or agrees with current conditions. This provides insight into the forecast confidence and conservativeness of the forecast (i.e. do they forecast a higher danger rating than what is presented the day of)
* Danger Ratings - avalanche hazard on a scale from 1 (lowest) to 5 (highest)
* Forecast Region - geographic area that Avalanche Canada forecast applies
* Alpine, Treeline, Belowtree - elevation the forecast applies (i.e. alpine is above treeline, treeline is sparse trees, belowtree is forested)

### Key Repo Locations
* Data scraping (i.e. retrieval) code lives in `scripts`
* Test tools to confirm data scraping PATHS are still relevant live in `tests`
* Raw and cleaned data for select forecast regions and dates lives in `data`
* Jupyter Notebook to analyze and visualize danger rating data lives in `notebooks`
* Result figures are in save to `figures`

## Getting Started
1. Clone this repo, instructions found [HERE](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository)
2. Open a command prompt and navigate to the newly cloned repo
3. Create a virtual environment by executing `python -m venv venv` in a command prompt, instructions found [HERE](https://docs.python.org/3/library/venv.html)
4. Activate the virtual environment, in Linux this is `source venv/bin/activate`
5. Install dependencies by executing `pip install -r requirements.txt` in a command prompt 

## Scraping Avalanche Canada Data
Scraping involves launching a web browser, in this case Firefox, extracting information from a desired page path, and saving data. This code scrapes and saves historical Avalanche Canada danger ratings for day of and 1- and 2-day out conditions for any forecast region and date range. Raw data is saved to `data/raw` and cleaned data is saved to `data/cleaned`. 

#### Test Scrape
Prior to scraping data it's a good idea to test the scraping code as the Avalanche Canada page paths may have changed. Perform the following to test the scraping code:
1. Open a command prompt and navigate to the root directory of the cloned repo (likely `avalanche-canada-data-analysis`)
2. Execute `python -m unittest discover tests`
3. If the code passes the tests an `OK` will be displayed (note, this may take 10-15 seconds)

#### Scrape New Data
Perform the following to scrape new data:
1. Open `scrape_inputs.json` and set the desired forecast region and date range to scrape. Also, determine if a web browser should be displayed while scraping (suggest yes as it provides feedback). Note, the forecast region must match EXACTLY with the Avalanche Canada regions. To check a forecast region name go [HERE](https://www.avalanche.ca/forecasts/archives) and select the forecast region then confirm the forecast region name displayed in the URL address bar (i.e. this might be `sea-to-sky` or `south-coast-inland`). 
2. Open a command prompt or IDE and navigate to `scripts`
3. Execute `python scrape_export_data.py`, this may take some time. The results will be save to `data/raw`

## Clean Scraped Avalanche Canada Data


## Analyze and Visualize Avalanche Canada Data
