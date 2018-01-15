from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView

from blog.models import Post
from tagging.models import Tag, TaggedItem
from tagging.views import TaggedObjectList

from django.views.generic.edit import FormView
from blog.forms import PostSearchForm
from django.db.models import Q
from django.shortcuts import render

# -- TemplateView
class TagTV(TemplateView):
    template_name = 'tagging/tagging_cloud.html'


# -- ListView
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'  # default: post_list.html
    context_object_name = 'posts'  # 템플릿 파일로 넘겨주는 객체 리스트에 대한 변수명
    paginate_by = 2  # 한 페이지에 보여주는 객체 리스트의 숫자


class PostTOL(TaggedObjectList):
    model = Post
    template_name = 'tagging/tagging_post_list.html'


# -- DetailView
class PostDV(DetailView):
    model = Post


# -- ArchiveView
class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_date'


class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_date'
    make_object_list = True  # 해당 연도에 해당하는 객체의 리스트를 만들어서 템플릿에 넘겨준다


class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_date'


class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_date'


class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_date'


# --FormView
class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'blog/post_search.html'

    def form_valid(self, form):
        sch_word = '%s' % self.request.POST['search_word']
        post_list = Post.objects.filter(Q(title__icontains=sch_word) | Q(description__icontains=sch_word) |
                                        Q(content__icontains=sch_word)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = sch_word
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)  # No Redirection