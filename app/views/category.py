from .status_codes import Status


class CategoryListCreateView:
    def __init__(self,
                 get_all_interactor_factory,
                 create_interactor_factory
                 ):
        self.get_all_interactor_factory = get_all_interactor_factory
        self.create_interactor_factory = create_interactor_factory

    def get(self, *args, **kwargs):
        body = self.get_all_interactor_factory.create().set_params(*args, **kwargs).execute()
        return body.__dict__, Status.OK

    def post(self, *args, **kwargs):
        body = self.create_interactor_factory.create().set_params(*args, **kwargs).execute()
        return body.__dict__, Status.CREATED


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
        body = self.retrieve_interactor_factory.create().set_params(*args, **kwargs).execute()
        return body, Status.OK

    def put(self, *args, **kwargs):
        body = self.update_interactor_factory.create().set_params(*args, **kwargs).execute()
        return body, Status.CREATED

    def delete(self, *args, **kwargs):
        body = self.delete_interactor_factory.create().set_params(*args, **kwargs).execute()
        return body, Status.NO_CONTENT

