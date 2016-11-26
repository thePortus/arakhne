import pip


class GetBase:
    pip_modules = []

    def __init__(self, language):
        self.language = language

    def packages(self):
        # Overridden by all child classes
        pass

    def modules(self):
        for module in self.pip_modules:
            pip.main(['install', module])
        print('Finished installing!')
        return True

    def all(self):
        self.modules()
        self.packages()
