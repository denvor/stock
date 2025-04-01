# Stock 项目安装说明（阿里云Linux服务器）
1. 从GitHub拉取项目代码
git clone https://github.com/denvor/stock.git /path/to/webroot/stock
cd /path/to/webroot/stock

2. 创建并激活虚拟环境
python3 -m venv venv
source venv/bin/activate  # Linux/

3 安装项目依赖
pip install -r requirements.txt

4. 设置定时任务（可选）
编辑 crontab 文件，添加以下内容：
crontab -e
# 每隔5分钟运行一次
*/5 * * * * /path/to/webroot/stock/venv/bin/python /path/to/webroot/stock/stock.py >> /path/to/webroot/stock/cron.log 2>&1




