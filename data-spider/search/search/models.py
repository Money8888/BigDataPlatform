# -*- coding: utf-8 -*-
__author__ = 'bobby'

from datetime import datetime
import elasticsearch_dsl
# DocType
from elasticsearch_dsl import Document, Date, Nested, Boolean, \
    analyzer, Completion, Keyword, Text, Integer
# InnerObjectWrapper

from elasticsearch_dsl.analysis import CustomAnalyzer as _CustomAnalyzer

from elasticsearch_dsl.connections import connections

connections.create_connection(hosts=["127.0.0.1"])


class CustomAnalyzer(_CustomAnalyzer):
    def get_analysis_definition(self):
        return {}


ik_analyzer = CustomAnalyzer("ik_max_word", filter=["lowercase"])


class Article(Document):
    title_suggest = Completion(analyzer=ik_analyzer, search_analyzer=ik_analyzer)
    title = Text(analyzer='ik_max_word', search_analyzer="ik_max_word", fields={'title': Keyword()})
    id = Text()
    url = Text()
    front_image_url = Text()
    front_image_path = Text()
    create_date = Date()
    praise_nums = Integer()
    comment_nums = Integer()
    fav_nums = Integer()
    tags = Text(analyzer='ik_max_word', fields={'tags': Keyword()})
    content = Text(analyzer='ik_max_word')

    class Meta:
        index = ''
        doc_type = 'jobbole_article'


if __name__ == "__main__":
    Article.init()
