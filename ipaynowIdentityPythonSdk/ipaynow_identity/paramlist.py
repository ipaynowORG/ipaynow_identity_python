#!/usr/bin/env python
# -*- coding: utf-8; mode: python; tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 4 -*- vim:fenc=utf-8:ft=python:et:sw=4:ts=4:sts=4

# define interface parameter attributes and max len

# key name 'name' indicates parameter name
# key name 'must' indicates parameter
# 身份认证
ID01_PostList = [
    {'name': 'funcode', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 4, 'desp': "功能码"},
    {'name': 'appId', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 40, 'desp': "商户应用唯一标识"},
    {'name': 'mhtOrderNo', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 40, 'desp': "商户订单号"},
    {'name': 'idcard', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 64, 'desp': "身份证号"},
    {'name': 'cardName', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 1000, 'desp': "姓名"}
]

# 银行卡认证
ID02_PostList = [
    {'name': 'funcode', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 4, 'desp': "功能码"},
    {'name': 'appId', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 40, 'desp': "商户应用唯一标识"},
    {'name': 'mhtOrderNo', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 40, 'desp': "商户订单号"},
    {'name': 'idCard', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 64, 'desp': "身份证号"},
    {'name': 'idCardName', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 1000, 'desp': "姓名"},
    {'name': 'bankCardNum', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 1000, 'desp': "银行账户"},
    {'name': 'certiType', 'mandatory': 'N', 'md5': 'Y', 'type': 'str', 'len': 64, 'desp': "证件类型"},
    {'name': 'mobile', 'mandatory': 'N', 'md5': 'Y', 'type': 'str', 'len': 1000, 'desp': "手机号"}
]

# 手机号认证
ID03_PostList = [
    {'name': 'funcode', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 4, 'desp': "功能码"},
    {'name': 'appId', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 40, 'desp': "商户应用唯一标识"},
    {'name': 'mhtOrderNo', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 40, 'desp': "商户订单号"},
    {'name': 'idCard', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 64, 'desp': "身份证号"},
    {'name': 'idCardName', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 1000, 'desp': "姓名"},
    {'name': 'certiType', 'mandatory': 'N', 'md5': 'Y', 'type': 'str', 'len': 64, 'desp': "证件类型"},
    {'name': 'mobile', 'mandatory': 'N', 'md5': 'Y', 'type': 'str', 'len': 1000, 'desp': "手机号"}
]

# 查询接口
QUERY_PostList = [
    {'name': 'funcode', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 10, 'desp': "功能码"},
    {'name': 'appId', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 40, 'desp': "商户应用唯一标识"},
    {'name': 'mhtOrderNo', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 40, 'desp': "订单号"},
    {'name': 'mchSign', 'mandatory': 'N', 'md5': 'N', 'type': 'str', 'len': 32, 'desp': "商户签名"}
]
