
from collections import deque


class Collection(object):
    """

        Base Class of Collections object types.
        Manage the creations and handle its behaviour.

        Objects variables:
            - parent                 Object of upper class, the type of collection rules the type of parent
            - parentsDict            OrderDict object, contains the parents of collections
            - collectionType         Catia's collection name
            - deque                  Deque object, list of object instantiated by collection
            - cat_constructor        Catia's working variables, python COMObject
            - cls                    Declaration of class, ruled by the type of the collection
            - name                   Property, name of the collection
    """

    def __init__(self, parent, collectionType):
        """

        Import the collection type referenced by import_path and saves its class declaration.

        :param parent: orderDict object, Contains the parents of the object. See also OrderDict doc.
        :param collectionType: Catia's collection name
        :return:
        """
        self.parent = parent[parent[-1]]
        self.parentsDict = parent
        self.collectionType = collectionType
        self.deque = deque()
        self.cat_constructor = eval('self.parent.cat_constructor.{}'.format(self.collectionType))

        self.parentsDict[self.name] = self

    @property
    def name(self):
        return self.cat_constructor.Name

    @name.setter
    def name(self, value):
        self.cat_constructor.Name = value

    @property
    def application(self):
        return self.cat_constructor.Application

    @property
    def Count(self):
        return self.cat_constructor.Count

    @property
    def Parent(self):
        return self.cat_constructor.Parent

    def GetItem(self, name):
        return self.cat_constructor.GetItem(name)

    def item(self,index_name):
        obj = self.cat_constructor.Item(index_name)
        return obj

    def new_from(self, file_path):
        #TODO
        pass

    def open(self, file_path):
        #TODO
        pass

    def read(self, file_path):
        #TODO
        pass

    def add(self, obj):
        self.deque.append(obj)
