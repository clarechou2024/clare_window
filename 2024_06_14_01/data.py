import requests
from requests import Response
from pydantic import BaseModel, RootModel, Field,field_validator,ConfigDict

def __download_json():
    url = "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"

    try:
        res:Response = requests.get(url)
    except Exception:
        raise Exception("連線失敗")
    else:
        all_data:dict[any] = res.json()
        return all_data
    

class Info(BaseModel):
    sna:str
    sarea:str
    mday:str
    ar:str
    act:str
    updateTime:str
    total:int
    rent_bikes:int = Field(alias="available_rent_bikes")
    lat:float = Field(alias="latitude")
    lng:float = Field(alias="longitude")
    retuen_bikes:int = Field(alias="available_return_bikes")

    model_config = ConfigDict(populate_by_name=True)   #兩種名稱都搜尋的到

    @field_validator("sna",mode='before')
    @classmethod
    def flex_string(cls, value:str)->str:
        return value.split(sep="_")[-1]   #sep:切掉

class Youbike_Data(RootModel):
    root:list[Info]

def load_data()->list[dict]:
    all_data:dict[any] = __download_json()
    youbike_data:Youbike_Data = Youbike_Data.model_validate(all_data)
    data = youbike_data.model_dump()
    return data



class FilterData(object):
    @staticmethod
    def get_selected_coordinate(sna:str,data:list[dict])->dict:
        #def abc(item:dict)->bool:     #用lambda可簡短程式
            #if item['sna'] == sna:
                #return True
            #else:
                #return False
        right_list:list[dict] = list(filter(lambda item:True if item['sna']==sna else False,data))
        data:dict = right_list[0]
        return Info.model_validate(data)

        ''' #可以和<  model_config = ConfigDict(populate_by_name=True)  >二選一

        return Info(sna=data['sna'],      
                    sarea=data['sarea'],
                    mday=data['mday'],
                    ar=data['ar'],
                    act=data['act'],
                    total=data['total'],
                    updateTime=data['updateTime'],
                    available_rent_bikes=data['rent_bikes'],
                    available_return_bikes=data['retuen_bikes'],
                    latitude=data['lat'],
                    longitude=data['lng']
                    )
        '''