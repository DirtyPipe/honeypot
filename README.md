# honeypot
web蜜罐
该蜜罐主要用于捕捉web扫描器的攻击，
包含主流Server头和主流首页特征

使用方法：

`python3 index.py`

使用tcpdump抓包
`tcpdump -i eth0 -w all.pcap`

如果需要后台可以使用nohup进行
