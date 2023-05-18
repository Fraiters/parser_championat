import os
from lxml import etree
from lxml.builder import unicode
from lxml.etree import Element, SubElement
from article import Article
from crawler_championat.settings.xml_settings import XML_FOLDER, XML_TAGS, XML_ATTRIBUTES


class XmlConstructor:
    """Конструктор xml-документа"""

    def __init__(self, text_info: Article):
        # дата класс статьи с информацией
        self.text_info = text_info  # type: Article
        # название папки для xml-файлов
        self.xml_folder = ...  # type: str
        # полный путь до папки с xml-файлами
        self.path_xml_folder = ...  # type: str
        # имя xml-файла
        self.xml_name = ...  # type: str
        # содержимое xml-файла
        self.xml_content = ...  # type: str

    def create_folder(self, xml_folder: str = XML_FOLDER):
        """Создание директории для xml-файлов

        :param xml_folder: название директории для xml-файлов
        """
        # заполнение значения xml-папки
        self.xml_folder = xml_folder
        # заполнение значения полного пути до xml-папки
        self.path_xml_folder = os.path.abspath(xml_folder)
        # если папки не существует, то она создается
        if os.path.exists(self.path_xml_folder) is False:
            os.mkdir(xml_folder)

    def construct_structure(self):
        """Построение структуры xml-документа"""

        doc = XML_TAGS.get("DOC")
        # основной раздел doc (первый уровень)
        doc_section = Element(_tag=doc)

        # заполнение данных о категории
        if self.text_info.category is not None:
            # подраздел categories (второй уровень)
            categories = XML_TAGS.get("CATEGORIES")
            categories_section = self.add_subsection(parent_section=doc_section, tag=categories,
                                                     auto_value="true", type_value="list", verify_value="true")
            text_data = self.text_info.category
            # подраздел category (третий уровень)
            category = XML_TAGS.get("CATEGORY")
            self.add_subsection(parent_section=categories_section, tag=category, text=text_data,
                                type_value="str")

        # заполнение данных о заголовке
        if self.text_info.title is not None:
            text_data = self.text_info.title
            # подраздел title (второй уровень)
            title = XML_TAGS.get("TITLE")
            self.add_subsection(parent_section=doc_section, tag=title, text=text_data,
                                auto_value="true", type_value="str", verify_value="true")

        # заполнение данных об авторе
        if self.text_info.authors is not None:
            # подраздел authors (второй уровень)
            authors = XML_TAGS.get("AUTHORS")
            authors_section = self.add_subsection(parent_section=doc_section, tag=authors,
                                                  auto_value="true", type_value="list", verify_value="true")
            # добавление подразделов author (третий уровень)
            for author_data in self.text_info.authors:
                author = XML_TAGS.get("AUTHOR")
                text_data = author_data
                self.add_subsection(parent_section=authors_section, tag=author, text=text_data,
                                    type_value="str")

        # заполнение данных о дате
        if self.text_info.date is not None:
            text_data = self.text_info.date
            # подраздел date (второй уровень)
            date = XML_TAGS.get("DATE")
            self.add_subsection(parent_section=doc_section, tag=date, text=text_data,
                                auto_value="true", type_value="datetime", verify_value="true")

        # заполнение данных о тексте статьи
        if self.text_info.text is not None:
            text_data = self.text_info.text
            # подраздел text (второй уровень)
            text = XML_TAGS.get("TEXT")
            self.add_subsection(parent_section=doc_section, tag=text, text=text_data,
                                auto_value="true", type_value="str", verify_value="true")

        self.xml_content = etree.tostring(doc_section, pretty_print=True, encoding=unicode)

    def add_subsection(self, parent_section: Element, tag: str, text: str = "",
                       auto_value: str = "", type_value: str = "", verify_value: str = "") -> SubElement:
        """Добавление подраздела

        :param auto_value: значение auto
        :param type_value: значение type
        :param verify_value: значение verify
        :param parent_section: раздел (родитель подраздела)
        :param tag: тег добавляемого подраздела
        :param text: текст раздела (необязательный)

        :return section: объект SubElement созданного подраздела
        """
        # значения атрибутов
        auto_attr = XML_ATTRIBUTES.get("AUTO")
        type_attr = XML_ATTRIBUTES.get("TYPE")
        verify_attr = XML_ATTRIBUTES.get("VERIFY")
        # добавление элемента подраздела
        section = SubElement(_parent=parent_section, _tag=tag)
        if auto_value != "":
            # добавление атрибута auto
            section.set(auto_attr, auto_value)
        if type_value != "":
            # добавление атрибута type
            section.set(type_attr, type_value)
        if verify_value != "":
            # добавление атрибута verify
            section.set(verify_attr, verify_value)
        if text != "":
            # добавление текста
            section.text = etree.CDATA(text)
        # созданный подраздел
        return section

    def set_name(self):
        """Составление имени xml-файла"""
        self.xml_name = self.text_info.link.split('/')[2] + '.xml'

    def create_xml(self):
        """Создание xml-файла"""
        self.create_folder()
        self.construct_structure()
        self.set_name()

        with open(os.path.join(self.path_xml_folder, self.xml_name), 'w', encoding="utf-8") as xml_file:
            xml_file.write(self.xml_content)
