# parser_championat- Приложение парсинга сайта championat.com

# Пакеты:

# 1. `settings` - пакет настроек приложения

# Модули:

- ## `server_settings.py` - набор серверных настроек для обращения к сайту championat.com
- ## `xpath_settings.py` - набор настроек путей для поиска - xpath
- ## `xml_settings.py` - набор настроек для создания xml-документа

# 2. `crawler_championat`

# Модули:

- ## `article_page.py` - модуль для работы с общей страницей, где отображаются статьи
    - ## Классы:
        - ### `ArticlesPage` - Класс работы со страницей, где отображаются статьи
            - #### `set_articles_links(html_content: str)` - Заполнение списка ссылок на статьи

- ## `article.py` - модуль для обработки и получения всей информации о статьях
    - ## Классы:
        - ### `Article` - Класс работы со статьей
            - #### `get_general_articles_links()` - Получение общего списка ссылок на статьи (генератор - возвращает ссылки на каждой странице)
            - #### `is_article_page()` - Проверка, что ссылка ведет на страницу статьи (т.к. есть, например, статьи-истории, в которых структура html-страницы отличается, в данной работе такие статьи не рассматриваются)
            - #### `set_content()` - Заполнение html-текста страницы
            - #### `set_category()` - Заполнение категории статьи
            - #### `set_title()` - Заполнение заголовка статьи
            - #### `set_author()` - Заполнение списка авторов статьи
            - #### `set_date()` - Заполнение даты статьи
            - #### `set_text()` - Заполнение текста статьи
            - #### `set_article_attributes()` - Заполнение всех атрибутов статьи
            - #### `get_article_attributes()` - Получение всех заполненных атрибутов статьи

- ## `xml_constructor.py` - модуль для построения структуры xml-документа с данными о статье
    - ## Классы:
        - ### `XmlConstructor` - Конструктор xml-документа
          - #### `create_folder(xml_folder: str = XML_FOLDER)` - Создание директории для xml-файлов
          - #### `construct_structure()` - Построение структуры xml-документа
          - #### `add_subsection(parent_section: Element, tag: str, text: str = "", auto_value: str = "", type_value: str = "", verify_value: str = "")` - Добавление подраздела
          - #### `set_name()` - Составление имени xml-файла
          - #### `create_xml()` - Создание xml-файла

- ## `parser_championat.py` - модуль для запуска парсинга
    - ## Классы:
        - ### `ParserChampionat` - Парсер для статей с сайта championat.com (собирает информацию о статьях и сохраняет ее в xml-файлах)
        - #### `run()` - Запуск парсера
