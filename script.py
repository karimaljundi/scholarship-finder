from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def get_uoft_scholarships():
    service = Service(executable_path="chromedriver.exe")
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
                    first_cell_text = cells[0].text
                    scholarships.append(first_cell_text)
                    print(first_cell_text)
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
get_uoft_scholarships()