import tushare as ts
ts.set_token("15c29753625614d25a5aeddcbf444818b741a1d38693c23bdd8bdc99")
pro = ts.pro_api()

# 添加API基础信息检查
print("=== API基础信息 ===")
print(f"API状态: {'可用' if pro.query('api') else '不可用'}")

# 尝试获取股票基本信息
basic_info = pro.stock_basic(ts_code="00700.HK")
print("\n=== 股票基本信息 ===")
print(basic_info)

# 尝试获取日线数据（添加日期参数）
df = pro.daily(
    ts_code="00700.HK",
    trade_date="20231115"  # 使用具体日期测试
)
print("\n=== 日线数据 ===")
print(df)