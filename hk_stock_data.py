import requests
from datetime import datetime, time

class HKStockData:
    def __init__(self):
        self.base_url = "http://qt.gtimg.cn/q="
        
    def get_stock_data(self, stock_codes):
        url = self.base_url + ",".join(stock_codes)
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            response.encoding = 'gbk'
            
            data = response.text.split(";")
            result = {}
            for item in data:
                if not item.strip():
                    continue
                parts = item.split("~")
                if len(parts) > 30:
                    code = item.split("=")[0].replace("v_", "")
                    result[code] = {
                        "name": parts[1],
                        "price": parts[3],
                        "change_percent": parts[5],
                        "status": "交易中" if self._is_trading_time() else "已收盘"
                    }
            return result
        except Exception as e:
            print(f"获取数据失败: {str(e)}")
            return {}

    def _is_trading_time(self):
        now = datetime.now().time()
        return ((time(9, 30) <= now <= time(12, 0)) or 
                (time(13, 0) <= now <= time(16, 0)))

    def get_single_stock_data(self, stock_code):
        try:
            url = self.base_url + stock_code
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            response.encoding = 'gbk'
            
            data = response.text.split(";")
            for item in data:
                if not item.strip():
                    continue
                parts = item.split("~")
                if len(parts) > 43:  # 确保有足够字段
                    code = item.split("=")[0].replace("v_", "")
                    return {
                        "name": parts[1],
                        "price": parts[3],  # 当前价格
                        "change_percent": parts[43],  # 涨跌幅(百分比)使用第43个字段
                        "status": "交易中" if self._is_trading_time() else "已收盘"
                    }
            return None
        except Exception as e:
            print(f"获取港股 {stock_code} 数据失败: {str(e)}")
            return None