import datetime

from faker import Faker
fake = Faker(locale='en_CA')




#______________________________WeGoStudy app DATA PARAMETERS____________________________

app = 'WeGoStudy'
wego_study_url = 'https://wegostudy.ca/'
wego_study_homepage_title = 'WeGoStudy'

user_email = 'pewec@protonmail.com'
password = '789WeStudy!'
first_name = fake.first_name()
last_name = fake.last_name()
email = fake.email()
