class DatabaseError(Exception):
    """Generic DB exception"""

    error_dict = None

    def __init__(self, *args, error_dict: dict = None):
        super().__init__(*args)
        self.error_dict = error_dict

    pass


class DataBaseIntegrityError(DatabaseError):
    def __init__(self, *args, error_dict = None):
        super().__init__(*args, error_dict=error_dict)
    pass


class NotFoundError(DatabaseError):
    pass