#coding:utf-8
import urllib,urllib2
import json


#########################################################
class wxTools():
    def __init__(self,id,secret):
        self.appid=id
        self.appsecret=secret
    def getTokenFromWX(self):
        result=urllib2.urlopen("https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s"%((self.appid,self.appsecret))).read()
        token=json.loads(result)['access_token']
        return token;
    #获取IP
    def getIP(self,token):
        return urllib2.urlopen('https://api.weixin.qq.com/cgi-bin/getcallbackip?access_token=%s'%token).read()
    #创建分组
    #入参：token，字典类型group
    #返回创建结果及分组ID
    def createGroup(self,token,group):
        groupdata=json.dumps(group)
        result=urllib2.urlopen('https://api.weixin.qq.com/cgi-bin/groups/create?access_token=%s'%token,groupdata).read()
        return result
    #查询所有分组
    #返回json格式分组列表
    def getAllGroups(self,token):
        return urllib2.urlopen('https://api.weixin.qq.com/cgi-bin/groups/get?access_token=%s'%token).read()

    #根据openid查询用户所在分组
    #入参 token，字典openid
    #返回值：成功：返回分组ID；失败：返回失败原因
    def getGroupByopenid(self,token,openid):
        openiddata=json.dumps(openid)
        result=json.loads(urllib2.urlopen('https://api.weixin.qq.com/cgi-bin/groups/getid?access_token=%s'%token,openiddata).read())
        try:
            return result['groupid']
        except:
            return result['errmsg']

    #修改分组名称
    #入参：token；包含分组信息的字典和名字,一次仅能修改一条 {"group":{"id":108,"name":"test2_modify2"}}
    #返回结果代码，0代表成功，其他代表失败
    def changeGroupName(self,token,groupname):
        result=json.loads(urllib2.urlopen("https://api.weixin.qq.com/cgi-bin/groups/update?access_token=%s"%token,json.dumps(groupname)).read())
        return result['errcode']

    #移动用户分组,可批量或单条
    # 入参：token；包含分组信息的字典,修改单条参数：{"openid":"oDF3iYx0ro3_7jD4HFRDfrjdCM58","to_groupid":108}；
    # 修改多条：{"openid_list":["oDF3iYx0ro3_7jD4HFRDfrjdCM58","oDF3iY9FGSSRHom3B-0w5j4jlEyY"],"to_groupid":108}
    # 返回结果代码，0代表成功，其他代表失败
    def moveUserGroup(self,token,usergroup):
        if usergroup.has_key("openid_list"):
            result = json.loads(urllib2.urlopen("https://api.weixin.qq.com/cgi-bin/groups/members/batchupdate?access_token=%s" % token,
                                json.dumps(usergroup)).read())
        else:
            result=json.loads(urllib2.urlopen("https://api.weixin.qq.com/cgi-bin/groups/members/update?access_token=%s"%token,json.dumps(usergroup)).read())
        return result['errcode']

    #删除分组
    #入参token，group信息{"group":{"id":108}}
    # 返回结果代码，0代表成功，其他代表失败
    def deleteGroup(self,token,group):
        result = json.loads(urllib2.urlopen("https://api.weixin.qq.com/cgi-bin/groups/update?access_token=%s" % token,
                                            json.dumps(group)).read())
        return result['errcode']

    #根据openid获取unionid
    #入参，token
    def getUnionID(self,token,openid,lang='zh-CN'):
        result=json.loads(urllib2.urlopen('https://api.weixin.qq.com/cgi-bin/user/info?access_token=%s&openid=%s&lang=%s'%(token,openid,lang)).read())
        return result

    #批量获取




    ##############################仅认证服务号可用的功能##################################

    #修改用户备注名称
    #入参：POST数据格式：{"openid":"oDF3iY9ffA-hqb2vVvbr7qxf6A0Q","remark":"pangzi"}
    def setRemark(self,token,userremark):
        result = json.loads(urllib2.urlopen("https://api.weixin.qq.com/cgi-bin/user/info/updateremark?access_token=%s" % token,
                                            json.dumps(userremark)).read())

        return result['errcode']