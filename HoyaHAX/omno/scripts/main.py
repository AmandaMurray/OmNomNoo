import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path = "C:/Users/amm2x/OneDrive/Desktop/chromedriver_win32/chromedriver.exe")
driver.get("https://www.hoyaeats.com/menu-hours/")
elem = driver.find_elements_by_class_name("open-now-location-link")
link_list = []
for a in elem:
    link = (a.get_property("href"))
    if "https://www.hoyaeats.com/" in link:
        #print(a.text)
        link_list.append(link)
scores_dict = {}
for link in link_list:
    driver.get(link)
    restaurant = driver.find_element_by_tag_name('h1').text
    score = 0
    num = 0;
    elem = driver.find_elements_by_class_name("menu-item-li")
    name_list = []
    ingredients = []
    html = driver.page_source
    for a in elem:
        if len(a.text) > 0:
            num+=1
            ingredientsList = a.get_attribute("data-searchable")
            ingredientsList = ingredientsList.lower()
            name_list.append(a.text)
            ingredients.append(ingredientsList)
            if "beef" in ingredientsList:
                score+=0.1414
            if "lamb" in ingredientsList:
                score+=0.2343
            if "butter" in ingredientsList:
                score+=0.0717
            if "cheese" in ingredientsList:
                score+=0.807
            if "palm oil" in ingredientsList:
                score+=0.0586
            if "asparagus" in ingredientsList:
                score+=0.0532
            if "pork" in ingredientsList:
                score+=0.0723
            if "sugar" in ingredientsList:
                score+=0.0251
            if "salmon" in ingredientsList:
                score+=0.0711
            if "turkey" in ingredientsList:
                score+=0.0652
            if "chicken" in ingredientsList:
                score+=0.0412
            if "tuna" in ingredientsList:
                score+=0.0365
            if "eggs" in ingredientsList:
                score+=0.0287
    if num != 0:
        scores_dict[restaurant] = score/num
print(scores_dict)



'''
    elem = driver.find_elements_by_class_name("menu-item-li")
    if len(elem) > 0:
        for a in elem:
            if len(a.text) >0:
                a.click()
                webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
                ingredients  = ingredients.lower()
                if "beef" in ingredients:

                if "sugar" in ingredients:
                    print("suuuggggggaarrr")

driver.close()
'''
