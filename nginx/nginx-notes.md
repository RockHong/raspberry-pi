## 命令

    sudo nginx -p /home/pi/workspace/raspberry-pi/nginx -c nginx.conf -t  

因为目录权限的问题（比如log目录），需要以`sudo`来启动，
启动时会把nginx进程的用户切换成配置文件中指定的用户。
`-p`指定去哪个目录找配置文件。
`-t`，启动前先测试一下。

	sudo nginx -s reload

重新载入配置文件。要以运行nginx的用户来执行。
（TODO：以root还是以配置文件中指定的用户，比如www-data？）


## 开机启动
TODO

