import logging
import sys
from datetime import datetime
from multiprocessing import Pool
from selenium.webdriver.common.by import By
from Config import config
from Driver.InitDriver import initDriver
from Enum.ExtractItemEnum import ExtractedJobEnum, JobSource

current_time = datetime.now().strftime("%Y_%m_%d")
logging.basicConfig(filename=f'./log/JobExtractor_{current_time}.log',
                    filemode='a',
                    format='[%(asctime)s] - %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)


def extractJobInJobsDB(search_word):
    str(search_word).replace(" ", "-")
    try:
        driver = initDriver(headless=True)
    except Exception as e:
        logging.error("[JobsDB Extractor] Init driver error!")
        logging.error(f'[JobsDB Extractor] Error Msg: {e}')

    job_found = []
    for i in range(1, 4):
        target_url = config.jobsDB_website.replace("name", search_word).replace("page", str(i))

        try:
            driver.get(target_url)

            # Time for loading
            driver.implicitly_wait(5)

            logging.info(f'[JobsDB Extractor] - Getting the job details and company names')
            jobs_detail_list = driver.find_elements(By.CSS_SELECTOR, config.jobsDB_jobs_details)
            company_names_list = driver.find_elements(By.CSS_SELECTOR, config.jobsDB_company_names)
            logging.info(f'[JobsDB Extractor] - Required information got')

            for itr in range(len(company_names_list)):
                extract_company_name = company_names_list[itr].text
                extract_role_name = jobs_detail_list[itr].text
                extract_jobs_url = jobs_detail_list[itr].find_element(By.TAG_NAME, "a").get_attribute("href")

                extract_job = {ExtractedJobEnum.company.value: extract_company_name,
                               ExtractedJobEnum.role.value: extract_role_name,
                               ExtractedJobEnum.source.value: JobSource.jobsDB.value,
                               ExtractedJobEnum.url.value: extract_jobs_url}

                job_found.append(extract_job)
            logging.info(f'[JobsDB Extractor] - Finished extraction')
        except Exception as e:
            logging.error("[JobsDB Extractor] Exception Caught!")
            logging.error(f'[JobsDB Extractor] Error msg: {e}')

    return job_found


def extractJobInGlassdoor(search_word):
    try:
        driver = initDriver(headless=False)
    except Exception as e:
        logging.error("[Glassdoor Extractor] Init driver error!")
        logging.error(f'[Glassdoor Extractor] Error Msg: {e}')

    job_found = []

    try:
        driver.get(config.glassdoor_website)

        # Search by keyword
        search_box = driver.find_element(By.CSS_SELECTOR, config.glassdoor_search_box)
        search_box.send_keys(str(search_word))
        driver.find_element(By.CSS_SELECTOR, config.glassdoor_search_button).click()

        # Time for loading page
        driver.implicitly_wait(5)

        # Navigate to "all job" page
        driver.find_element(By.CSS_SELECTOR, config.glassdoor_view_all_job_button).click()
        driver.implicitly_wait(5)

        logging.info(f'[Glassdoor Extractor] - Getting the job details and company names')
        company_names_list = driver.find_elements(By.CSS_SELECTOR, config.glassdoor_company_names)
        job_roles_list = driver.find_elements(By.CSS_SELECTOR, config.glassdoor_company_roles)
        driver.implicitly_wait(5)
        logging.info(f'[Glassdoor Extractor] - Required information got')

        for itr in range(len(company_names_list)):
            extract_company_name = company_names_list[itr].text
            extract_role_name = job_roles_list[itr].text
            extract_url = job_roles_list[itr].get_attribute("href")

            extract_job = {ExtractedJobEnum.company.value: extract_company_name,
                           ExtractedJobEnum.role.value: extract_role_name,
                           ExtractedJobEnum.source.value: JobSource.glassdoor.value,
                           ExtractedJobEnum.url.value: extract_url,
                           }

            job_found.append(extract_job)
        driver.implicitly_wait(15)
        logging.info(f'[Glassdoor Extractor] - Finished extraction')
    except Exception as e:
        logging.error("[Glassdoor Extractor] Exception caught!")
        logging.error(f"[Glassdoor Extractor] Error msg: {e}")

    return job_found


def MultiProcessorExtractor(search_word):
    with Pool(processes=2) as pool:
        p1 = pool.apply_async(extractJobInJobsDB, args=(str(search_word),))
        p2 = pool.apply_async(extractJobInGlassdoor, args=(str(search_word),))
        return p1.get() + p2.get()


if __name__ == '__main__':
    search_word = sys.argv[1]
    print("Test")
    MultiProcessorExtractor(search_word)
