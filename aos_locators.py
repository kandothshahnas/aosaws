import datetime
from faker import Faker

fake = Faker(locale='en_CA')
aos_url = 'https://advantageonlineshopping.com/#/'
aos_username = f'{fake.user_name()}{fake.pyint(111, 999)}'[:15]
aos_password = fake.password()[:12]
aos_email = fake.email()
first_name = fake.first_name()
last_name = fake.last_name()
phone = fake.phone_number()
city = fake.city()
province = fake.province()[:10]
address = fake.street_address()
postal_code = fake.postcode()
full_name = f'{first_name} {last_name}'
cart_url = 'https://advantageonlineshopping.com/#/shoppingCart'
fb_url = 'https://www.facebook.com/MicroFocus/'
twitter_url = 'https://twitter.com/MicroFocus'
linkedin_url = 'https://www.linkedin.com/company/micro-focus/'
contact_text = f'User added by {aos_username} via Python Selenium Automated script on {datetime.datetime.now()}'
order_no = 0
tracking_no = 0
order_date = ' '
my_account_url = 'https://advantageonlineshopping.com/#/myAccount'
