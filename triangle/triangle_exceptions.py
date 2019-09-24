class Error(Exception):
    """Base Exception Class For Other Exceptions"""
    pass


class NotAValidTriangleError(Error):
    """Raised When the object is not a triangle """

class NotProvidedSidesOrAnglesError(Error):
    """if sides or angles is not provided in init class raise this error"""