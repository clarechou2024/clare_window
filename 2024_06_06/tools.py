import requests
from requests import JSONDecodeError 
from pydantic import BaseModel,RootModel,Field,field_validator
from datetime import datetime

class Site(BaseModel):
    site_name:str = Field (alias='sitename')
    county:str
    aqi:int
    status:str
    pm25:float = Field(alias='pm2.5')
    date:str = Field(alias='datacreationdate')

    @field_validator("pm25",mode='before')   #自訂驗證:@field_validator
    @classmethod
    def abc(cls, value:str)->str:            #cls-->class
        if value=="":                        #if值為空字串
           return "0.0"                      #回傳字串:0.0
        else:
            return value

class Records(RootModel):
    root: list[Site]

def download_json()->dict[any]:    #將槽狀結構簡化:建立function
    aqi_url = 'https://data.moenv.gov.tw/api/v2/aqx_p_488?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate desc&format=JSON'
    try:
        response = requests.get(aqi_url)
    except Exception:
        raise Exception("連線失敗")
    else:
        if response.status_code == 200:
            try:                              #pythony資料結構為[dict]和{list}
                all_data:dict[any] = response.json() #json字串轉換成python的資料結構
                return all_data
            except JSONDecodeError:
                raise Exception("api_key為測試用,連線以至上限,請稍後再試")
        else:
           raise Exception("下載狀態碼不是200")
        
def get_data(all_data:dict[any])->list[dict]:  #all_data驗證後傳出->list[dict]
    records:Records = Records.model_validate(all_data['records'])  #python的資料結構用:model_validate
    data:list[dict] = records.model_dump()
    return data

class AQI(object):  #沒有繼承人用:object
    '''
    利用class attribute aqi_records儲存下載資料
    利用class attribute update_time儲存下載時間
    '''
    aqi_records:list[dict] | None = None
    update_time:datetime | None = None