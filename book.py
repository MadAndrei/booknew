from flask_restful import Resource, reqparse
from models import BookDe, BookEn, BookRu


def parse():
    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str, help="title didn't send", required=True)
    parser.add_argument('url', type=str, help="url didn't send", required=True)
    parser.add_argument('abstract', type=str, help="abstract didn't send", required=True)
    parser.add_argument('body_text', type=str, help="body_text didn't send", required=True)
    parser.add_argument('html_body', type=str, help="html_body didn't send", required=True)
    return parser


class BookAPIDe(Resource):
    def __init__(self):
        self.parser = parse()

    def get(self):
        result = BookDe.query.limit(5).all()
        return [elem.title for elem in result]

    def put(self):
        args = self.parser.parse_args()
        new_book = BookDe(**args)
        new_book.save()
        return args


class BookAPIEn(Resource):
    def __init__(self):
        self.parser = parse()

    def get(self):
        result = BookEn.query.limit(5).all()
        return [elem.title for elem in result]

    def put(self):
        args = self.parser.parse_args()
        new_book = BookEn(**args)
        new_book.save()
        return args


class BookAPIRu(Resource):
    def __init__(self):
        self.parser = parse()

    def get(self):
        result = BookRu.query.limit(5).all()
        return [elem.title for elem in result]

    def put(self):
        args = self.parser.parse_args()
        new_book = BookRu(**args)
        new_book.save()
        return args
