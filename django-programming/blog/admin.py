from django.contrib import admin
from blog.models import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'modify_date')
    # modify_date를 화면에 출력하라고 지정
    list_filter = ('modify_date',)
    # 검색박스를 표시하고, 입력된 단어는 title과 content 컬럼에서 검색하도록 한다.
    search_fields = ('title', 'content')
    # slug 필드는 title 필드를 사용해 미리 채워지도록 한다
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)