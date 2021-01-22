from django.shortcuts import render
from bloodapp.models import Contact
from bloodapp.models import Donor
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        address = request.POST['address']
        email = request.POST['email']
        phone = request.POST['phone']
        if len(name)<2 or len(email)<3 or len(address)< 10 or len(phone)<10 :
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(name=name, email=email, phone=phone, address=address)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')

def donor(request):
    if request.method == "POST":
        name = request.POST['name']
        gender = request.POST['gender']
        dob = request.POST['dob']
        bloodgroup = request.POST['bloodgroup']
        if len(name)<2 :
            messages.error(request, "Please fill the form correctly")
        else:
            donor=Donor(name=name, gender=gender, dob=dob, bloodgroup=bloodgroup)
            donor.save()
            messages.success(request, "Your message has been successfully sent")

    return render(request, 'home/donor.html')

def search(request):
    query=request.GET['query']
    if len(query)>78 or len(query) == 0:
        allPosts=Donor.objects.none()
    else:
        allPostsName= Donor.objects.filter(name__icontains=query)
        allPostsBloodgroup= Donor.objects.filter(bloodgroup__iexact=query)
        allPostsGender =Donor.objects.filter(gender__iexact=query)
        allPosts=  allPostsName.union(allPostsBloodgroup, allPostsGender)
    if allPosts.count() == 0:
        messages.warning(request, "No search results found. Please refine your query.")
    params={'allPosts': allPosts, 'query': query}
    return render(request, 'home/search.html', params)