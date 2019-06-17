from django.http import  HttpResponse
from django.shortcuts import render

def home(request):
    return  render(request,'home.html')

def count(request):
    #获取前端文本框内容
    text = request.GET['text']

    res = {}
    for  i in text:
        if  i not in res:
            res[i] = 1
        else:
            res[i] += 1


    res = sorted(res.items(), key=lambda x:x[1],reverse=True)
    #返回渲染的html
    # request参数;用于生成此响应的请求对象
    # template_name:要使用的模板的全名或模板名称的序列
    # context:要添加到模板上下文的值的字典
    # content_type:用于结果文档的mime类型默认为：设置:setting:DEFAULT_CONTENT_TYPE 设置的值。
    # status：响应的状态代码默认为“200”
    # using：用于加载模板的模板引擎的 :setting:`NAME `
    return render(request,'count.html',{'count_result':res})