# 阿里云域名解析Certbot证书续期

1、获取阿里云 AccessKey：您需要从阿里云控制台获取 AccessKey ID 和 AccessKey Secret，这些是调用阿里云 API 所需的凭证

2、安装阿里云 SDK：在您的服务器上安装阿里云 Python SDK，以便您的脚本可以使用它来与阿里云 DNS 服务进行交互。您可以使用 pip3 来安装所需的 SDK 包：

  ```bash
  pip3 install aliyun-python-sdk-core
  pip3 install aliyun-python-sdk-alidns
  ```

3、下载hook.py到服务器

```bash
wget 
```

4、运行续期命令

```bash
certbot renew --manual-auth-hook /you/path/hook.py
```
