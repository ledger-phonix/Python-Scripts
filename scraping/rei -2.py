import httpx
from selectolax.parser import HTMLParser
import time

# This is the better way of joining url
from urllib.parse import urljoin
# This use for handling data
from dataclasses import dataclass, asdict, fields

import json
import csv


@dataclass
class item:
   Brand: str | None
   Name: str  | None
   Price: str  | None
   Item_num: str | None
   Rating: float | None





# This will handle only html code a page.
def get_html(url, **kwargs):
      
 
   headers={ "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36", "referer":"https://www.rei.com/s/womens-hiking-clothing"
   } 
   if kwargs.get('page'):
      resp = httpx.get(url + str(kwargs.get('page')), headers=headers, follow_redirects=True)
   else:
      resp = httpx.get(url, headers=headers, follow_redirects=True)


   html = HTMLParser(resp.text)
   
   try:
      resp.raise_for_status()
   except httpx.HTTPStatusError as exc:
      print(f"Error response {exc.response.status_code} while requesting {exc.request.url!r}. Page limit exeeded.")
      return False

   # print(html.css_first('title').text())
   return html

def extract_text(html,sel):
   try:
      text = html.css_first(sel).text()
      return data_clean(text)
   except AttributeError:
      return None

def parse_page(html):
   products = html.css('li.VcGDfKKy_dvNbxUqm29K')
   for product in products:
      yield urljoin('https://www.rei.com/' , product.css_first('a').attributes['href'])

def data_clean(value):
   chars_to_remove = ['$', '#', 'Item']
   for char in chars_to_remove:
      if char in value:
         value = value.replace(char,'')
   return value.strip()


def export_to_csv(products):
   field_name = [field.name for field in fields(item)]
   with open('products2.csv', 'w') as f:
      writer = csv.DictWriter(f,field_name)
      writer.writeheader()
      writer.writerows(products)


def export_to_json(products):
   with open('products.json' , 'w', encoding='utf-8') as f:
      json.dump(products, f , ensure_ascii= False, indent= 4)
  
def parse_item_page(html):
   new_Item = item(
      Brand= extract_text(html,"a#product-brand-link"),
      Name= extract_text(html,"h1#product-page-title"),
      Rating= extract_text(html, "span.cdr-rating__number_13-5-3"),
      Item_num= extract_text(html, "span#product-item-number"),
      Price= extract_text(html, "span#buy-box-product-price")
   )      
   return asdict(new_Item)

def main():
   products = []
   baseurl = 'https://www.rei.com/s/womens-hiking-clothing?page='
   for x in range(1,60):
      print(f'Getting data from page {x}')      
      html = get_html(baseurl, page = x)

      if html is False:
         break
      
      product_urls = parse_page(html)
      for url in product_urls:
         print(url)
         html =  get_html(url) 
         products.append(parse_item_page(html))        

         time.sleep(0.5)   
   # export_to_json(products)
   export_to_csv(products)

if __name__ == "__main__" :
   main()
   