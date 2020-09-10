# honeypot
web蜜罐
该蜜罐主要用于捕捉web扫描器的攻击，
包含主流Server头和主流首页特征
增加了日志功能，记录在txt里面。具体格式还有待考量

使用方法：

`python3 index.py 80`

端口转发，将21-65535端口的流量转发到80端口

`iptables -t nat -A PREROUTING -p tcp --dport 81:65535 -j REDIRECT --to-port 80`

使用tcpdump抓包，6小时保存一个文件并且排除22端口

`tcpdump -i eth0 -G 21600 -w %Y_%m%d_%H%M_%S.pcap -q -n -nn not port 22`

如果需要后台可以使用nohup进行
