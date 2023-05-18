from crawler_championat.article import Article
from xml_constructor import XmlConstructor


class ParserChampionat:
    """Парсер для статей с сайта championat.com
    (собирает информацию о статьях и сохраняет ее в xml-файлах)"""

    def run(self):
        """Запуск парсера"""
        # создание объекта статьи
        article_obj = Article()
        # получение значений атрибутов статьи (категория, заголовок, авторы, дата, текст)
        articles = article_obj.get_article_attributes()
        for article in articles:
            # создание объекта xml-конструктора
            xml_constructor = XmlConstructor(text_info=article)
            # заполнение и создание xml-файла
            xml_constructor.create_xml()


if __name__ == '__main__':
    crawler_championat = ParserChampionat()
    crawler_championat.run()
