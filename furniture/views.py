from django.shortcuts import render
from django.views import generic
from .models import Post
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse

class PostList(generic.ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'projects'

    def get_queryset(self):
        queryset = {'kitchens':Post.objects.filter(project_type='kitchen', status=1).order_by('-created_on')[:6],
                    'furniture':Post.objects.filter(project_type='furniture', status=1).order_by('-created_on')[:6]
                    }

        return queryset


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'page.html'


def FormHandler(request):
    name = request.POST["name"]
    email = request.POST["email"]
    message = request.POST["message"]
    receiverEmail = 'mshaklev@gmail.com'

    # convert user input to html
    HTMLmessage = convert_to_html(name, email, message)

    # send the html message to the specified receiver email
    send_mail(
        f"Client message",
        'Client message',
        'noreplytothis377@gmail.com',
        [f"{receiverEmail}"],
        fail_silently=False,
        html_message=HTMLmessage,
        )

    return HttpResponseRedirect(reverse('home'))


def Kitchens(request):
    kitchens = Post.objects.filter(project_type='kitchen', status=1)

    return render(request,"kitchen_projects.html", {"kitchens":kitchens})


def Furniture(request):
    furniture = Post.objects.filter(project_type='furniture', status=1)

    return render(request, "furniture_projects.html", {"furniture":furniture})


# helper function which creates html message
def convert_to_html(name, email, message):
    html = f"""\
    <html>
        <body>
            <ul>
                <li><strong>Name:</strong>{name}</li>
                <li><strong>Email:</strong><a href="mailto:{email}">{email}</a></li>
                <li><strong>Message:</strong>{message}</li>
            </ul>
        </body>
    </html>
    """

    return html
