from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from tqdm import tqdm

def crawl(**kwargs):
    for k_, v_ in kwargs.items():
        setattr(options, k_, v_)
    options = Options()
    options.add_argument('--headless')

    driver = webdriver.Firefox(firefox_options=options, executable_path='./crawl/geckodriver')
    driver.get('http://fhy.wra.gov.tw/ReservoirPage_2011/StorageCapacity.aspx')

    f = open('./crawl/data.csv', 'w')
    f.write('Time,Reservoir,Percent\n')

    for y in tqdm(range(2009, 2019)):
        driver.find_element_by_xpath(f"//select[@id='ctl00_cphMain_ucDate_cboYear']/option[text()='{y}']").click()

        for m in tqdm(range(1, 13)):
            driver.find_element_by_xpath(f"//select[@id='ctl00_cphMain_ucDate_cboMonth']/option[text()='{m}']").click()
            select = driver.find_element_by_xpath("//select[@id='ctl00_cphMain_ucDate_cboDay']")
            
            for opt in tqdm(select.find_elements_by_tag_name('option')):
                day = opt.text
                driver.find_element_by_xpath(f"//select[@id='ctl00_cphMain_ucDate_cboDay']/option[text()='{day}']").click()
                rows = driver.find_elements_by_xpath('/html/body/form/div[3]/div[2]/div/table/tbody/tr')
                for row in range(3, len(rows)):
                    reservoir = driver.find_element_by_xpath(f'/html/body/form/div[3]/div[2]/div/table/tbody/tr[{row}]/td[1]').text
                    percent = driver.find_element_by_xpath(f'/html/body/form/div[3]/div[2]/div/table/tbody/tr[{row}]/td[11]').text.replace(' ', '')
                    f.write(f'{y}/{m}/{day},{reservoir},{percent}\n')

if __name__ == '__main__':
    import fire
    fire.Fire()