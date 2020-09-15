from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from .models import Application


class ApplicationListView(ListView):
    model = Application
    template_name = 'applications/home.html'
    extra_context = {
        'title': 'Home'
    }

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return super(ApplicationListView, self).get(*args, **kwargs)
        else:
            return redirect('/login/')

    def get_queryset(self):
        return Application.objects.filter(student_id=self.request.user)


class ApplicationDetailView(DetailView):
    model = Application
    template_name = 'applications/details.html'
    context_object_name = 'application'


def about(req):
    return render(req, "applications/about.html", {'title': 'About'})
