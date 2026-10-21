from django.shortcuts import render, redirect, get_object_or_404
from .forms import JobApplicationForm
from .models import JobApplication
from django.views.decorators.http import require_POST 
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
       
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = JobApplicationForm()

    job_applications = JobApplication.objects.all()
    
    application_status = request.GET.get('status','') 
    if application_status:
        job_applications = JobApplication.objects.filter(status=application_status) 


    return render(request, 'applications/home.html',
                  {
                      'job_applications': job_applications,
                      'form':form,
                      'application_status': application_status,
                  }
                  )

def edit_application(request, application_id):
    application_to_edit = get_object_or_404(JobApplication, id = application_id)
    
    if request.method == "POST":
        form = JobApplicationForm(request.POST, instance=application_to_edit)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = JobApplicationForm(instance = application_to_edit)

    job_applications = JobApplication.objects.all()
    
    return render(request, 'applications/edit.html', {
        'job_applications': job_applications,
        'form':form
    })

@require_POST
def delete_application(request, application_id):
    application = get_object_or_404(JobApplication, id = application_id)
    application.delete()
    return redirect('home')
