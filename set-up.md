## 声音
### 选择声音输出方式
树莓派的声音可以通过HDMI或者耳机口输出。
输出方式默认是自动选择。也可以手动选择，比如，

	>amixer cset numid=3 1

`numid=3`是card control的编号，可以通过`amixer controls`查看。
最后的数字`1`表示通过耳机输出，`2`表示通过HDMI输出，`0`表示自动。

参考资料[1][1]。

### 调整音量
TODO


## 网络
### 为树莓派设置静态ip
可以在路由器的配置页面为树莓派的网卡及无线网卡设置静态的ip地址，方便以后ssh登录树莓派时不用经常切换ip。
只需要在配置页面里为网卡的MAC地址配置一个静态ip就可以。
网卡的MAC地址一般可以在路由器的已连接设备列表里找到。
静态ip的设置可能不会马上生效，因为分配的动态ip不会马上失效。


### 设置无线网卡
[EDUP EP-N8508GS][2]无线网卡在树莓派下无需额外的驱动。

确认USB网卡正常工作。

	# list USB devices
	>lsusb

上面的命令会列出所有USB设备，包括插入的USB网卡。

	# like ifconfig, but dedicated for wireless interface
	# see more by 'man iwconfig'
	>iwconfig

如果无线网卡工作正常，上面的命令会输出`wlan0`信息。

扫描可用的wifi信号，找到想要连接的wifi信号的SSID。

	# see more by 'man iwlist'
	>iwlist wlan0 scan

生成psk，

	# pre-computes PSK entries for network configuration blocks of a wpa_supplicant.conf file
	>wpa_passphrase ssid wifi-password

把生成的psk信息存到wifi客户端（`wpa_supplicant`）的配置文件（`wpa_supplicant.conf`）里，

	# Wi-Fi Protected Access client and IEEE 802.1X supplicant
	>man wpa_supplicant
	# configuration file for wpa_supplicant
	>man wpa_supplicant.conf

编辑`ifup/ifdown`的配置文件`/etc/network/interfaces`（详见`man /etc/network/interfaces`）。        
如果无线网卡的ip是自动获得的，添加类似于下面的配置信息，

	allow-hotplug wlan0  
	auto wlan0  
	iface wlan0 inet dhcp  
	pre-up wpa_supplicant -B w -D wext -i wlan0 -c /etc/wpa_supplicant/wpa_supplicant.conf  
	post-down killall -q wpa_supplicant  

如果是固定ip，添加类似于下面的配置信息，

	allow-hotplug wlan0  
	auto wlan0  
	iface wlan0 inet static  
	  address 192.168.1.137  
	  netmask 255.255.255.0  
	  network 192.168.1.0  
	  broadcast 192.168.1.255  
	  gateway 192.168.1.1  
	wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf  

启动wifi连接，

	>sudo ifup wlan0

如果想关闭wifi链接，

	>sudo ifdown wlan0

参考文章见[这里][1]。


[1]: http://blog.csdn.net/bailyzheng/article/details/33336709 "set up usb wifi card"
[2]: http://item.jd.com/509932.html "EDUP EP-N8508GS"
[3]: https://www.raspberrypi.org/documentation/configuration/audio-config.md "audio config"
[5]: http://blog.scphillips.com/posts/2013/01/sound-configuration-on-raspberry-pi-with-alsa/ "audio config"







