__version__ = "1.0"


import requests
from kivymd.uix.label import MDLabel
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.list import OneLineListItem
from kivymd.uix.snackbar import Snackbar



class HomePage(Screen):
    pass


class ErrorPage(Screen):
    pass


states = ['Andaman and Nicobar Islands', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh', 'Dadra and Nagar Haveli and Daman and Diu', 'Delhi', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir', 'Jharkhand', 'Karnataka',
          'Kerala', 'Ladakh', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttarakhand', 'Uttar Pradesh', 'West Bengal', 'Cases being reassigned to states']


class mainApp(MDApp):
    def build(self):
        return Builder.load_file('main.kv')

    def s(self, i):
        # print(DATA['regionData'][1]['totalCases'])
        try:
            # print(DATA)
            c = 0
            for state in states:
                if state == i.text:
                    # print(c)
                    self.root.ids['Home_Page'].ids['total'].text = str(int(DATA['regionData'][c]['totalInfected']) + int(
                        DATA['regionData'][c]['recovered']) + int(DATA['regionData'][c]['deceased']))
                    self.root.ids['Home_Page'].ids['active'].text = str(
                        DATA['regionData'][c]['totalInfected'])
                    self.root.ids['Home_Page'].ids['recover'].text = str(
                        DATA['regionData'][c]['recovered'])
                    self.root.ids['Home_Page'].ids['death'].text = str(
                        DATA['regionData'][c]['deceased'])
                    self.root.ids['Home_Page'].ids['bd'].open()
                    self.root.ids['Home_Page'].ids['stateName'].text = i.text
                    break
                c = c + 1
        except:
            Snackbar(text="No Internet Connection").show()

    def navBar(self, opt):
        # print('Prashant')
        self.root.ids['nav'].set_state(opt)

    def all(self, instance):
        try:
            self.root.ids['Home_Page'].ids['stateName'].text = "All India"
            self.root.ids['Home_Page'].ids['total'].text = str(
                DATA['totalCases'])
            self.root.ids['Home_Page'].ids['active'].text = str(
                DATA['activeCases'])
            self.root.ids['Home_Page'].ids['recover'].text = str(
                DATA['recovered'])
            self.root.ids['Home_Page'].ids['death'].text = str(DATA['deaths'])
            # print(instance)
        except:
            Snackbar(text="No Internet Connection").show()

    def on_start(self):
        global API_URL
        global DATA
        for state in states:
            self.root.ids['Home_Page'].ids['sv'].add_widget(
                OneLineListItem(
                    text=state,
                    on_press=self.s,
                    _no_ripple_effect=True,
                )
            )
        try:
            API_URL = "https://api.apify.com/v2/key-value-stores/toDWvRj1JpTXiM8FF/records/LATEST?disableRedirect=true"
            DATA = requests.get(url=API_URL).json()
            self.root.ids['Home_Page'].ids['stateName'].text = "All India"
            self.root.ids['Home_Page'].ids['total'].text = str(
                DATA['totalCases'])
            self.root.ids['Home_Page'].ids['active'].text = str(
                DATA['activeCases'])
            self.root.ids['Home_Page'].ids['recover'].text = str(
                DATA['recovered'])
            self.root.ids['Home_Page'].ids['death'].text = str(DATA['deaths'])
            # print(state)
        except Exception as e:
            self.root.ids['sm'].current = 'Error_Page'
            print(e)
            Snackbar(text="No Internet Connection").show()

    def insta(self):
        # webbrowser.open("www.google.com")
        pass


if __name__ == "__main__":
    mainApp().run()
