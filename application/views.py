from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from .forms import ApplicationForm
from .models import Application


class ApplicationListView(LoginRequiredMixin, ListView):
    model = Application
    template_name = 'applications/home.html'
    extra_context = {
        'title': 'Home'
    }

    def get_queryset(self):
        return Application.objects.filter(
            student_id=self.request.user
        ).order_by('-dateApplication')


class ApplicationDetailView(LoginRequiredMixin, DetailView):
    model = Application
    template_name = 'applications/details.html'
    context_object_name = 'application'


class ApplicationCreateView(LoginRequiredMixin, CreateView):
    model = Application
    form_class = ApplicationForm
    template_name = 'applications/create_form.html'
    extra_context = {
        'title': 'Create Application'
    }

    def form_valid(self, form):
        form.instance.student_id = self.request.user.id
        return super(ApplicationCreateView, self).form_valid(form)


def about(req):
    return render(req, "applications/about.html", {'title': 'About'})
