from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

def get_url(search_text):
    """Generate a url from search text"""

    url = f"https://www.amazon.com/s?k={search_text}&ref=nb_sb_noss_1"

    # add page query for pagination

    url += "&page{}"

    return url

def extract_record(single_item):
    """Extract and return data from a single item in the search"""

    try:
        price_parent = single_item.find("span", "a-price")

        price = price_parent.find("span", "a-offscreen").text
    except AttributeError:

        return

    return price

def main(search_term, max_price):
    """This function will accept the search term and the maximum price you are expecting the product to be"""

# startup the webdriver

    options=Options()
    
    options.headless = True #choose if we want the web browser to be open when doing the crawling 
    driver = webdriver.Chrome('/home/muhammed/Desktop/dev/blog-repo/twilioXseleniumXpython/chromedriver',options=options)
    prices_list=[] # this will hold the list of prices

    url = get_url(search_term) # takes the search term to get_url() function above.

    for page in range(1, 5):
        """For loop to get each item in the first 5 pages of the search"""

        driver.get(url.format(page))
        soup = BeautifulSoup(driver.page_source, "html.parser") #retrieve and parse HTML text.
        results = soup.find_all("div", {"data-component-type": "s-search-result"}) #get all the attributes of each item

        for item in results:
            record = extract_record(item) #takes each item to extract_record() function above to get the prices
            if item:
                prices_list.append(item)

main("iphone", "1000") # call the main function with the search term and the maximum price you are expecting the product to be
# above values are examples.