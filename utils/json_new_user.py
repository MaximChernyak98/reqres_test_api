class JSON_new_user():

    @staticmethod
    def create_minimum_json(email, name, tasks, companies):
        json = {
            "email": email,
            "name": name,
            "tasks": tasks,
            "companies": companies
        }
        return json
