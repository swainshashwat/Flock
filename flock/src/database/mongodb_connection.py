from pymongo import MongoClient

class MongoDatabase(object):
    def __init__(self, uri, db_name):
        self.client = MongoClient(uri)
        self.db = self.clinet[db_name]

    def get_collection(self, collection_name):
        return self.db[collection_name]
    
    def find_documents(self, collection_name, filter_dict = None, limit=None, use_generator=False):
        """
        Find documents in a collection based on a filter.

        :param collection_name: The name of the collection to search.
        :param filter_dict: A dictionary containing filters (optional).
        :param limit: Maximum number of documents to retrieve (optional).
        :param use_generator: Whether to use a generator (default is True).
        :return: A generator yielding matching documents (if use_generator is True), otherwise a list.
        """
        collection = self.get_collection(collection_name)
        try:
            if filter_dict is None:
                cursor = collection.find()

            else:
                cursor = collection.find(filter_dict)

            if limit:
                cursor.limit(limit)

            if use_generator:
                for document in cursor:
                    yield document

            else:
                return list(cursor)
        except Exception as e:
            return f"Error occured: {str(e)}"