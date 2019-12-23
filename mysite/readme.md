## 依赖：

* django
* django-cors-headers
* apscheduler==2.1.2
---

### Nginx+Uwsgi+Django部署到阿里云遇到的问题

* CentOS7.3系统成功，Ubuntu的apt-get下载总是报错
* Nginx下载钱依赖先安装好，包括openssl，zlib等，配置文件在/etc/nginx/nginx.conf
* Uwsgi不要用yum或者apt下载，用python的pip最好，yum下载的会少很多文件，虽然uwsgi命令能成功，但是连uwsgi --http都会报错
* pip下载好需要把uwsgi软连接到/usr/sbin，且把anaconda环境下的3个libxxxxx.so文件复制到/lib64下
* 还需将anaconda下高版本的CXXABI复制到/lib64下进行软连接，参考https://www.cnblogs.com/shanguanghui/p/8994919.html
