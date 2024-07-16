#!/usr/bin/env python
# coding=utf-8
import logging
import os
import traceback

from alibabacloud_alidns20150109 import models as alidns_20150109_models
from alibabacloud_alidns20150109.client import Client as AliDns20150109Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util import models as util_models

ACCESS_KEY_ID = '你的阿里云访问钥匙（access key）'
ACCESS_KEY_SECRET = '你的阿里云访问钥匙密码（access key secret）'

# 域名，certbot设置的变量
DOMAIN_NAME = os.environ['CERTBOT_DOMAIN']
# 校验值，certbot设置的变量
VALUE = os.environ['CERTBOT_VALIDATION']
# 主机记录
RR = '_acme-challenge'

logging.basicConfig(filename='/var/log/letsencrypt/hook.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def create_client() -> AliDns20150109Client:
    """
    使用AK&SK初始化账号Client
    @return: Client
    @throws Exception
    """
    config = open_api_models.Config(
        access_key_id=ACCESS_KEY_ID,
        access_key_secret=ACCESS_KEY_SECRET
    )
    # Endpoint 请参考 https://api.aliyun.com/product/Alidns
    config.endpoint = f'alidns.cn-hangzhou.aliyuncs.com'
    return AliDns20150109Client(config)


client = create_client()


def find_records():
    """
    查询域名记录
    :return: 记录详情
    """
    describe_domain_records_request = alidns_20150109_models.DescribeDomainRecordsRequest(
        domain_name=DOMAIN_NAME,
        key_word=RR
    )
    runtime = util_models.RuntimeOptions()
    try:
        response = client.describe_domain_records_with_options(describe_domain_records_request, runtime)
        return response.body.domain_records.record
    except Exception as error:
        logging.error(f'{DOMAIN_NAME}记录获取异常 {error} {traceback.format_exc()}')


def add_txt_record():
    """
    添加域名记录
    """
    add_domain_record_request = alidns_20150109_models.AddDomainRecordRequest(
        domain_name=DOMAIN_NAME,
        rr=RR,
        type='TXT',
        value=VALUE
    )
    runtime = util_models.RuntimeOptions()
    try:
        client.add_domain_record_with_options(add_domain_record_request, runtime)
    except Exception as error:
        logging.error(f'{DOMAIN_NAME}记录添加异常{error} {traceback.format_exc()}')


def update_txt_record(record_id):
    """
    修改域名记录
    :param record_id: 记录编号
    """
    update_domain_record_request = alidns_20150109_models.UpdateDomainRecordRequest(
        record_id=record_id,
        rr=RR,
        type='TXT',
        value=VALUE
    )
    runtime = util_models.RuntimeOptions()
    try:
        client.update_domain_record_with_options(update_domain_record_request, runtime)
    except Exception as error:
        logging.error(f'{DOMAIN_NAME}记录修改异常 {error} {traceback.format_exc()}')


# 主逻辑
if __name__ == '__main__':
    records = find_records()
    if records:
        record_id = records[0].record_id
        update_txt_record(record_id)
    else:
        add_txt_record()
