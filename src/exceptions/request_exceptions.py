class BadRequestError(Exception):
    error_dict = None

    def __init__(self, *args, error_dict=None):
        super().__init__(*args)
        self.error_dict = error_dict


class InvalidJSONError(BadRequestError):
    error_dict = {"data": "invalid_json"}

    def __init__(self, *args, error_dict=None):
        super().__init__(*args)
        self.error_dict = error_dict


