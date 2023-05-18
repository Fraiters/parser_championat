# начальный номер html-страницы со статьями
START_PAGE = 1
# конечный номер html-страницы со статьями
FINAL_PAGE = 50

# Набор настроек для URL:

# базовая ссылка на сайт
BASE_URL = "https://www.championat.com"
# указываются заголовки для избежания ошибочного статуса кода 403 при выполнении запроса
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}
# ссылка на страницу с перечнем статей
PAGE_URL = "https://www.championat.com/articles/{number_page}.html"
