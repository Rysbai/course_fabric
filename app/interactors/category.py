
class GetAllCategoryInteractor:
    def __init__(self, category_repo):
        self.category_repo = category_repo

    def set_params(self, *args, **kwargs):
        return self

    def execute(self):
        body = self.category_repo.get_all()
        return body


class CreateCategoryInteractor:
    def __init__(self, category_entity, category_repo):
        self.category_entity = category_entity
        self.category_repo = category_repo
    
    def set_params(self, *args, **kwargs):
        self.data = kwargs
        return self
    
    def execute(self):
        category = self.category_entity.create(**self.data)
        return self.category_repo.create(category)
    

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
    def __init__(self, category_entity, category_repo):
        self.category_entity = category_entity
        self.category_repo = category_repo

    def set_params(self, *args, **kwargs):
        print(kwargs)
        self.pk = kwargs.get('pk', None)
        self.data = kwargs
        return self
    
    def execute(self):
        self._validate()
        category = self.category_entity.create(**self.data)
        return self.category_repo.update(category)

    def _validate(self):
        pass


class DeleteCategoryInteractor:
    def __init__(self, category_repo):
        self.category_repo = category_repo
    
    def set_params(self, *args, **kwargs):
        self.pk = kwargs.get('pk', None)
        return self
    
    def execute(self):
        self.category_repo.delete(self.pk)
        return True
