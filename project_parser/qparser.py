from ast import Break
from time import time
import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


url = 'https://zakupki.gov.ru/epz/contract/search/results.html?searchString=%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82&morphology=on&search-filter=%D0%94%D0%B0%D1%82%D0%B5+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F&fz44=on&fz94=on&contractStageList_0=on&contractStageList=0&contractPriceFrom=10000000&contractCurrencyID=-1&budgetLevelsIdNameHidden=%7B%7D&sortBy=UPDATE_DATE&pageNumber=1&sortDirection=false&recordsPerPage=_10&showLotsInfoHidden=false'
file_path_page = 'project_parser/pars_data/source-page.html'
file_path_urls = 'project_parser/pars_data/item_urls.txt'
add_to_path = 'https://zakupki.gov.ru'


# Словар с заголовками запросов
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}


def get_source_html(url):
    driver = webdriver.Chrome('/Volumes/HDD/Dropbox/Data Science/VS CODE/sf_data_science/project_parser/chromedriver')
    print('driver:', driver)
    driver.maximize_window

    try:
        driver.get(url=url)
        time.sleep(3)
        
        while True:
            find_more_element = driver.find_element_by_class_name('paginator-button paginator-button-next')
            print('find_more_element:', find_more_element)
            if driver.find_element_by_class_name('paginator-button'):
                with open('file_path_page', 'w') as file:
                    file.write(driver.page_source)
                break
            else:
                # данный кусок необходим если надо скролить страницу для загрузки
                actions = ActionChains(driver)
                actions.move_to_element('paginator-button')# Здесь надо указывать элемент через который скорится с методом .perform()
                time.sleep(3)            
                
                
    except Exception as ex:
        print(ex)
        
    finally:
        driver.close()
        driver.quit()


def get_items_urls(file_path):
    with open(file_path) as file:
        src = file.read()
    soup = BeautifulSoup(src, 'lxml')
    items_divs = soup.find_all('div', class_='row no-gutters registry-entry__form mr-0')

    urls = []
    for item in items_divs:
        item_url = item.find('div', class_='col-8 pr-0 mr-21px').find('a').get('href')
        print('Found URL:', item_url)
        urls.append(item_url)
        

    with open('file_path_urls', 'w') as file:
        for url in urls:
            file.write(f'{url}\n')
    
    return '[INFO] Urls collected saccessfully!'


def get_data(file_path):
    with open(file_path) as file:
        urls_list = [url.strip() for url in file.readlines()] # Формируя список ссылок отрезаем \n 
        print('urls_list', urls_list)
    
    # Работаем со списком ссылок из файла    
    for url in urls_list:
        response = requests.get(url=add_to_path+url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')

        # на случай если что-то пойдет не так делаем чере try-except
        try:
            item_name = soup.find('span', {'itemprop': 'name'}).text.strip()
            
        except Exception as ex:
            item_name = None
        
        item_participants_list =[]
        try:
            participants_info = soup.find('div', class_='participantsInnerHtml').find_all('td', class_='tableBlock__col')
            
            for item in participants_info:
                item_participant = item.get('href')
                item_participants_list.append(item_participant)
        except Exception as ex:
            participants_info = None
            
        print(item_name, item_participants_list)
            
                    
def main():
    #get_source_html(url)
    #print(get_items_urls(file_path=file_path_page))
    get_data(file_path=file_path_urls)
    
    
if __name__ == '__main__':
    main()    
    
"""def main():
    
    driver.get('https://zakupki.gov.ru/epz/contract/search/results.html?searchString=%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82&morphology=on&search-filter=%D0%94%D0%B0%D1%82%D0%B5+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F&fz44=on&fz94=on&contractStageList_0=on&contractStageList=0&contractPriceFrom=10000000&contractCurrencyID=-1&budgetLevelsIdNameHidden=%7B%7D&sortBy=UPDATE_DATE&pageNumber=1&sortDirection=false&recordsPerPage=_10&showLotsInfoHidden=false')
    driver.find_element_by_class_name
    """
