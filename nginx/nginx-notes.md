>nginx -h
nginx version: nginx/1.4.2
Usage: nginx [-?hvVtq] [-s signal] [-c filename] [-p prefix] [-g directives]

Options:
  -?,-h         : this help
  -v            : show version and exit
  -V            : show version and configure options then exit
  -t            : test configuration and exit
  -q            : suppress non-error messages during configuration testing
  -s signal     : send signal to a master process: stop, quit, reopen, reload
  -p prefix     : set prefix path (default: /usr/local/Cellar/nginx/1.4.2/)
  -c filename   : set configuration file (default: /usr/local/etc/nginx/nginx.conf)
  -g directives : set global directives out of configuration file


  266  git add notes/nginx-notes.txt
  326  cd nginx_workspace/
  333  which nginx
  602  which nginx
  603  cat /usr/local/etc/nginx/nginx.conf
  604  nginx --help
  605  nginx -h
  607  nginx -c nginx/nginx.conf -p nginx/
  609  nginx -c /Users/hongzhihua/Documents/workspace/others_workspace/raspberry-pi/nginx/nginx.conf -p /Users/hongzhihua/Documents/workspace/others_workspace/raspberry-pi/nginx/
  610  nginx -V
  611  sudo nginx -c /Users/hongzhihua/Documents/workspace/others_workspace/raspberry-pi/nginx/nginx.conf -p /Users/hongzhihua/Documents/workspace/others_workspace/raspberry-pi/nginx/
  623  brew upgrade nginx
  624   nginx -c /Users/hongzhihua/Documents/workspace/others_workspace/raspberry-pi/nginx/nginx.conf -p /Users/hongzhihua/Documents/workspace/others_workspace/raspberry-pi/nginx/
  625  ps -ef | grep nginx
  627  nginx -h
  628  nginx -s reload
  642  nginx -V
  644  nginx -s reload
  645  ps -ef | grep nginx
  652  nginx -h
  653  nginx -s reload
  655  nginx -s reload
  669  ps -ef | grep nginx
  700  history | grep nginx




  开机启动
  简单认证
