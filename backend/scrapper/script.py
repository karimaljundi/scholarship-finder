import os
import sys


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
import time
import re

parent_dir=os.path.abspath('..')
sys.path.append(parent_dir)
from models import db, Scholarship
from app import create_app
app = create_app()
app.app_context().push()

def save_scholarship(scholarship):
    new_scholarship = Scholarship(
        name=scholarship["name"],
        description=scholarship["description"],
        offered_by=scholarship["offered_by"],
        type=scholarship["type"],
        citizenship_type=scholarship["citizenship_type"],
        application_required=scholarship["application_required"],
        nature_of_award=scholarship["nature_of_award"],
        application_deadline=scholarship["application_deadline"],
        value=scholarship["value"],
        university=scholarship["university"]
    )
    db.session.add(new_scholarship)
    db.session.commit()

def filter_value(text):
        # Try matching a single value
    single_value = re.search(r'\b(?:approx|around|about|up to|)\s*\$?(\d+)\b', text)
    if single_value:
        return int(single_value.group(1))

    # Try matching a range
    range_value = re.search(r'\$?(\d+)\s*(?:-|to)\s*\$?(\d+)', text)
    if range_value:
        low, high = map(int, range_value.groups())
        return (low + high) // 2  # or low, or high

    # Return None if no pattern matched
    return None
def scrape_uoft_scholarships():
    service=Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    driver.get("https://uoftscholarships.smartsimple.com/ex/ex_viewreport.jsp?key=&token=%40HwoGSxocZERdRRtfQRxZQ11SZV1zH3pgEw~~")
    scholarships = []

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'report_frame')))
    iframe = driver.find_element(By.ID, "report_frame")
    driver.switch_to.frame(iframe)
    # print(driver.page_source)
    while True:
        outerDiv = driver.find_element(By.ID, "containerDiv")
        table = outerDiv.find_element(By.TAG_NAME, "table")
    # print(table.get_attribute("innerHTML"))
        for row in table.find_elements(By.TAG_NAME, "tr"):
            cells = row.find_elements(By.TAG_NAME, "td")
            if cells:     
                    print(filter_value(cells[8].text))         
                    scholarship = {
                        "name": cells[0].text,
                        "description": cells[1].text,
                        "offered_by": cells[2].text,
                        "type": cells[3].text,
                        "citizenship_type": cells[4].text,
                        "application_required": cells[5].text,
                        "nature_of_award": cells[6].text,
                        "application_deadline": cells[7].text,
                        "value": str(filter_value(cells[8].text)),
                        "university": "University of Toronto"
                    }
                    scholarships.append(scholarship)
                    save_scholarship(scholarship)
            else:
                    print("Row has no cells.")
        try:
            next_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-default.next.lastvisible"))
            )
            next_button.click()
        except TimeoutException:
            print("No next button found or not clickable.")
            break
    driver.switch_to.default_content()

    driver.quit()
    for scholarship in scholarships:
        print(scholarship)
    return scholarships
if __name__ == '__main__':
    scrape_uoft_scholarships()

    