class Element:
    def __init__(self,driver,element_id,By_object):
        self.driver = driver
        self.element_id = element_id
        self.By_object = By_object
        print(element_id,By_object)


    def find_element(self):
        return self.driver.find_element(self.By_object,self.element_id)