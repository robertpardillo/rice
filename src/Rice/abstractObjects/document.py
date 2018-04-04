
import inspect
import re
from ..baseClasses.anyObject import AnyObject


class Document(AnyObject):
    def __init__(self, parent=None, document_type=None):
        """

        :param parent: Application Object
        :param document_type:   Part

        """
        self.parent = parent[parent[-1]]
        self.parentsDict = parent
        self.cat_constructor = self.parent.cat_constructor.Add(document_type)
        self.parentsDict[self.name] = self
        cls = __import__('abstractObjects.documents.{}'.format(document_type.lower()), globals(), locals(), [document_type], level=2)
        cls = cls.__dict__[document_type]

        self.__setattr__(document_type, cls(self.parentsDict._copy()))

    def export_data(self, file_path, extension):
        self.cat_constructor.ExportData(file_path, extension)

    def save(self, file_path):
        self.cat_constructor.SaveAs(file_path)
