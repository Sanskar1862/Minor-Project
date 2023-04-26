from django.shortcuts import render,HttpResponse,redirect
from django.shortcuts import render
from .forms import ImageForm
from .models import Image
# Create your views here.

def lessor(request):
 if request.method == "POST":
  form = ImageForm(request.POST, request.FILES)
  if form.is_valid():
   form.save()
 form = ImageForm()
 img = Image.objects.all()
 return render(request, 'lessor.html', {'img':img, 'form':form})
# Create your views here.

def rent(request):
    return render(request,'rent.html')

