
class GetAllCategoryInteractor:
    def __init__(self, category_repo):
        self.category_repo = category_repo

    def set_params(self, *args, **kwargs):
        return self

    def execute(self):
        body = self.category_repo.get_all()
        return body


class CreateCategoryInteractor:
    def __init__(self, category_repo):
        self.category_repo = category_repo
    
    def set_params(self, *args, **kwargs):
        self.data = kwargs
        return self
    
    def execute(self):
        return self.category_repo.create(self.data)
    

class RetrieveCategoryInteractor:
    def __init__(self, category_repo):
        self.category_repo = category_repo

    def set_params(self, *args, **kwargs):
        self.pk = kwargs.get('pk', None)
        return self

    def execute(self, *args, **kwargs):
        body = self.category_repo.get_by_id(self.pk)
        return body


class UpdateCategoryInteractor:
    def __init__(self, category_repo):
        self.category_repo = category_repo

    def set_params(self, *args, **kwargs):
        self.pk = kwargs.get('pk', None)
        self.data = kwargs
        return self
    
    def execute(self):
        self._validate()
        return self.category_repo.update(self.data)


    def _validate(self):
        pass


class DeleteCategoryInteractor:
    def __init__(self, category_repo):
        self.category_repo = category_repo
    
    def set_params(self, *args, **kwargs):
        self.pk = kwargs.get('pk', None)
    
    def execute(self):
        self.category_repo.delete(self.pk)
        return True