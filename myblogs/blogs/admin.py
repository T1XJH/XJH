from django.contrib import admin
from .models import MyblogInfo, Img

# Register your models here.

@admin.register(MyblogInfo)
class Myblog_infoAdmin(admin.ModelAdmin):
    def titles(self):
        return self.title
    titles.short_description = u'标题'
    def image_data(self):
        path = "http://127.0.0.1:8000/static/all/uploadimg/" + self.imgname
        return path
    image_data.short_description = u'图片地址'
    def description(self):
        return self.descriptions
    description.short_description = u'内容'

    # 列表属性
    list_display = ['id', titles, description, image_data, 'time']
    list_filter = ['title']  # 过滤器
    search_fields = ['title']  # 搜索字段
    list_per_page = 50

    fieldsets = [
        ("主要内容", {"fields": ['title', 'descriptions']}),
        ("其他", {"fields": ['imgname', 'uploadimg', 'time']}),
    ]  # 分组

    # 执行动作的位置
    actions_on_bottom = True
    actions_on_top = False

from django.utils.safestring import mark_safe
@admin.register(Img)
class ProductAdmin(admin.ModelAdmin):

    readonly_fields = ('image_data', 'imgname')  #必须加这行 否则访问编辑页面会报错
    def image_data(self):
        path = "http://127.0.0.1:8000/static/test/img/" + self.imgname
        return mark_safe(u'< img src="%s" width="100px" />' % path)

    list_display = ('id', image_data)
    # 页面显示的字段名称
    image_data.short_description = u'品牌图片'


