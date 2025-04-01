import json
# 修改导入语句，确保从模块中导入类
from hk_stock_data import HKStockData
from us_stock_data import USStockData  # 确保这是从模块导入类而不是模块本身
from jinja2 import Environment, FileSystemLoader
import os
import time

def main():
    try:
        # 港股代码
        hk_codes = ["hk00700", "hk09988", "hk03690"]
        
        # 美股代码 (从产品要求美股.txt读取)
        us_codes = ["AAPL", "MSFT", "GOOGL"]
        
        # 修改这里 - 不再需要传递API Key
        hk_data = HKStockData()
        # 确保是这样调用的
        us_data = USStockData()  # 正确：实例化类
        # 而不是这样：
        # us_data = USStockData  # 错误：这只是引用模块/类，没有实例化
        
        # 获取港股数据...
        stock_data = {}
        
        # 逐个请求股票数据
        for code in hk_codes:
            single_stock_data = hk_data.get_single_stock_data(code)
            if single_stock_data:
                stock_data[code] = single_stock_data

        # 添加港股数据输出
        print("\n港股实时行情数据:")
        print("="*40)
        for code in hk_codes:
            if code in stock_data:
                info = stock_data[code]
                print(f"{info['name']}({code})")
                print(f"当前价格: {info['price']}")
                print(f"涨跌幅: {info['change_percent']}%")
                print(f"状态: {info['status']}")
            else:                                                                                                                                                                                                                                                                                                                                               
                print(f"未获取到股票 {code} 的数据")
            print("-"*40)

        # 获取美股数据
        us_stock_data = {}
        for code in us_codes:
            stock_info = us_data.get_single_stock_data(code)
            if stock_info:
                us_stock_data[code] = stock_info
            # Alpha Vantage免费版限制5次/分钟
            
        
        # 输出美股数据
        print("\n美股实时行情数据:")
        print("="*40)
        for code in us_codes:
            if code in us_stock_data:
                info = us_stock_data[code]
                print(f"{info['symbol']}")
                print(f"当前价格: {info['price']}")
                print(f"涨跌幅: {info['change_percent']}%")
                print(f"状态: {info['status']}")
            else:
                print(f"未获取到股票 {code} 的数据")
            print("-"*40)
            
        # 准备模板环境
        env = Environment(loader=FileSystemLoader('templates'))
        template = env.get_template('stock_report.html')

        # 准备模板数据
        template_data = {
            'hk_stocks': [
                {
                    'code': code,
                    'name': info['name'],
                    'price': info['price'],
                    'change_percent': info['change_percent'],
                    'status': info['status']
                }
                for code, info in stock_data.items()
            ],
            'us_stocks': [
                {
                    'symbol': code,
                    'price': info['price'],
                    'change_percent': info['change_percent'],
                    'status': info['status']
                }
                for code, info in us_stock_data.items()
            ]
        }

        # 渲染模板并保存到文件
        output_html = template.render(template_data)
        with open('stock_report.html', 'w', encoding='utf-8') as f:
            f.write(output_html)

        print("股票报告已生成到 stock_report.html 文件")

    except Exception as e:
        print(f"程序运行出错: {e}")

if __name__ == "__main__":
    # 确保模板目录存在
    os.makedirs('templates', exist_ok=True)
    main()