# 计算圈复杂度的api接口

## 开发环境准备
	# pip install -r requirement.txt
	# mv package/dist/my-languages.so .

### 启动flask服务
    # python myflask.py
	
### 调用方式
    method: post
    Content-Type:application/json
    body: {"code": "代码块"}
    测试脚本
    # python mytest.py

## 返回值
    json格式
    {
     "cyclic": 15
    }

###库说明
    package下的cyclicmy文件夹内的为库的源代码
    使用时需要依赖package/dist/my-languages.so
    