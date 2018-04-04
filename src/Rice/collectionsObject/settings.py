
from ..baseClasses.collection import Collection


class Settings(Collection):
    def __init__(self, parent, *args):
        self.parent = parent[parent[-1]]
        self.parentsDict = parent
        self.cat_constructor = self.parent.cat_constructor
        self.parentsDict[self.name] = self
        self.setting_dict = dict()

    @property
    def name(self):
        return self.cat_constructor.Name

    @name.setter
    def name(self, value):
        self.cat_constructor.Name = value

    def change(self, path, name, *args):
        ## Example path: Infrastructure.PartInfrastructure.PartDocument
        path = path.split('.')
        cls = __import__('collectionsObject.settingF.{}.{}'.format(path[0], path[1]), [path])
        func = cls.__dict__['settingF'].__dict__[path[0]].__dict__[path[1]].__dict__[path[2]]
        func(self.parent, name, args)
        self.setting_dict[name] = [path, args]

    def __getitem__(self, item):
        return self.setting_dict[item]

    def __setitem__(self, key, value):
        self.setting_dict[key][1] = value
        self.change(self.setting_dict[key][0],key,value)
