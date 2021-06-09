from django.shortcuts import render
from django.utils.translation import activate
from django.http import Http404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from proxima.utils.mail import send_mail
from .models import *
from .forms import ResumeForm

def index(request):
    try:
        page = MainPage.objects.latest('id')
        contacts = Contacts.objects.latest('id')
    except:
        page = ''
        contacts = ''
    return render(request, 'index.html', { 'page' : page, 'contacts' : contacts })

def about(request):
    try:
        page = About.objects.latest('id')
    except:
        page = ''
    return render(request, 'pages/about.html', { 'page' : page })

def team(request):
    try:
        page = Team.objects.latest('id')
    except:
        page = ''
    return render(request, 'pages/team.html', { 'page' : page })

def career(request):
    try:
        page = Career.objects.latest('id')
    except:
        page = ''
    return render(request, 'pages/career.html', { 'page' : page })

def actives(request):
    try:
        page = Actives.objects.latest('id')
    except:
        page = ''
    active_projects = Project.objects.filter(is_active=True, is_end=False)
    ended_projects = Project.objects.filter(is_active=True, is_end=True)
    return render(request, 'pages/invest.html', { 'page' : page, 'act_projects' : active_projects, 'end_projects' : ended_projects })

def person(request, name):
    try:
        page = Person.objects.get(slug=name)
    except:
        raise Http404
    return render(request, 'pages/person.html', { 'page' : page })

def docs(request):
    try:
        page = Documentation.objects.latest('id')
    except:
        page = ''
    return render(request, 'pages/docs.html', { 'page' : page })

def expertise(request):
    try:
        page = Expertise.objects.latest('id')
    except:
        page = ''
    directions = ActionDirection.objects.all()
    return render(request, 'pages/expertise.html',{ 'page' : page, 'directions' : directions })

def expertise_page(request, id):
    try:
        page = ActionDirection.objects.get(id=id)
        page_title = Expertise.objects.latest('id').title
    except:
        raise Http404
    return render(request, 'pages/ex_page.html', { 'page' : page, 'title': page_title })

def active(request, id):
    try:
        page = Project.objects.get(slug=id)
    except:
        raise Http404
    return render(request, 'pages/active.html', { 'page' : page })

def news(request):
    try:
        page = NewsPage.objects.latest('id')
    except:
        page = ''
    news = News.objects.all()
    news_length = News.objects.filter(category='n').count()
    act_length = News.objects.filter(category='a').count()
    return render(request, 'pages/news.html',{ 'page' : page, 'news' : news, 'news_length' : news_length, 'act_length' : act_length })

def new(request, id):
    try:
        page = News.objects.get(id=id)
        page_title = NewsPage.objects.latest('id').title
    except:
        raise Http404
    news = News.objects.all()[:4]
    return render(request, 'pages/new.html', { 'page' : page, 'title' : page_title, 'news' : news })

def projects(request):
    try:
        page = ProjectPage.objects.latest('id')
    except:
        page = ''
    projects  = Project.objects.all()
    directions = ActionDirection.objects.filter(project__in=projects).distinct()
    industries = Industry.objects.filter(project__in=projects).distinct()
    active_length = Project.objects.filter(is_active=True).count()
    return render(request, 'pages/projects.html', { 'page' : page, 'directions' : directions, 'industries' : industries, 'active_length' : active_length, 'projects' : projects })

def contacts(request):
    try:
        page = Contacts.objects.latest('id')
    except:
        page = ''
    return render(request, 'pages/contacts.html', {'page' : page})

def consulting(request):
    return render(request, 'pages/consulting.html')

@csrf_exempt
@require_POST
def send_resume(request):
    form = ResumeForm(request.POST, request.FILES)
    print(request.POST)

    if form.is_valid():
        form.save()
        send_mail('mail/resume.html', {
            'resume': form.cleaned_data
        })
        return JsonResponse({'result' : 'ok'})
    else:
        print(form.errors)
        return JsonResponse({'error' : form.errors})

@csrf_exempt
@require_POST
def filter_projects(request):
    if request.POST['data']:
        data = request.POST['data']
        directions = request.POST['directions'] or 'all'
        industries = request.POST['industries'] or 'all'
        language = request.POST['language'] or 'ru'

        activate(language)

        actions_kwargs = {}
        actions_title_arg = 'actions__title_%s' % language
        actions_kwargs[actions_title_arg] = directions

        industries_kwargs = {}
        industries_title_arg = 'industries__title_%s' % language
        industries_kwargs[industries_title_arg] = industries

        result = Project.objects.filter(is_active=False)

        if directions != 'all':
            result = result.filter(**actions_kwargs)
        if industries != 'all':
            result = result.filter(**industries_kwargs)

        filter_direction = []
        filter_industry = []
        for p in result:
            filter_direction.append(p.actions.all())
            filter_industry.append(p.industries.all())
        filter_direction = list(set([item for sublist in filter_direction for item in sublist]))
        filter_industry = list(set([item for sublist in filter_industry for item in sublist]))

        return render(request, 'items/items_projects.html', { 'items' : result, 'filter_direction' : filter_direction, 'filter_industry' : filter_industry })
    else:
        return JsonResponse({'error' : True})


@csrf_exempt
@require_POST
def filter_news(request):
    if request.POST['data']:
        data = request.POST['data']
        result = []
        if data == 'all':
            result = News.objects.all()
        else:
            result = News.objects.filter(category=data)
        return render(request, 'items/items_news.html', { 'items' : result })
    else:
        return JsonResponse({'error' : True})

def search(request):
    if request.GET['type'] and request.GET['search']:
        type = request.GET['type']
        search = request.GET['search']
        items = []
        if type == 'projects':
            items = Project.objects.filter(title__icontains=search)
            page = ProjectPage.objects.latest('id')
        if type == 'news':
            items = News.objects.filter(title__icontains=search)
            page = NewsPage.objects.latest('id')
    return render(request, 'pages/search.html', { 'items' : items, 'search' : search, 'page' : page, 'type' : type })
