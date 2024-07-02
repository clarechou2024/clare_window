import requests
import datetime as dt # 時間套件
import pandas as pd
from pydantic import BaseModel,RootModel,Field
from datetime import datetime
from dateutil.relativedelta import relativedelta

def Get_N_Month_Data(month_num:int,stock_id:int) ->pd.DataFrame:
# 當日時間
    date_now = dt.datetime.now()

    # 建立日期串列
    date_list = [(date_now - relativedelta(months=i)).replace(day=1).\
                strftime('%Y%m%d') for i in range(month_num)]
    date_list.reverse()

    # 用於存儲每個月的數據
    all_data = []

    # 使用迴圈抓取連續月份資料
    for date in date_list:
        url = f'https://www.twse.com.tw/rwd/zh/afterTrading/\
            STOCK_DAY?date={date}&stockNo={stock_id}'
        try:
            json_data = requests.get(url).json()

            df = pd.DataFrame(data=json_data['data'],
                            columns=json_data['fields'])
        
            all_data.append(df)

        except Exception as e:
            print(f"無法取得{date}的資料, 可能資料量不足.")

    # 合併所有月份的數據
    if all_data:
        final_df = pd.concat(all_data, ignore_index=True)
    else:
        final_df = pd.DataFrame()

    return final_df
    
def Get_Data_Dict(data:pd.DataFrame)->dict:
    
    try:
        if not data.empty: 
            columns_list = data.columns.tolist()
            datas_list = data.values.tolist()

            final_dict_list = []
            for row in datas_list:
                row_dict = {columns_list[i]: row[i] for i in range(len(columns_list))}
                final_dict_list.append(row_dict)
        
            return final_dict_list
        else:
            print("資料遺失或空白 DataFrame")
            return {}
    except Exception as e:
        print(f"發生錯誤: {str(e)}")
        return {}
     

class StockData(BaseModel):
    date:str=Field(alias="日期")
    trading_volume:str=Field(alias="成交股數")
    turnover:str=Field(alias="成交金額")
    open_price:float=Field(alias="開盤價")
    high_price:float=Field(alias="最高價")
    low_price:float=Field(alias="最低價")
    close_price:float=Field(alias="收盤價")
    change:float=Field(alias="漲跌價差")
    transactions:str=Field(alias="成交筆數")

class Data(RootModel):
    root:list[StockData]


def Rsi(df):

    return 0




def main():
    month_num=6
    stock_id=1101
    month_datas:pd.DataFrame=Get_N_Month_Data(month_num=month_num,stock_id=stock_id)
    data_list:list=Get_Data_Dict(month_datas)
    data:Data=Data.model_validate(data_list)
    stock_datas:list[dict]=data.model_dump()
    print(stock_datas)


if __name__ =="__main__":
    main()