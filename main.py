import toga

class DocumentApp(toga.App):
    
    def __init__(self, title, id):
        toga.App.__init__(self, title, id)
        
        self.title = title
        self.size = ((400, 500))

    def startup(self):
        self.main_window = toga.MainWindow('main', title=self.title, size=self.size)
        
        self.main_window.content = toga.Box()
        self.main_window.show()


    def create_elements(self):
        pass
    

if __name__ == '__main__':
    document = DocumentApp('CódigoFacilito', 'com.codigofacilito')
    document.main_loop()