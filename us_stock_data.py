import requests
from datetime import datetime, time
import pytz

class USStockData:
    def __init__(self):
        self.base_url = "http://push2.eastmoney.com/api/qt/stock/get"
    
    def get_single_stock_data(self, stock_code):
        try:
            params = {
                'ut': '7eea3edcaed734bea9cbfc24409ed989',
                'fltt': '2',
                'invt': '2',
                'fields': 'f43,f57,f58,f169,f170',
                'secid': f'105.{stock_code}',
                '_': str(int(datetime.now().timestamp() * 1000))
            }
            
            headers = {
                'User-Agent': 'Mozilla/5.0',
                'Referer': 'http://quote.eastmoney.com'
            }
            
            response = requests.get(self.base_url, params=params, headers=headers, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if not data.get('data'):
                return None
                
            stock_data = data['data']
            return {
                "symbol": stock_code,
                "price": stock_data['f43'],
                "change_percent": f"{stock_data['f170']}",  # 确保添加百分号
                "status": "交易中" if self._is_trading_time() else "已收盘"
            }
            
        except Exception as e:
            print(f"获取美股 {stock_code} 数据失败: {str(e)}")
            return None

    def _is_trading_time(self):
        """检查当前是否是美股交易时间(美东时间)"""
        tz = pytz.timezone('America/New_York')
        now = datetime.now(tz)  # 获取带时区的当前时间
        current_time = now.time()  # 获取时间部分
        trading_start = time(9, 30)  # 交易开始时间
        trading_end = time(16, 0)   # 交易结束时间
        return trading_start <= current_time <= trading_end