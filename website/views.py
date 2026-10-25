from django.shortcuts import render, redirect
from .forms import ContactMessageForm

def home(request):
    return render(request, "website/home.html")


def services(request):
    return render(request, "website/services.html")


def about(request):
    return render(request, "website/about.html")



def contact(request):
    if request.method == "POST":
        form = ContactMessageForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("website:contact_success")
    else:
        form = ContactMessageForm()

    return render(
        request,
        "website/contact.html",
        {"form": form},
    )


def contact_success(request):
    return render(request, "website/contact_success.html")

