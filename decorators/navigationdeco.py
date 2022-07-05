
def navigationdecoapi():
    class deco:
        def __init__(self,cls):
            self.pom_cls = cls

        def __call__(self, *cls_args):
            obj = self.pom_cls(*cls_args)
            self.driver = obj.driver
            return obj
    return deco

