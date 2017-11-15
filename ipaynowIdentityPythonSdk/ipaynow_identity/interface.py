#!/usr/bin/env python
# -*- coding: utf-8; mode: python; tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 4 -*- vim:fenc=utf-8:ft=python:et:sw=4:ts=4:sts=4
from ipaynowIdentityPythonSdk.ipaynow_identity.packMsg import PackMsgSend
from ipaynowIdentityPythonSdk.ipaynow_identity.paramlist import ID01_PostList, QUERY_PostList, ID02_PostList, \
    ID03_PostList


def getCheckMobileNoStr(appKey, desKey, payparam={}):
    pms = PackMsgSend(payparam["appId"], appKey, desKey, payparam, ID03_PostList)
    return pms.getResultString()


def getCheckCardStr(appKey, desKey, payparam={}):
    pms = PackMsgSend(payparam["appId"], appKey, desKey, payparam, ID02_PostList)
    return pms.getResultString()


def getCheckIDStr(appKey, desKey, payparam={}):
    pms = PackMsgSend(payparam["appId"], appKey, desKey, payparam, ID01_PostList)
    return pms.getResultString()


def query(appKey, desKey, queryparam={}):
    pms = PackMsgSend(queryparam["appId"], appKey, desKey, queryparam, QUERY_PostList)
    return pms.getResultString()


def parseMessage(instr=""):
    print(instr)
    return instr


def parseQuery(instr=""):
    print(instr)
    return instr
