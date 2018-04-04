

class AnyObject(object):
    """
    def get_address(self):
        order_list = self.parentsDict.order_list
        address = list()
        for i in range(len(order_list))[::-1]:
            if isinstance(self.parentsDict[order_list[i]], Collection):
                continue
            elif isinstance(self.parentsDict[order_list[i]], Part):
                address.append(order_list[i])
                break
            address.append(order_list[i])
        string_address = ""
        for i in address[::-1]:
            string_address += "{}\\".format(i)

        return string_address[0:-1]
    """
    @property
    def name(self):
        return self.cat_constructor.Name

    @name.setter
    def name(self, value):
        self.cat_constructor.Name = value
