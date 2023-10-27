# **SubDomainScan**

子域名爆破

## **简介**

本子域名爆破工具采用多线程化优化效率，将扫描任务多线程化，每个线程扫描一个子域名，同时使用“threading.Lock()”确保“result”列表的安全访问

## 使用

使用说明

![image-20231027193501044](C:\Users\luo\AppData\Roaming\Typora\typora-user-images\image-20231027193501044.png)

-h  帮助文档

-u “url”   目标url

-f "filename"   字典的路径

-t [1,10]   扫描威胁系数 1最低 10最高

扫描启动

```
python SubDomainScan.py -u "qq.com" -f "subdomains_top100.txt" -t 5
```

测试案例

![image-20231027193748755](C:\Users\luo\AppData\Roaming\Typora\typora-user-images\image-20231027193748755.png)