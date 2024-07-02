import requests
import datetime as dt
import pandas as pd
from dateutil.relativedelta import relativedelta
import numpy as np

from pydantic import BaseModel, Field
from typing import List

class StockData(BaseModel):
    date: str = Field(alias="日期")
    trading_volume: str = Field(alias="成交股數")
    turnover: str = Field(alias="成交金額")
    open_price: float = Field(alias="開盤價")
    high_price: float = Field(alias="最高價")
    low_price: float = Field(alias="最低價")
    close_price: float = Field(alias="收盤價")
    change: float = Field(alias="漲跌價差")
    transactions: str = Field(alias="成交筆數")

class Data(BaseModel):
    root: List[StockData]

  
    def check_empty_data(cls, values):
        if not values['root']:
            raise ValueError("Data is empty")
        return values

def Get_N_Month_Data(month_num: int, stock_id: int) -> pd.DataFrame:
    date_now = dt.datetime.now()
    date_list = [(date_now - relativedelta(months=i)).replace(day=1).strftime('%Y%m%d') for i in range(month_num)]
    date_list.reverse()

    all_data = []

    for date in date_list:
        url = f'https://www.twse.com.tw/rwd/zh/afterTrading/STOCK_DAY?date={date}&stockNo={stock_id}'
        try:
            json_data = requests.get(url).json()
            df = pd.DataFrame(data=json_data['data'], columns=json_data['fields'])
            all_data.append(df)
        except Exception as e:
            print(f"無法取得{date}的資料, 可能資料量不足.")

    if all_data:
        final_df = pd.concat(all_data, ignore_index=True)
    else:
        final_df = pd.DataFrame()

    return final_df

def Get_Data_Dict(data: pd.DataFrame) -> List[dict]:
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
            return []
    except Exception as e:
        print(f"發生錯誤: {str(e)}")
        return []

def calculate_bollinger_bands(data: pd.DataFrame, window=20, num_std=2):
    # 計算收盤價的移動平均線和標準差
    data['MA'] = data['收盤價'].rolling(window=window).mean()

    data['std_dev'] = data['收盤價'].rolling(window=window).std()

    # 計算布林通道的上限線和下限線
    data['UpperBand'] = data['MA'] + num_std * data['std_dev']
    data['LowerBand'] = data['MA'] - num_std * data['std_dev']

    return data

def main():
    month_num = 6
    stock_id = 1101

    # 取得股票數據
    month_datas = Get_N_Month_Data(month_num, stock_id)

    if not month_datas.empty:
        # 計算布林通道
        month_datas['收盤價'] = month_datas['收盤價'].astype(float)  # 確保收盤價的數據類型是 float
        bollinger_data = calculate_bollinger_bands(month_datas)
        
        # 打印結果
        print(bollinger_data[['日期', '收盤價', 'MA', 'UpperBand', 'LowerBand']])
    else:
        print("無法獲取股票數據，請檢查是否有足夠的數據。")

if __name__ == "__main__":
    main()
