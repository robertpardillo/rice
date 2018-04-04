
from win32com.client import dynamic
from .miscellaneous.orderDict import OrderDict
import inspect
import re
from .collectionsObject.documents import Documents
from .collectionsObject.windows import Windows
from .abstractObjects.documents.part import Part


class Application(object):
    """

        Root class which is the origin of the rest. It contains all the objects and all the instantiated data.

        It initializes connection with CATIA.

    """

    def __init__(self, visible=True):
        """

        :param visible: Catia's window visible or not
        :type visible: bool
        """
        self.parent = None
        self.cat_constructor = dynamic.Dispatch("CATIA.Application")
        self.cat_constructor.Visible = visible
        self.name = self.cat_constructor.Name
        self.parentsDict = OrderDict()
        self.parentsDict[self.name] = self
        self.documents_COLL = Documents(self.parentsDict._copy())
        self.windows_COLL = Windows(self.parentsDict._copy())
        caller = inspect.getouterframes(inspect.currentframe())[1][1]
        caller = re.findall('([a-z]*)\.py.*', caller)[0]
        if caller in ['part', 'product', 'drawing']:
            print('Not create Document')
            pass
        else:
            self.documents_COLL.add('Part')
            pass

    def add_part(self):
        """
            Add a Part
        """
        self.documents_COLL.add('Part')

    def get_parts(self):
        """
        Get all created Parts

        :return: list of created Parts
        :rtype: list of :class:`~Rice.abstractObjects.documents.part.Part`
        """
        result = list()
        for i in self.documents_COLL.deque:
            result.append(i.Part)
        return result

    def active_document(self):
        """
        TO-DO
        """
        return self.value

    def active_window(self):
        return self.value

    def documents(self):
        return self.value

    def windows(self):
        return self.value

    def visible(self):
        return self.value

    def quit(self):
        self.cat_obj.Quit()

