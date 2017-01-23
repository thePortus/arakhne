from .. import Arakhne


class BaseFixtureLayer:

    @classmethod
    def setUp(cls):
        cls.arakne = Arakhne(None)


class EnglishFixtureLayer:

    @classmethod
    def setUp(cls):
        cls.arakhne = Arakhne('english')


class LatinFixtureLayer:

    @classmethod
    def setUp(cls):
        cls.arakhne = Arakhne('latin')


class GreekFixtureLayer:

    @classmethod
    def setUp(cls):
        cls.arakhne = Arakhne('greek')
