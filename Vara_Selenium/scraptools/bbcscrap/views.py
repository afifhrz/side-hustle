from django.shortcuts import render, HttpResponse
from selenium.webdriver.common.by import By
from selenium import webdriver
import selenium
import json
import time
import traceback

from bbcscrap.models import master_link, detail_link

# Create your views here.
def scrap_links(request):
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome = webdriver.Chrome(chrome_options=chrome_options)
        chrome.set_page_load_timeout(30)
        chrome.get("https://www.bbc.com/")
        time.sleep(5)
        
        scrap_option = ["a.media__link", "a.reel__link", "a.top-list-item__link"]
        result_link = []
        for opt in scrap_option:
            els = chrome.find_elements(By.CSS_SELECTOR, opt)
            for el in els:
                result_link.append(el.get_property("href"))
        for data in result_link:
            master_link.objects.create(
                    URI_link = data
                )
        chrome.quit()
        return HttpResponse(json.dumps({
            "status":True
        }))
    except selenium.common.exceptions.StaleElementReferenceException:
        chrome.get("https://www.bbc.com/")
        time.sleep(5)
        result_link = []
        
        for opt in scrap_option:
            els = chrome.find_elements(By.CSS_SELECTOR, opt)
            for el in els:
                result_link.append(el.get_property("href"))
        for data in result_link:
            master_link.objects.create(
                    URI_link = data
                )    
        chrome.quit()
        return HttpResponse(json.dumps({
            "status":True
        }))
        
    
    except Exception as e:
        return HttpResponse(json.dumps({
            "status":False,
            "message": traceback.format_exc()
        }))

def scrap_each(request):
    try:
        data = master_link.objects.all()
        
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome = webdriver.Chrome(chrome_options=chrome_options)
        chrome.set_page_load_timeout(30)
        
        scrap_option = {
            'news':['h1', 'div.ssrcss-11r1m41-RichTextComponentWrapper','div.ssrcss-7uxr49-RichTextContainer','div.ssrcss-1s1kjo7-RichTextContainer'],
            'worklife':['h1', 'div.article__body-content'],
            'travel':['h1','div.article__body-content'],
            'future':['h1', 'div.article__body-content'],
            'culture':['h1', 'div.article__body-content'],
            'sport':['h1', 'div.qa-story-body'],
            'reel':['h1', 'div.x11b5-summary'],
            'sport-live':['h1','section.qa-summary-points'],
            'news-live':['h1','section.qa-summary-points'],
        }
        
        for page in data:
            chrome.get(page.URI_link)
            time.sleep(5)
        
            result_title = ''
            result_desc = ''
            splitlink = page.URI_link.split('/')
            
            if splitlink[4] == 'live':
                key = splitlink[3]+'-live'
            else:
                key = splitlink[3]
            for opt in scrap_option[key]:
                if opt == 'h1':
                    els = chrome.find_element(By.CSS_SELECTOR, opt)
                    result_title += els.text    
                else:
                    els = chrome.find_elements(By.CSS_SELECTOR, opt)
                    for el in els:
                        if el.text == '':
                            result_desc+=el.get_attribute("innerText")
                        else:
                            result_desc+=el.text
            
            detail_link.objects.create(
                title = result_title,
                description = result_desc,
                link_id = page
            )
        chrome.quit()
        return HttpResponse(json.dumps({
            "status":True
        }))
    except Exception as e:
        return HttpResponse(json.dumps({
            "status":False,
            "message": traceback.format_exc()
        }))