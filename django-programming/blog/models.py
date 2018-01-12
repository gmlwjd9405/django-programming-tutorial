from django.db import models
from django.urls import reverse  # URL 패턴을 만들어주는 장고의 내장 함수


# Create your models here.
class Post(models.Model):
    title = models.CharField('TITLE', max_length=50)
    # 기본키 대신 사용. allow_unicode: 한글 사용 가능.
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text.')
    content = models.TextField('CONTENT')
    create_date = models.DateField('Create Date', auto_now_add=True)
    modify_date = models.DateField('Modify Date', auto_now=True)

    # 필드 속성 외에 필요한 파라미터가 있으면 Meta 내부 클래스로 정의
    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = "my_post"  # default = "blog_post"
        ordering = ('-modify_date',)  # modify_date 컬럼을 기준으로 내림차순으로 정렬

    def __str__(self):
        return self.title

    # 해당 객체를 지칭하는 URL을 반환
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.slug,))

    def get_previous_post(self):
        return self.get_previous_by_modify_date()

    def get_next_post(self):
        return self.get_next_by_modify_date()