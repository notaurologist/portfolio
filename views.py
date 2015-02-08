from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from models import Site
from forms import ContactForm

def index(request):
    site_list = Site.objects.filter(hidden=False).order_by('sort_order')
    paginator = Paginator(site_list, 3)
    
    # Make sure page request is an int. If not, deliver first page.
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # If page request (9999) is out of range, deliver last page of results.
    try:
        sites = paginator.page(page)
    except (EmptyPage, InvalidPage):
        sites = paginator.page(paginator.num_pages)
    
    # Handle form submit
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data.get('email', 'noreply@jasonlemoine.com')
            message = form.cleaned_data['message']
            try:
                send_mail(
                    'Feedback from JasonLeMoine.com',
                    message, email,
                    ['xxxxx']
                )
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/')
    else:
        form = ContactForm()
    return render_to_response('base.html', {'form': form, 'sites': sites})
