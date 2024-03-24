#import necessary tools + libraries
import requests
from bs4 import BeautifulSoup
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from urllib3 import HTTPResponse
from .forms import SurveyForm  # Assuming you have a form class for validation

@require_http_methods(["POST"])
def submit_survey(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
    if form.is_valid():
        import json
        #post_data = json.loads(request.body.decode("utf-8"))
        memorySize = form.cleaned_data['memorySize']
        #print(post_data)
        processor = form.cleaned_data['processor']
        
        #print(processor)
        brand = form.cleaned_data['brand']
        screen = form.cleaned_data['screen']
        price = form.cleaned_data['price']
        touch = form.cleaned_data['touch']
        print(touch)


        # Example: Perform some logic based on selected options
        recommendation = scrape_best_buy_laptops(memorySize, processor, brand, screen, price,touch)

        response_data = {
            'success': True,
            'message': 'Thank you for your submission!',
            'recommendation': recommendation,  # Include additional data based on form input
        }
        return JsonResponse(response_data)
    else:
        return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    

#scrapes the first four pages of the best buy website 
def scrape_best_buy_laptops(memorySize, processor, brand, screen, price,touch):
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"} 
    urls = ['https://www.bestbuy.com/site/searchpage.jsp?id=pcat17071&st=laptops+computers+on+sale', 
            'https://www.bestbuy.com/site/searchpage.jsp?cp=2&id=pcat17071&st=laptops+computers+on+sale', 
            'https://www.bestbuy.com/site/searchpage.jsp?cp=3&id=pcat17071&st=laptops+computers+on+sale', 
            'https://www.bestbuy.com/site/searchpage.jsp?cp=4&id=pcat17071&st=laptops+computers+on+sale']
    
    laptops = [] #laptop_data is a dictionary with key-value pairs (key = name)
    for url in urls: #iterate through all 4 pages 
        response = requests.get(url = url, headers = headers)
        soup = BeautifulSoup(response.content, 'html.parser') # If this line causes an error, run 'pip install html5lib' or install html5lib
        # print(soup.prettify()) 
        for row in soup.findAll('h4', attrs = {'class':'sku-title'}):  # find the names of the laptops
            laptop = {}
            laptop['name'] = row.a.text
            laptops.append(laptop) #add the key-value pairs (ex. name-"lenovo thinkpad...") to the dictionary
    gb = []
    for i in laptop:
        name = i.get("name") #retrieves the value associated with the key
        if (name.__contains__(memorySize)): #checks to see if the value contains the attribute
            gb.append(name) #adds the laptop to the list 
    processor = []
    for i in gb:
        if (i.__contains__(processor)): #checks to see if the value contains the attribute
            gb.append(i) #adds the laptop to the list 
    return processor


@require_http_methods(["GET"])
def demo(request):
    return render(request, "base.html")