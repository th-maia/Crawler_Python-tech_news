import sys
from typing import List, Type
from tech_news.core.base_option import BaseOption
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_category,
    search_by_date,
)
from tech_news.analyzer.ratings import top_5_categories
from tech_news.scraper import get_tech_news


Option = Type[BaseOption]


class FillDatabase(BaseOption):
    desc = "Popular o banco com notícias"

    @classmethod
    def _exec(cls):
        amount = int(
            input("Digite quantas notícias serão buscadas:")
        )
        return get_tech_news(amount)


class FindByTitle(BaseOption):
    desc = "Buscar notícias por título"

    @classmethod
    def _exec(cls):
        title = input("Digite o título:")
        return search_by_title(title)


class FindByDate(BaseOption):
    desc = "Buscar notícias por data"

    @classmethod
    def _exec(cls):
        date = input("Digite a data no formato aaaa-mm-dd:")
        return search_by_date(date)


class FindByCategory(BaseOption):
    desc = "Buscar notícias por categoria"

    @classmethod
    def _exec(cls):
        category = input("Digite a categoria:")
        return search_by_category(category)


class TopFiveCategories(BaseOption):
    desc = "Listar top 5 categorias"

    @classmethod
    def _exec(cls):
        return top_5_categories()


class Quit(BaseOption):
    desc = "Sair"

    @classmethod
    def _exec(cls):
        return "Encerrando script"


class AnalyserMenu:
    def __init__(self, _options: List[Option]):
        self.options = _options

    def str_options(self):
        _str_options = ';\n '.join([
            f'{index} - {option.desc}'
            for index, option
            in enumerate(self.options)
        ])

        return (
            f"Selecione uma das opções a seguir:\n {_str_options}.\n")

    def start(self):
        try:
            user_choice = int(input(self.str_options()))
            res = self.options[user_choice].exec()
            print(res)
        except (IndexError, ValueError):
            sys.stderr.write("Opção inválida\n")


OPTIONS: List[Option] = [
    FillDatabase,
    FindByTitle,
    FindByDate,
    FindByCategory,
    TopFiveCategories,
    Quit,
]


def analyzer_menu():
    AnalyserMenu(OPTIONS).start()
