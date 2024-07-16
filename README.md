# 阿里云域名解析Certbot证书续期

> 该脚本使用阿里云SDK，查询"_acme-challenge"域名记录是否存在，存在时更新记录，否则添加一条类型为"TXT"主机记录为"_acme-challenge"的记录

1、获取阿里云 AccessKey：您需要从阿里云控制台获取 AccessKey ID 和 AccessKey Secret，这些是调用阿里云 API 所需的凭证

2、安装阿里云 SDK：在您的服务器上安装阿里云 Python SDK，以便您的脚本可以使用它来与阿里云 DNS 服务进行交互。您可以使用 pip3 来安装所需的 SDK 包：

  ```bash
  pip3 install alibabacloud_alidns20150109
  pip3 install alibabacloud_tea_openapi
  pip3 install alibabacloud_tea_util
  ```

3、下载hook.py到服务器

```bash
wget https://github.com/CloudyLtd/certbot-alidns-hook/blob/main/hook.py
```

4、运行续期命令

```bash
certbot renew --manual-auth-hook /you/path/hook.py
```
