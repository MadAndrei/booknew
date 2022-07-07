from book import BookAPIDe, BookAPIEn, BookAPIRu


def create_routes(api):
    api.add_resource(BookAPIDe, '/de')
    api.add_resource(BookAPIEn, '/en')
    api.add_resource(BookAPIRu, '/ru')

