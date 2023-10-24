from django.shortcuts import redirect, render
from .models import Food,Consume
# Create your views here.

def index(request):
    
    if request.method == "POST":
        
        food_consumed = request.POST.get('food_consumed')
        consume = Food.objects.get(name=food_consumed)
        user = request.user
        consumes = Consume(user=user,food_consumed=consume)
        consumes.save()
    
    
    
    foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user)
    
    return render(request,'myapp/index.html',{'foods':foods,'consumed_food':consumed_food})

def delete_consume(request,id):
    consumed_food = Consume.objects.get(id=id)
    if request.method == "POST":
        consumed_food.delete()
        return redirect('/')   

    return render(request,'myapp/delete.html')
         

