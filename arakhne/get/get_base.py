import pip


class GetBase:
    pip_modules = []

    def __init__(self, language):
        self.language = language

    def install(self):
        for module in self.pip_modules:
            pip.main(['install', module])
        print('Finished installing!')
        return True
