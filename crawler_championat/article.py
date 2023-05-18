from typing import *
import lxml.html
import requests
from articles_page import ArticlesPage
from crawler_championat.settings.server_settings import BASE_URL, HEADERS, PAGE_URL, START_PAGE, FINAL_PAGE
from crawler_championat.settings.xpath_settings import \
    XPATH_TITLE, XPATH_CATEGORY, XPATH_HTML_CLASS, XPATH_AUTHOR, XPATH_DATE, XPATH_TEXT


class Article:
    """Класс работы со статьей"""
    # ссылка на статью
    link = None  # type: str
    # общий html-текст страницы
    html_content = None  # type: str
    # категория статьи
    category = None  # type: str
    # заголовок статьи
    title = None  # type: str
    # авторы статьи
    authors = None  # type: List[str]
    # дата публикации статьи
    date = None  # type: str
    # текст статьи
    text = None  # type: str

    def get_general_articles_links(self) -> List[str]:
        """Получение общего списка ссылок на статьи
        (генератор - возвращает ссылки на каждой странице)

        :return links: список ссылок на одной странице
        """
        # проход по всем страницам со статьями от START_PAGE до FINAL_PAGE
        for number_page in range(START_PAGE, FINAL_PAGE + 1):
            # запрос на данные одной html-страницы
            response = requests.get(
                url=PAGE_URL.format(number_page=number_page),
                headers=HEADERS)
            # получение html-текста страницы и перевод в формат строки
            content = str(response.content)
            # создание объекта страницы со статьями
            articles_page = ArticlesPage()
            # получение списка ссылок на статьи
            articles_page.set_articles_links(html_content=content)
            links = articles_page.articles_links
            yield links

    def is_article_page(self) -> bool:
        """Проверка, что ссылка ведет на страницу статьи
        (т.к. есть, например, статьи-истории, в которых структура html-страницы отличается,
        в данной работе такие статьи не рассматриваются)"""

        tree = lxml.html.document_fromstring(self.html_content)
        # поиск класса страницы по шаблону
        class_page = tree.xpath(XPATH_HTML_CLASS)
        # если класс нашелся (длина списка не нуль), то возвращается True
        if len(class_page) != 0:
            return True
        # иначе False
        else:
            return False

    def set_content(self):
        """Заполнение html-текста страницы"""
        # составление url ссылки
        url = BASE_URL + self.link
        # запрос на данные одной html-страницы
        response = requests.get(url=url, headers=HEADERS)
        # заполнение html-текста страницы и перевод в формат строки
        self.html_content = str(response.content.decode(encoding='utf-8', errors='strict'))

    def set_category(self):
        """Заполнение категории статьи"""
        # получение категории на английском из ссылки
        category_value = self.link.split('/')[1]
        tree = lxml.html.document_fromstring(self.html_content)
        # заполнение значения категории с помощью xpath
        categories = tree.xpath(XPATH_CATEGORY.format(category_value=category_value))
        self.category = categories[0]

    def set_title(self):
        """Заполнение заголовка статьи"""
        tree = lxml.html.document_fromstring(self.html_content)
        # заполнение значения заголовка с помощью xpath
        titles = tree.xpath(XPATH_TITLE)
        self.title = titles[0]

    def set_author(self):
        """Заполнение списка авторов статьи"""
        tree = lxml.html.document_fromstring(self.html_content)
        # заполнение списка авторов с помощью xpath
        authors = tree.xpath(XPATH_AUTHOR)
        self.authors = authors

    def set_date(self):
        """Заполнение даты статьи"""
        tree = lxml.html.document_fromstring(self.html_content)
        # заполнение значения даты с помощью xpath
        dates = tree.xpath(XPATH_DATE)
        self.date = dates[0]

    def set_text(self):
        """Заполнение текста статьи"""
        tree = lxml.html.document_fromstring(self.html_content)
        # заполнение значения текста с помощью xpath
        texts = tree.xpath(XPATH_TEXT)
        # объединение всех текстовых блоков
        self.text = ' '.join(texts)

    @classmethod
    def set_article_attributes(cls):
        """Заполнение всех атрибутов статьи

        :return article: объект Article с заполненными атрибутами
        """
        # вызов генератора, получение ссылок на статьи с одной страницы
        all_links = cls().get_general_articles_links()
        # номер текущей статьи
        cur_article_number = 0  # type: int
        for links in all_links:
            # проход по каждой ссылке
            for link in links:
                # создание объекта статьи
                article = cls()
                # заполнение ссылки на статью
                article.link = str(link)
                # заполнение html-текста страницы
                article.set_content()
                # счетчик статей
                cur_article_number += 1
                # если ссылка не ведет на страницу статьи, то происходит следующая итерация
                if article.is_article_page() is False:
                    print("Статья номер {cur_article_number} - пропущена"
                          .format(cur_article_number=cur_article_number))
                    continue
                # заполнение значения категории
                article.set_category()
                # заполнение значения заголовка
                article.set_title()
                # заполнение значения списка авторов
                article.set_author()
                # заполнение значения даты
                article.set_date()
                # заполнение значения текста
                article.set_text()
                print("Статья номер {cur_article_number} - обработана"
                      .format(cur_article_number=cur_article_number))
                yield article

    def get_article_attributes(self):
        """Получение всех заполненных атрибутов статьи"""
        articles = self.set_article_attributes()
        for article in articles:
            yield article
