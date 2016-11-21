import pip


class GetBase:
    pip_modules = []

    def install(self):
        for module in self.pip_modules:
            pip.main(['install', module])
        print('Finished installing!')
        return True
