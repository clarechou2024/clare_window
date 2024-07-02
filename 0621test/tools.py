import pandas as pd


value=1000

class A():
    def __init__(self) -> None:
        self.value=0
        self.text=0
        self.__date    

    @property
    def date():
        return "123"

    def CCC(self):
        pass

def calculate_rsi(data:pd.DataFrame, window=14)->pd.Series:

    delta = pd.Series(data['收盤價'].astype(float).values).diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    
    
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    
    return rsi

def CCC():
    return "123"