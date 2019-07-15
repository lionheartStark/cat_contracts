# -*- coding: utf-8 -*-
import os.path
import glob


class CatContr():
    """
        use for cat contracts and then get the source map
    """
    def __init__(self,
                 file_path=os.path.abspath('.')+"/contracts",
                 ):
        self.file_path = file_path
        self.main_contracts = {}
        pass

    def sol_file_added(self):
        pass

    def del_uesless_file(self):
        pass

    def get_main_contracts(self):
        for filename in glob.glob(self.file_path+r"/*.sol"):
            self.main_contracts[filename] = []
        pass

    def get_import_contracts(self, path):
        pass



if __name__ == '__main__':
    CatContrqy = CatContr()
    CatContrqy.get_main_contracts()
    for main_contr in CatContrqy.main_contracts:
        print(main_contr)
        pass
    pass























