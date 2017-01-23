from .. import Arakhne


class BaseFixtureLayer:

    @classmethod
    def setUp(cls):
        cls.arakne = Arakhne(cls.language)
