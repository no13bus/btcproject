## 部署时候注意的问题
- supervisord.conf文件要配置好。(gunicorn+nginx运行django）
- 还有就是端口转发。linux里面叫default。这是为了区分这个文件名字叫nginx_default
- 在控制台输入python manage.py collectstatic，此命令的作用是将所有需转发的文件拷入static文件夹
重启nginx，sudo /etc/init.d/nginx restart

- bitfinex的相同的key和secret只能允许在一个程序里面。不能运行在多个程序里面。否则会报错:`none is to small`.
`最最重要的一点`：为了测试，本地会运行程序，但是主要不要进行自动交易，否则开发环境和部署环境都在进行自动交易，增加了同一个时间点上对api的请求数量（小心被封） 还有就是同一时间多次分析价格和交易 没有必要。容易混淆。

## 部署前需要安装的libs:
- `sudo apt-get install python-mysqldb`
- `pip install celery`
- `pip install celery[redis]`
- `pip install gunicorn`
- `pip install gevent`
- `sudo apt-get install redis-server`
- `ssh-keygen -t rsa -C "no13bus@gmail.com"`
- `pip install django==1.6.5`
- `pip install django-celery`
- `pip install south`
- `pip install requests`
- `pip install tornado==3.2`
- `pip install flower`
- `pip install redis`
- `pip install mailer`
当然你也可以使用 pip install -r requirement.txt来将python库一起安装