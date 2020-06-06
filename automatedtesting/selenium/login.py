# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

class SwagLab:
# Start the browser and login with standard_user

    driver = webdriver.Chrome()
    
    def login (self, user, password):
        print ('Starting the browser...')
        # --uncomment when running in Azure DevOps.
        # options = ChromeOptions()
        # options.add_argument("--headless") 
        # driver = webdriver.Chrome(options=options)
        driver = self.driver
        print ('Browser started successfully')
        print ('Navigating to the demo page to login.')
        driver.get('https://www.saucedemo.com/')
        print ('User {'+user+'} trying to login now')
        driver.find_element_by_css_selector("input[id='user-name']").send_keys(user)
        driver.find_element_by_css_selector("input[id='password']").send_keys(password)
        driver.find_element_by_css_selector("input[class='btn_action']").click()
        products = driver.find_element_by_css_selector("div[class='product_label']").text
        print('We are on page '+ products)

        if(products == 'Products'):
            print('User {'+ user +'} able to login successfully')
        else:
            print('Error something went Wrong while login')
    #login('standard_user', 'secret_sauce')

    def click_on_products(self, products, action):
        for product in products:
            name = product.find_element_by_css_selector('div[class="inventory_item_name"]').text
            print(action +' Product to Cart :'+name)
            product.find_element_by_css_selector("div[class='pricebar'] > button").click()

    #Add all products into cart and then remove its
    def add_to_cart(self):
        self.login('standard_user', 'secret_sauce')
        driver = self.driver
        products = driver.find_elements_by_css_selector("div[class='inventory_item']")
        self.click_on_products(products,'Adding')
        noOfProductsAdded = driver.find_element_by_css_selector('span[class="fa-layers-counter shopping_cart_badge"]').text
        print("Total no of products added " + noOfProductsAdded )
        assert "6" in [noOfProductsAdded]
        self.click_on_products(products, 'Removing')
        noOfProductsAdded = len(driver.find_elements_by_css_selector('span[class="fa-layers-counter shopping_cart_badge"]'))
        print("Total no of products Removed " + str(noOfProductsAdded))
        assert "0" in [str(noOfProductsAdded)]    
x = SwagLab()
x.add_to_cart()
