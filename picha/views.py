from django.shortcuts import render, redirect, get_object_or_404

from django.template.loader import render_to_string

from django.http import JsonResponse

from picha.models import Picture
from picha.forms import PictureForm


def home(request):
    images = Picture.objects.all()
    return render(request, "picha/home.html", {'images': images})


def add_picture(request):

    data = {}
    
    form = PictureForm()
    
    if request.method == "POST":
       
        form = PictureForm(request.POST, request.FILES)
        
        if form.is_valid():
        
            form.save()
            
            data['form_is_valid'] = True
            
            return JsonResponse(data)
            
        else:
            
            data['form_is_valid'] = False
            
            data['picture_form'] = render_to_string("picha/picture_form.html", {'form': form}, request=request )
      
    data['picture_form'] = render_to_string("picha/picture_form.html", {'form': form}, request=request )
    
    return JsonResponse(data)
    
    


def edit_picture(request, id):

    data = {}

    image = get_object_or_404(Picture, pk=id)
    
    form = PictureForm(instance=image)
    
    if request.method == "POST":
    
        form = PictureForm(request.POST, request.FILES, instance=image)
        
        if form.is_valid():
        
            form.save()
            
            data['form_is_valid'] = True
            
            return JsonResponse(data)
            
        else:
        
            data['form_is_valid'] = False
            
            data['edit_picture'] = render_to_string("picha/edit_picture.html", {'form': form}, request=request )
                 
            
    data['edit_picture'] = render_to_string("picha/edit_picture.html", {'form': form}, request=request )
    
    return JsonResponse(data)
    
    
    
    
    
    
