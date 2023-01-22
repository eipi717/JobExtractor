import configparser

# init config
config = configparser.ConfigParser()
config.read('/Users/nicholas717/Downloads/Non-work/JobExtractor/Config/config.ini')

########################### Driver ###########################
# Driver's path
selenium_driver_path = config['Driver']['seleniumDriver_fullPath']

######################### JobsDB #########################
# JobsDB website
jobsDB_website = config['Website']['jobsDB_website']

# Elements used in crawling
jobsDB_search_box = config['jobsDB_Element']['search_box']
jobsDB_search_button = config['jobsDB_Element']['search_button']
jobsDB_jobs_details = config['jobsDB_Element']['job_details']
jobsDB_company_names = config['jobsDB_Element']['company_names']

######################## Glassdoor ########################
# Glassdoor
# Glassdoor website
glassdoor_website = config['Website']['glassdoor_website']

# Elements used in crawling
glassdoor_search_box = config['glassdoor_Element']['search_box']
glassdoor_search_button = config['glassdoor_Element']['search_button']
glassdoor_view_all_job_button = config['glassdoor_Element']['view_all_job_button']
glassdoor_company_names = config['glassdoor_Element']['company_names']
glassdoor_company_roles = config['glassdoor_Element']['roles']
