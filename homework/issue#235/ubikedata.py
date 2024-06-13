import requests
from datetime import datetime    #做一個datetime的型別
from pydantic import BaseModel, RootModel,Field,field_serializer

def download_json()->list[any]:   
    aqi_url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
    try:
        response = requests.get(aqi_url)
    except Exception:
        raise Exception("連線失敗")
    else:
        all_data:list[any] = response.json()
        return all_data
    
class Site(BaseModel):          #先做內層的,dict{}用->BaseModel

    sna:str
    sarea:str
    mday:datetime
    ar:str
    act:bool        #布林值:1->營業中;0->維護中
    updateTime:datetime          #放datetime型別
    total:int
    available_rent_bikes:int
    latitude:float
    longitude:float
    available_return_bikes:int

    @field_serializer("mday","updateTime")    #註冊field_serializer:變更日期模式
    def serialize_str(self,value:datetime)->str:   #自訂日期模式->自訂變數為字串
        return value.strftime('%Y-%m-%d %p%I:%M:%S')  
    
    @field_serializer("sna")
    def serializer_split(self,value:str)->str:   
        return value.split('_')[-1]
    
    @field_serializer("act")
    def serializer_act(self,value:bool)->str:
        if bool:
            return "營業中"
        else:
            return"維護中"
    

class Records(RootModel):
    root: list[Site]


def load_data() -> list[dict]:
    all_data:list[any] = download_json()
    records:Records = Records.model_validate(all_data) 
    data = records.model_dump()  #model_dump:傳出python的資料結構
    return data