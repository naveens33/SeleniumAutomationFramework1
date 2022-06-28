from selenium.webdriver.common.by import By

from util.element import Element


def elements(selector_cls):
    test_ids = selector_cls.Test_Ids
    def deco(pom_cls):
        for test_id in test_ids.keys():
            def get_attr(self,test_id=test_ids[test_id]):
                if not isinstance(test_id,tuple):
                    return Element(self.driver,test_id,By.CSS_SELECTOR)
                else:
                    pass
            prop = property(get_attr)
            setattr(pom_cls,test_id,prop)
        pom_cls.CONFIG = selector_cls.CONFIG()
        return pom_cls
    return deco
