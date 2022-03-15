from multiprocessing import context
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.urls import reverse
from .models import Job
from .forms import AppyForm, JobForm
from django.contrib.auth.decorators import login_required
from .list_filter import JobFilter
# Create your views here.
def job_list(request):
    jobs = Job.objects.all()
    
    # Filtter
    # https://github.com/carltongibson/django-filter
    myfilter = JobFilter(request.GET, queryset=jobs)
    jobs = myfilter.qs
    # pagination
    # # https://docs.djangoproject.com/fr/4.0/topics/pagination/  
    paginator = Paginator(jobs, 3) # Show 1 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context ={'jobs':page_obj, 'myfilter':myfilter}
    return render(request, 'job/job_list.html',context)


def job_detail(request, slug):
    jobs_detail = Job.objects.get(slug=slug)
    
    if request.method == 'POST':
        form = AppyForm(request.POST,request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = jobs_detail 
            myform.save()
            print('Done')
    
    else:
        form = AppyForm()
    context = {'jobs_detail': jobs_detail, 'form': form}
    return render(request,'job/job_detail.html',context )

@login_required
def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user 
            myform.save()
            return redirect(reverse('jobs:job_list'))
        
    else:
        form = JobForm()
        context ={'form':form}
    return render(request, 'job/add_job.html',context)