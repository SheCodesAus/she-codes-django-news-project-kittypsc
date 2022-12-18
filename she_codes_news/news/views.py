from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm

user = get_user_model

class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        # auth_id = self.kwargs['auth_id']
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:3]
        context['all_stories'] = NewsStory.objects.all().order_by('-pub_date') [:3]
        # context['author_stories'] = NewsStory.objects.filter()
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'
   
# def get_queryset(self):
#     return super().get_queryset()

   

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class StoryEditView(LoginRequiredMixin, generic.UpdateView):
    model = NewsStory
    fields = ['title', 'pub_date', 'content']

    def get_success_url(self) -> str:
        return reverse_lazy('news:story', kwargs={'pk':self.kwargs['pk']})

    def get_queryset(self):
        qs = super().get_queryset()
        # if not self.request.user.is_authenticated:
        #     raise qs.model.DoesNotExist
        # qs = qs.filter(author=self.request.user)
        return qs.filter(author=self.request.user)

# class StoryDeleteView(generic.DeleteView):
#     model = NewsStory
#     success_url = reverse_lazy('news:index')

