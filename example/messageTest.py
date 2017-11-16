#!/usr/bin/env python
# -*- coding: utf-8; mode: python; tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 4 -*- vim:fenc=utf-8:ft=python:et:sw=4:ts=4:sts=4
from ipaynowIdentityPythonSdk.ipaynow_identity.authService import toCheckID, queryCheckID, toCheckCard, queryCheckCard, \
    toCheckMobileNo, queryCheckMobileNo

print(toCheckID("xxxxxxxxxxxxxxxx","xxxxxxxxxxxxxxxx","xxxxxxxxxxxxxxxxx","pyhtonCheckId1","xxxxxxxxxxxxxxxxxxxxxx","xxxxxxxxxxxxxx",isTest=False))

#身份认证查询
# print(queryCheckID("xxxxxxxxxxxxxxxxxxx","xxxxxxxxxxxxxxxxxxxxx","xxxxxxxxxxxxxxxxxxxxxxxxx","xxxxxxxxxxxxxxxxx",isTest=False))

# print(toCheckCard("xxxxxxxxxxxxx","xxxxxxxxxxxxxxxxxxxx","xxxxxxxxxxxxxxxxxxxx","pythonCardbeijin3","xxxxxxxxxxxxxxxxxxxxxxxxx","xxx","01","dddddd","xxxxx",isTest=False))

# print(queryCheckCard("xxxxxxxxxxxxxxxxx","xxxxxxxxxxxxxxxxx","xxxxxxxxxxxxxxxx","pythonCardbeijin0",isTest=False))

# print(toCheckMobileNo("xxxxxxxxxxxxxxxxx","xxxxxxxxxxxxxxxxxxx","xxxxxxxxxxxxxxxxxxxxxxx","pythonCardbeijin3","xxxxxxxxxxxxxxxxxxxxxxxx","xxx","01","xxxxxxxxxxxxx",isTest=False))

# print(queryCheckMobileNo("xxxxxxxxxxxxxxxxxxxxx","xxxxxxxxxxxxxxxxxx","xxxxxxxxxxxxxxxxxxx","pythonCardbeijin3",isTest=False))
