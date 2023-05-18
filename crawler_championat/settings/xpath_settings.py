# Набор настроек для XPATH:

# xpath до ссылки на статью
XPATH_HREF = "/html/body" \
             "/div[contains(@class, 'page')]" \
             "/div[contains(@class, 'page-content')]" \
             "/div[contains(@class, 'page-main')]" \
             "/div[contains(@class, 'article-preview-list')]" \
             "/div[contains(@class, 'article-preview')]" \
             "/div[contains(@class, 'article-preview__img')]" \
             "/a[starts-with(@href, '/')]/@href"

# xpath до класса html-страницы
XPATH_HTML_CLASS = "/html[contains(@class, 'article-page')]/@class"

# xpath до заголовка статьи
XPATH_TITLE = "/html/body" \
              "/div[contains(@class, 'page')]"\
              "/div[contains(@class, 'page-content')]" \
              "/div[contains(@class, 'page-main')]" \
              "/article/header" \
              "/div[contains(@class, 'article-head__title')]/text()"

# xpath до категории статьи
XPATH_CATEGORY = "/html/body" \
                 "/div[contains(@class, 'page')]" \
                 "/div[contains(@class, 'breadcrumbs')]" \
                 "/a[contains(@href, '{category_value}')]/text()"

# xpath до авторов статьи
XPATH_AUTHOR = "/html/body" \
               "/div[contains(@class, 'page')]" \
               "/div[contains(@class, 'page-content')]" \
               "/div[contains(@class, 'page-main')]" \
               "/article/header" \
               "/div[contains(@class, 'article-head__details')]" \
               "/div[contains(@class, 'article-head__author')]" \
               "/div[contains(@class, 'article-head__author-name')]" \
               "/a/span/text()"

# xpath до даты статьи
XPATH_DATE = "/html/body" \
             "/div[contains(@class, 'page')]" \
             "/div[contains(@class, 'page-content')]" \
             "/div[contains(@class, 'page-main')]" \
             "/article/header" \
             "/div[contains(@class, 'article-head__details')]" \
             "/time/text()"

# xpath до текста статьи
XPATH_TEXT = "/html/body" \
             "/div[contains(@class, 'page')]" \
             "/div[contains(@class, 'page-content')]" \
             "/div[contains(@class, 'page-main')]" \
             "/article" \
             "/div[contains(@class, 'article-content')]" \
             "//p//text()"
