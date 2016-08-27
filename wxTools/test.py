#coding:utf-8
from wxTools import wxTools

testappid='wxbf844f771df2017d'
testappsecret='d4624c36b6795d1d99dcf0547af5443d'
ss=wxTools(testappid,testappsecret)
token=ss.getTokenFromWX()
print token
print ss.getIP(token)
group={'group':{'name':'test'}}
# print ss.createGroup(token,group)
print ss.getAllGroups(token)