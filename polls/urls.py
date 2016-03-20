from django.conf.urls import url

from polls import views

# url规则命名空间配置, 可以在模板中使用 {% url 'app_name:url_name' url_parameters %},来反向组装url
app_name = 'polls'

# url规则配置
urlpatterns = [
    # 参数1:正则匹配规则, 参数2:回调方法, 参数3: 本规则的名称
    url(r'^$', views.index, name="index"),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name="detail"),
    url(r'^(?P<question_id>[0-9]+)/result/$', views.result, name="result"),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name="vote"),
]