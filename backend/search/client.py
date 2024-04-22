from algoliasearch_django import algolia_engine

def get_client():
    return algolia_engine.client

def get_index(index_name='product'):
    # cfe_Article
    client = get_client()
    index = client.init_index(index_name)
    return index


def perform_search (query , **kwargs):
    index = get_index()
    return index.search(query)