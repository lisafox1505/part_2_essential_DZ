class LinkShortService:

    def __init__(self, dict_user):
        self.dict_user = dict_user

    def check_key(self, key):
        return key in self.dict_user

    def add_new_data(self, name, url):
        self.dict_user[name] = url

    def get_link(self, key):
        return self.dict_user.get(key, "Такого ім'я не існує")

    def show_all_keys(self):
        return list(self.dict_user.keys())

    def del_link(self, key):
        del self.dict_user[key]