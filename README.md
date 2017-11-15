# 鉴权SDK python 版本使用说明 #

## 版本变更记录 ##

- 1.0.0 : 初稿


## 目录 ##

[1. 概述](#1)

&nbsp;&nbsp;&nbsp;&nbsp;[1.1 简介](#1.1)

&nbsp;&nbsp;&nbsp;&nbsp;[1.2 如何获取](#1.2)

[2. API](#2)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[身份验证](#2.1)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[身份验证-订单查询](#2.2)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[卡信息认证](#2.3)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[卡信息认证-订单查询](#2.4)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[手机号认证](#2.5)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[手机号认证-订单查询](#2.6)

[3.应用秘钥获取](#3)

[4. DEMO ](#4)

<h2 id='1'> 1. 概述 </h2>

<h4 id='1.1'> 1.1 简介 </h4>

- 鉴权SDK。

<h4 id='1.2'> 1.2 如何获取 </h4>

[获取源码](https://github.com/ipaynowORG/ipaynow_identity_python.git)


<h2 id='2'> 2. API </h2>


<h4 id='2.1'> 2.1 身份验证</h4>

    '''
        身份认证
        appId 商户应用ID
        appKey 应用秘钥
        desKey des秘钥
        mhtOrderNo 商户订单号
        idcard 待认证身份证号
        cardName 待认证姓名
    '''
    def toCheckID(appId, appKey, desKey, mhtOrderNo, idcard, cardName)

- 返回参数中的值的含义

<table>
        <tr>
            <th>名称</th>
            <th>说明</th>
        </tr>
<tr>
            <td>funcode</td>
            <td>同输入</td>
         </tr>
<tr>
<tr>
            <td>nowpayTransId</td>
            <td>xxxx</td>
         </tr>
<tr>
            <td>responseTime</td>
            <td>yyyyMMddHHmmss</td>
         </tr>
<tr>
            <td>responseCode</td>
            <td>0000 成功
                0001 参数信息有误
                0002 获取商户信息失败
                0003 获取商户费率失败
                0004 获取商户可用条数失败
                0005 商户资金不足
                0006 验证异常
                0007 商户订单号重复
            </td>
         </tr>
<tr>
            <td>responseMsg</td>
            <td>应答信息</td>
         </tr>
<tr>
            <td>status</td>
            <td>00匹配,01不匹配,02未知,03调用错误</td>
         </tr>
<tr>
            <td>mhtOrderNo</td>
            <td>同输入或SDK自动生成的订单号</td>
         </tr>
    </table>



<h4 id='2.2'> 2.2 身份验证-订单查询</h4>

        ''' 
         身份认证查询   
         appId 商户应用Id 
         appKey 商户应用秘钥
         mhtOrderNo 订单号
        '''
        
        
        def queryCheckID(appId, appKey, desKey, mhtOrderNo)

- 返回参数中的值的含义

<table>
        <tr>
            <th>名称</th>
            <th>说明</th>
        </tr>
<tr>
            <td>appId</td>
            <td>同输入</td>
         </tr>
<tr>
            <td>funcode</td>
            <td>同输入</td>
         </tr>
<tr>
            <td>responseTime</td>
            <td>yyyyMMddHHmmss</td>
         </tr>
<tr>
            <td>responseCode</td>
            <td>0000 成功
                0001 参数信息有误
                0002 获取商户信息失败
                0003 获取商户费率失败
                0004 获取商户可用条数失败
                0005 商户资金不足
                0006 验证异常
                0007 商户订单号重复
            </td>
         </tr>
<tr>
            <td>responseMsg</td>
            <td>应答信息</td>
         </tr>
<tr>
            <td>status</td>
            <td>00匹配,01不匹配,02未知,03调用错误</td>
         </tr>
<tr>
            <td>transStatus</td>
            <td>00成功  01失败</td>
         </tr>
<tr>
            <td>mhtOrderNo</td>
            <td>同输入或SDK自动生成的订单号</td>
         </tr>
    </table>

<h4 id='2.3'> 2.3 卡信息认证</h4>

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
        
        
        def toCheckCard(appId, appKey, desKey, mhtOrderNo, idcard, cardName, certiType, bankCardNum, mobile)

- 返回参数中的值的含义

<table>
        <tr>
            <th>名称</th>
            <th>说明</th>
        </tr>
<tr>
            <td>funcode</td>
            <td>同输入</td>
         </tr>
<tr>
            <td>responseTime</td>
            <td>yyyyMMddHHmmss</td>
         </tr>
<tr>
            <td>responseCode</td>
            <td>0000 成功
                0001 参数信息有误
                0002 获取商户信息失败
                0003 获取商户费率失败
                0004 获取商户可用条数失败
                0005 商户资金不足
                0006 验证异常
                0007 商户订单号重复
            </td>
         </tr>
<tr>
            <td>nowpayTransId</td>
            <td>现在支付流水号</td>
         </tr>
<tr>
            <td>requestId</td>
            <td>现在支付流水号</td>
         </tr>
<tr>
            <td>status</td>
            <td>00匹配,01不匹配,02未知,03调用错误</td>
         </tr>
<tr>
            <td>transStatus</td>
            <td>00成功  01失败</td>
         </tr>
<tr>
            <td>mhtOrderNo</td>
            <td>同输入或SDK自动生成的订单号</td>
         </tr>
    </table>

<h4 id='2.4'> 2.4 卡信息认证-订单查询</h4>

        ''' 
         银行卡认证查询   
         appId 商户应用Id 
         appKey 商户应用秘钥
         mhtOrderNo 订单号
        '''
        
        
        def queryCheckCard(appId, appKey, desKey, mhtOrderNo)      
        

- 返回参数中的值的含义

<table>
        <tr>
            <th>名称</th>
            <th>说明</th>
        </tr>
<tr>
            <td>appId</td>
            <td>同输入</td>
         </tr>
<tr>
            <td>funcode</td>
            <td>同输入</td>
         </tr>
<tr>
            <td>responseTime</td>
            <td>yyyyMMddHHmmss</td>
         </tr>
<tr>
            <td>responseCode</td>
            <td>0000 认证信息匹配
                0001 认证信息不匹配
                0002 参数为空或不合法
                0003 获取商户信息失败
                0004 获取商户费率失败
                0005 获取商户可用条数失败
                0006 商户资金不足
                0007 商户订单号重复
                0008 验证异常
                0009 身份证名字转码错误
                0010 银行卡可是错误或银行卡规则未配置
                0011 银行卡不支持
                0012 未获取到可用渠道
            </td>
         </tr>
<tr>
            <td>responseMsg</td>
            <td>应答信息</td>
         </tr>
<tr>
            <td>status</td>
            <td>00一致,01验证信息未通过/认证失败/密码错误/无效卡号/此卡已过期/未开通此功能/银行卡与证件不符/银行卡与姓名不符/请求要素不合法/响应吗设置异常/不支持该银行验证
            02,请求银行超时 03,解密失败/核对md5值异常/核对md5值不通过/报文解析异常/解析银行返回报文失败/商户不存在/其他错误</td>
         </tr>
<tr>
            <td>transStatus</td>
            <td>00成功,01失败</td>
         </tr>
<tr>
            <td>mhtOrderNo</td>
            <td>同输入或SDK自动生成的订单号</td>
         </tr>
    </table>        



<h4 id='2.5'> 2.5 手机号认证</h4>

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
        def toCheckMobileNo(appId, appKey, desKey, mhtOrderNo, idcard, cardName, certiType, mobile)    
        
- 返回参数中的值的含义

<table>
        <tr>
            <th>名称</th>
            <th>说明</th>
        </tr>
<tr>
            <td>funcode</td>
            <td>同输入</td>
         </tr>
<tr>
            <td>responseTime</td>
            <td>yyyyMMddHHmmss</td>
         </tr>
<tr>
            <td>responseCode</td>
            <td>0000 成功
                0001 参数信息错误
                0002 获取商户信息失败
                0003 获取商户费率失败
                0004 获取商户可用条数失败
                0005 商户资金不足
                0006 验证异常
                0007 商户订单号重复
            </td>
         </tr>
<tr>
            <td>responseMsg</td>
            <td>应答信息</td>
         </tr>
<tr>
            <td>nowpayTransId</td>
            <td>现在支付流水号</td>
         </tr>
<tr>
            <td>requestId</td>
            <td>现在支付流水号</td>
         </tr>
<tr>
            <td>status</td>
            <td>00匹配,01不匹配,02状态未知 03调用错误</td>
         </tr>
<tr>
            <td>mhtOrderNo</td>
            <td>同输入或SDK自动生成的订单号</td>
         </tr>
    </table>
        

<h4 id='2.6'> 2.6 手机号认证-订单查询</h4>


    ''' 
    手机号认证查询   
     appId 商户应用Id 
     appKey 商户应用秘钥
     mhtOrderNo 订单号
    '''
    
    
    def queryCheckMobileNo(appId, appKey, desKey, mhtOrderNo)       
        
- 返回参数中的值的含义

<table>
        <tr>
            <th>名称</th>
            <th>说明</th>
        </tr>
<tr>
            <td>appId</td>
            <td>同输入</td>
         </tr>
<tr>
            <td>funcode</td>
            <td>同输入</td>
         </tr>
<tr>
            <td>responseTime</td>
            <td>yyyyMMddHHmmss</td>
         </tr>
<tr>
            <td>responseCode</td>
            <td>0000 成功
                0001 参数信息错误
                0002 订单不存在
            </td>
         </tr>
<tr>
            <td>responseMsg</td>
            <td>应答信息</td>
         </tr>
<tr>
            <td>status</td>
            <td>00匹配,01不匹配,02状态未知 03调用错误</td>
         </tr>
<tr>
            <td>transStatus</td>
            <td>00成功,01失败</td>
         </tr>
<tr>
            <td>mhtOrderNo</td>
            <td>同输入或SDK自动生成的订单号</td>
         </tr>
    </table>        

<h2 id='3'> 3. 应用秘钥获取 </h2>

```
#appId(应用ID)和md5(appKey),登录商户后台 : https://mch.ipaynow.cn ->商户中心->应用信息可以新增应用或查看appKey
appId=xxxxxxxxx
md5=xxxxxxxxxx
#需要在运营后台-鉴权服务管理 中为商户进行配置
des=xxxxxxxx
```        

<h2 id='4'> 4. DEMO </h2>

     使用方法:
   
   您可以从 GitHub 上下载 Python SDK 的源代码：
   
    git clone https://github.com/ipaynowORG/ipaynow_identity_python.git

    1.cd 进入ipaynowIdentityPythonSdk文件夹
    2.执行 "python setup.py install"
    3.在代码中 import ipaynow
     参考示例代码
     示例代码
     cd 进入example文件夹
     运行 python tradeTest.py 

    messageTest.py

