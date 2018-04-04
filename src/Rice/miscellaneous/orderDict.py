__author__ = 'roberto'
import inspect
import re


class OrderDict(object):
    """
        Handle the parents of the object.
        The objects and its values are contained into dic[key] = value and the order of adding is contained into
        order_list.
        Example:
            obj = OrderDict()
            obj['key1']=1   # dic = {'key1':1} ; order_list=['key1']
            obj['key2']=2   # dic = {'key1':1,'key2':2} ; order_list=['key1','key2']
            obj['key3']=3   # dic = {'key1':1,'key2':2,'key3':3} ; order_list=['key1','key2','key3']

    """
    def __init__(self):
        self.dic = {}
        self.order_list = []

    def __setitem__(self, key, value):
        """
        Add key:value to the dict and append the key to order_list to register its order
        Example:
            obj['key4']=4 # dic = {'key1':1,'key2':2,'key3':3,'key4':4} ; order_list=['key1','key2','key3','key4']
        :param key: string
        :param value: any object
        :return:
        """
        self.dic[key] = value
        self.order_list.append(key)

    def __getitem__(self, item):
        """
        If item is a string return dic[item]
        If item is a integer return order_list[item]
        Example:

        :param item: str or int
        :return:
        """
        if type(item)==str:
            try:obj = self.dic[item]
            except:
                for i in self.dic.keys():
                    result = re.findall('{}[0-9]+'.format(item),i)
                    if len(result)>0:
                        obj = self.dic[result[0]]
                        break
        elif type(item)==int:
            obj = self.order_list[item]

        return obj

    def order(self, item):
        """
        Return the place in the order of item
        Example:

        :param item: string
        :return:integer
        """
        index = self.order_list.index(item)+1
        return index

    def _copy(self):
        """
        Copy dir and order_list and create a new instance of OrderDict with that dir and order_list
        Example:

        :return:OrderDict object
        """
        obj = OrderDict()
        obj.dic = self.dic.copy()
        obj.order_list = self.order_list.copy()

        return obj

    def _treeParent(self):
        """
        Represents in a visual way the upper tree of the object
        Example:
        ...
            Part
                Sketch
                    Line
                        ...
        :return: string
        """
        string=''
        for i in range(len(self.order_list)):
            string += ' '*i*2 + '{}\n'.format(self.order_list[i])
        return string

    def __str__(self):
        return self._treeParent()

