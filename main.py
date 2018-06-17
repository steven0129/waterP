from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def crawl(**kwargs):
    for k_, v_ in kwargs.items():
        setattr(options, k_, v_)
    options = Options()
    options.add_argument('--headless')

    driver = webdriver.Firefox(firefox_options=options, executable_path='./crawl/geckodriver')
    driver.get('http://fhy.wra.gov.tw/ReservoirPage_2011/StorageCapacity.aspx')
    print(driver.title)

if __name__ == '__main__':
    import fire
    fire.Fire()