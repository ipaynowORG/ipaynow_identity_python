import base64
import urllib
from ipaynowIdentityPythonSdk.ipaynow_identity import interface
from ipaynowIdentityPythonSdk.ipaynow_identity.desUtil import desDecrypt, md5Encrypt
from pip._vendor import requests
from ipaynowIdentityPythonSdk.ipaynow_identity.error import APIInputError

url = "https://dby.ipaynow.cn/identify"  # 测试

'''
手机号认证
appId 商户应用Id
md5Key 商户应用秘钥
desKey 商户3desKey
mhtOrderNo 商户订单号
idcard 身份证号
idCardName 姓名
certiType 证件类型
bankCardNum 银行账户
mobile 预留手机号
'''
def toCheckMobileNo(appId, appKey, desKey, mhtOrderNo, idcard, cardName, certiType, mobile):
    paypara = {
        'funcode': "ID03",
        'appId': appId,
        'mhtOrderNo': mhtOrderNo,
        'idCard': idcard,
        'idCardName': cardName,
        'mobile': mobile
    }
    if len(certiType) > 0:
        paypara['certiType'] = certiType
    messageStr = ""
    try:
        messageStr = interface.getCheckMobileNoStr(appKey, desKey, paypara)
        messageStr = "funcode=ID03" + "&message=" + messageStr
    except APIInputError as ipse:
        print(ipse)
    except Exception as e:
        print(e)
        print(e.with_traceback)
    resp = requests.post(url, messageStr)
    result = urllib.parse.unquote(resp.text)
    return1 = result.split("|")[0];
    if return1 == "0":
        return "fail"
    return2 = result.split("|")[1];
    return3 = base64.b64decode(result.split("|")[2]);
    originalMsg = desDecrypt(desKey, return2.strip())
    sign = md5Encrypt(originalMsg + "&" + appKey)
    if str(return3, encoding="UTF-8") == sign:
        return originalMsg
    return "verfiy sign fail"


''' 
手机号认证查询   
 appId 商户应用Id 
 appKey 商户应用秘钥
 mhtOrderNo 订单号
'''


def queryCheckMobileNo(appId, appKey, desKey, mhtOrderNo):
    return query("ID03_Query", appId, appKey, desKey, mhtOrderNo);


'''
银行卡认证(同一账号验证失败后需等24小时后再次验证)
appId 商户应用Id
md5Key 商户应用秘钥
desKey 商户3desKey
mhtOrderNo 商户订单号
idcard 身份证号
idCardName 姓名
certiType 证件类型
bankCardNum 银行账户
mobile 预留手机号
'''


def toCheckCard(appId, appKey, desKey, mhtOrderNo, idcard, cardName, certiType, bankCardNum, mobile):
    paypara = {
        'funcode': "ID02",
        'appId': appId,
        'mhtOrderNo': mhtOrderNo,
        'idCard': idcard,
        'idCardName': cardName,
        'bankCardNum': bankCardNum
    }
    if len(certiType) > 0:
        paypara['certiType'] = certiType
    if len(mobile) > 0:
        paypara["mobile"] = mobile
    messageStr = ""
    try:
        messageStr = interface.getCheckCardStr(appKey, desKey, paypara)
        messageStr = "funcode=ID02" + "&message=" + messageStr
    except APIInputError as ipse:
        print(ipse)
    except Exception as e:
        print(e)
        print(e.with_traceback)
    resp = requests.post(url, messageStr)
    result = urllib.parse.unquote(resp.text)
    return1 = result.split("|")[0];
    if return1 == "0":
        return "fail"
    return2 = result.split("|")[1];
    return3 = base64.b64decode(result.split("|")[2]);
    originalMsg = desDecrypt(desKey, return2.strip())
    sign = md5Encrypt(originalMsg + "&" + appKey)
    if str(return3, encoding="UTF-8") == sign:
        return originalMsg
    return "verfiy sign fail"


''' 
 银行卡认证查询   
 appId 商户应用Id 
 appKey 商户应用秘钥
 mhtOrderNo 订单号
'''


def queryCheckCard(appId, appKey, desKey, mhtOrderNo):
    return query("ID02_Query", appId, appKey, desKey, mhtOrderNo);


'''
    身份认证
    appId 商户应用ID
    appKey 应用秘钥
    desKey des秘钥
    mhtOrderNo 商户订单号
    idcard 待认证身份证号
    cardName 待认证姓名
'''
def toCheckID(appId, appKey, desKey, mhtOrderNo, idcard, cardName):
    paypara = {
        'funcode': "ID01",
        'appId': appId,
        'mhtOrderNo': mhtOrderNo,
        'idcard': idcard,
        'cardName': cardName,
    }
    messageStr = ""
    try:
        messageStr = interface.getCheckIDStr(appKey, desKey, paypara)
        messageStr = "funcode=ID01" + "&message=" + messageStr
    except APIInputError as ipse:
        print(ipse)
    except Exception as e:
        print(e)
        print(e.with_traceback)
    resp = requests.post(url, messageStr)
    result = urllib.parse.unquote(resp.text)
    return1 = result.split("|")[0];
    if return1 == "0":
        return "fail"
    return2 = result.split("|")[1];
    return3 = base64.b64decode(result.split("|")[2]);
    originalMsg = desDecrypt(desKey, return2.strip())
    sign = md5Encrypt(originalMsg + "&" + appKey)
    if str(return3, encoding="UTF-8") == sign:
        return originalMsg
    return "verfiy sign fail"


''' 
 身份认证查询   
 appId 商户应用Id 
 appKey 商户应用秘钥
 mhtOrderNo 订单号
'''


def queryCheckID(appId, appKey, desKey, mhtOrderNo):
    return query("ID01_Query", appId, appKey, desKey, mhtOrderNo);


def query(funcode, appId, appKey, desKey, mhtOrderNo):
    paypara = {
        'funcode': funcode,
        'appId': appId,
        'mhtOrderNo': mhtOrderNo,
    }
    messageStr = ""
    try:
        messageStr = interface.query(appKey, desKey, paypara)
        messageStr = "funcode=" + funcode + "&message=" + messageStr
    except APIInputError as ipse:
        print(ipse)
    except Exception as e:
        print(e)
        print(e.with_traceback)
    resp = requests.post(url, messageStr)
    result = urllib.parse.unquote(resp.text)
    return1 = result.split("|")[0];
    if return1 == "0":
        return "fail"
    return2 = result.split("|")[1];
    return3 = base64.b64decode(result.split("|")[2]);
    originalMsg = desDecrypt(desKey, return2.strip())
    sign = md5Encrypt(originalMsg + "&" + appKey)
    if str(return3, encoding="UTF-8") == sign:
        return originalMsg
    return "verfiy sign fail"
