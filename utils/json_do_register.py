class JSON_do_register():

    @staticmethod
    def create(email, name, password):
        json = {
            "email": email,
            "name": name,
            "password": password
        }
        return json
