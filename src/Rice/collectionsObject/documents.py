import inspect
import re
from ..baseClasses.collection import Collection
from ..abstractObjects.document import Document


class Documents(Collection):
    """
        Application
            Documents
                Document ----> Part, Product, Drawing

        Document class
    """
    def __init__(self, parents_dict):
        super(Documents, self).__init__(parents_dict, 'Documents')
        self.imported = list()

    def add(self, docType):
        """

        Initialize and instance an object of the class imported, then adds it to the deque.

        :param args:
        :return:
        """

        obj = Document(self.parentsDict._copy(), docType)
        self.deque.append(obj)
        return obj

    def item(self, index_name):
        if isinstance(index_name, int):
            return self.deque[index_name]
        elif isinstance(index_name, str):
            for i in self.deque:
                if i.Name == index_name:
                    return i

    def new_from(self, file_path):
        pass

    def open(self, file_path):
        pass

    def read(self, file_path):
        pass

