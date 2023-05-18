import lxml.html
from typing import *
from crawler_championat.settings.xpath_settings import XPATH_HREF


class ArticlesPage:
    """Класс работы со страницей, где отображаются статьи"""
    # список ссылок на статьи (на одной html-странице)
    articles_links = []  # type: List[str]

    def set_articles_links(self, html_content: str):
        """Заполнение списка ссылок на статьи

        :param html_content: html-текст (ответ, приходящий с запроса)
        """
        # преобразование строки в формат html
        tree = lxml.html.document_fromstring(html_content)
        # заполнение списка ссылок на статьи с помощью xpath
        self.articles_links = tree.xpath(XPATH_HREF)
