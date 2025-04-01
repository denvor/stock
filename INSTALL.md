# Stock 项目安装说明（阿里云Linux服务器）
1. 上传项目代码
上传 stock.zip 到 阿里云的 web服务器根目录/path/to/webroot，解压为 /path/to/webroot/stock

2. 创建并激活虚拟环境
cd /path/to/webroot/stock
python3 -m venv venv
source venv/bin/activate  # Linux/

3 安装项目依赖
pip install -r requirements.txt

4. 设置定时任务（可选）
编辑 crontab 文件，添加以下内容：
crontab -e
# 每隔5分钟运行一次
*/5 * * * * /path/to/webroot/stock/venv/bin/python /path/to/webroot/stock/stock.py >> /path/to/webroot/stock/cron.log 2>&1




