import requests
from bs4 import BeautifulSoup
import kivy
from kivy.app import App
from kivy.uix.label import Label

def parsing():
    url = 'http://bseu.by/schedule/'
    response = requests.get(url)
    
    if response.status_code == 200:
        page_content = response.text
        soup = BeautifulSoup(page_content, 'html.parser')
        div_content = soup.find_all('tbody')
        for content_div in div_content:
            print(content_div.text)
    else:
        print('ERROR')

parsing()

# class MyApp(App):

    

#      def build(self):
#          return Label(text='Hello world')


# if __name__ == '__main__':
#     MyApp().run()