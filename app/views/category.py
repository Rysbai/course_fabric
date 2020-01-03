from .status_codes import Status
from app.serializers.category import CategorySerializer


class CategoryListCreateView:
    def __init__(self,
                 get_all_interactor_factory,
                 create_interactor_factory
                 ):
        self.get_all_interactor_factory = get_all_interactor_factory
        self.create_interactor_factory = create_interactor_factory

    def get(self, *args, **kwargs):
        body = self.get_all_interactor_factory.create().set_params(*args, **kwargs).execute()
        return CategorySerializer.serialize_many(body), Status.OK

    def post(self, *args, **kwargs):
        body = self.create_interactor_factory.create().set_params(*args, **kwargs).execute()
        return CategorySerializer.serialize_entity(body), Status.CREATED


class CategoryRetrieveUpdateDeleteView:
    def __init__(self,
                 retrieve_interactor_factory,
                 update_interactor_factory,
                 delete_interactor_factory
                 ):
        self.retrieve_interactor_factory = retrieve_interactor_factory
        self.update_interactor_factory = update_interactor_factory
        self.delete_interactor_factory = delete_interactor_factory

    def get(self, *args, **kwargs):
        print('Im here')
        body = self.retrieve_interactor_factory.create().set_params(*args, **kwargs).execute()
        return CategorySerializer.serialize_entity(body), Status.OK

    def put(self, *args, **kwargs):
        body = self.update_interactor_factory.create().set_params(*args, **kwargs).execute()
        return CategorySerializer.serialize_entity(body), Status.CREATED

    def delete(self, *args, **kwargs):
        self.delete_interactor_factory.create().set_params(*args, **kwargs).execute()
        return None, Status.NO_CONTENT
