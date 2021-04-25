from uis.loadingScreen import loadingScreen



class Main(loadingScreen):
    def __init__(self) -> None:
        super().__init__()

    def loadDependicies(self):
        """Load dependicies while function is loading in new thread"""
        
