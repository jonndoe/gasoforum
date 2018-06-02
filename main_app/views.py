# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from . models import GasTheme
from . models import GasTopic
from . models import PhotoAlbum
from . models import Photo
from . models import GasThemeText
from . models import GasTopicText
from . models import GasThemeComment
from . models import GasThemeCommentReply
from . models import GasTopicComment
from . forms import GasThemeForm
from . forms import GasTopicForm
from . forms import GasThemeTextForm
from . forms import GasTopicTextForm
from . forms import PhotoAlbumForm
from . forms import PhotoForm
from . forms import GasThemeCommentForm
from . forms import GasThemeCommentReplyForm
from . forms import GasTopicCommentForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    gastopics = GasTopic.objects.order_by('date_added')
    gastopics = gastopics[:3]
    gastextes = []
    for topic in gastopics:
        #text = topic.gastopictext_set.get.photo.url
        text = topic.gastopictext_set.all()[0:1]
        gastextes.append(text)
    print('gastextes', gastextes)
    print('gastopics', gastopics)


    context = {'gastopics': gastopics,
               'gastextes': gastextes}
    #the home page for moreforum
    return render(request, 'main_app/index.html', context)


@login_required
def gasthemes(request):
    #show all gas themes
    gasthemes = GasTheme.objects.order_by('order')
    context = {'gasthemes': gasthemes}
    return render(request, 'main_app/gasthemes.html', context)


def gastopics(request):
    #show all gas topics
    gastopics = GasTopic.objects.order_by('date_added')

    context = {'gastopics': gastopics,
               }
    return render(request, 'main_app/gastopics.html', context)

def photoalbums(request):
    # show all photoalbums
    photoalbums = PhotoAlbum.objects.order_by('date_added')
    context = {'photoalbums': photoalbums}
    return render(request, 'main_app/photoalbums.html', context)

def photoalbum(request, photoalbum_id):
    # show all photos for a single photoalbump
    photoalbum = PhotoAlbum.objects.get(id=photoalbum_id)
    context = {'photoalbum': photoalbum}
    return render(request, 'main_app/photoalbum.html', context)


def gasthemetext(request, gastheme_id):
    # show a single gastheme and all its text and comments
    gasthemes = GasTheme.objects.order_by('order')
    gastheme = GasTheme.objects.get(id=gastheme_id)
    gasthemetext = gastheme.gasthemetext_set.all()
    gasthemetext = gasthemetext.order_by('order')
    gasthemecomments = gastheme.gasthemecomment_set.all()
    context = {'gastheme': gastheme,
               'gasthemetext': gasthemetext,
               'gasthemecomments':gasthemecomments,
               'gasthemes': gasthemes,
               }
    return render(request, 'main_app/gastheme.html', context)


def gastopictext(request, gastopic_id):
    # show a single gastopic and all its text and comments
    gastopic = GasTopic.objects.get(id=gastopic_id)
    gastopics = GasTopic.objects.order_by('date_added')
    gastopictext = gastopic.gastopictext_set.all()
    gastopictext = gastopictext.order_by('date_added')
    gastopiccomments = gastopic.gastopiccomment_set.all()
    context = {'gastopic': gastopic,
               'gastopictext': gastopictext,
               'gastopiccomments':gastopiccomments,
               'gastopics': gastopics,
               }
    return render(request, 'main_app/gastopic.html', context)


@login_required
def new_gastheme(request):
    owner = request.user
    '''add a  new gas_theme by the user'''
    if request.method !='POST':
        # no data submitte; create a blank form
        form = GasThemeForm()
    else:
        # POST data submitted; process data
        form = GasThemeForm(request.POST, request.FILES)
        if form.is_valid():
            new_gastheme = form.save(commit=False)
            new_gastheme.owner = owner
            print(str(new_gastheme.photo))
            if str(new_gastheme.photo) == '':
                new_gasthemetext.photo = 'pictures/pic.bmp'
            new_gastheme.save()
            return HttpResponseRedirect(reverse('main_app:gasthemes'))

    context = {'form':form}
    return render(request, 'main_app/new_gastheme.html', context)


@login_required
def new_gastopic(request):
    owner = request.user
    '''add a  new gas_ttopic by the user'''
    if request.method != 'POST':
        # no data submitte; create a blank form
        form = GasTopicForm()
    else:
        # POST data submitted; process data
        form = GasTopicForm(request.POST, request.FILES)

        if form.is_valid():
            new_gastopic = form.save(commit=False)
            new_gastopic.owner = owner
            if new_gastopic.avatar == '':
                print('new_gastopic.avatar = ' ,new_gastopic.avatar)
                new_gastopic.avatar = 'pictures/pic.bmp'
            new_gastopic.save()
            print('new_gastopic.id', new_gastopic.id)
            id_new = new_gastopic.id
            return HttpResponseRedirect(reverse('main_app:gastopictext', args=[id_new]))

    context = {'form': form,
               }
    return render(request, 'main_app/new_gastopic.html', context)


def new_photoalbum(request):
    owner = request.user
    '''add a  new_photoalbum by the user'''
    if request.method != 'POST':
        # no data submitte; create a blank form
        form = PhotoAlbumForm()
    else:
        # POST data submitted; process data
        form = PhotoAlbumForm(request.POST, request.FILES)

        if form.is_valid():
            new_photoalbum = form.save(commit=False)
            new_photoalbum.owner = owner
            if str(new_photoalbum.avatar) == '':
                new_photoalbum.avatar = 'pictures/pic.bmp'
            if str(new_photoalbum.text) == '':
                new_photoalbum.text = 'Без названия'
            new_photoalbum.save()

            id_new = new_photoalbum.id
            return HttpResponseRedirect(reverse('main_app:photoalbum', args=[id_new]))

    context = {'form': form,}
    return render(request, 'main_app/new_photoalbum.html', context)


@login_required
def new_photo(request, photoalbum_id):
    '''add a  new photo by the user'''
    owner = request.user
    photoalbum = PhotoAlbum.objects.get(id=photoalbum_id)
    if request.method !='POST':
        # no data submitte; create a blank form
        form = PhotoForm()
    else:
        # POST data submitted; process data
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            new_photo = form.save(commit=False)
            new_photo = new_photo
            new_photo.owner = owner
            new_photo.photoalbum = PhotoAlbum.objects.get(id=photoalbum_id)

            if str(new_photo.picture) == '':
                new_photo.picture = 'pictures/pic.bmp'

            new_photo.save()
            return HttpResponseRedirect(reverse('main_app:photoalbum', args=[photoalbum_id]))

    context = {'photoalbum':photoalbum,'form':form}
    return render(request, 'main_app/new_photo.html', context)



@login_required
def new_gasthemetext(request, gastheme_id):
    '''add a  new gas_themetext by the user'''
    gastheme = GasTheme.objects.get(id=gastheme_id)
    if request.method !='POST':
        # no data submitte; create a blank form
        form = GasThemeTextForm()
    else:
        # POST data submitted; process data
        form = GasThemeTextForm(request.POST, request.FILES)
        if form.is_valid():
            new_gasthemetext = form.save(commit=False)
            new_gasthemetext.gas_theme = gastheme
            print('1 the path of .photo are:'+str(new_gasthemetext.photo)+':')
            print('1 the path of .photo2 are:' + str(new_gasthemetext.photo2) + ':')
            if str(new_gasthemetext.photo) == '':
                new_gasthemetext.photo = 'pictures/pic.bmp'
            if str(new_gasthemetext.photo2) == '':
                new_gasthemetext.photo2 = 'pictures/pic.bmp'
            if str(new_gasthemetext.photo3) == '':
                new_gasthemetext.photo3 = 'pictures/pic.bmp'
            print('2 the path of .photo are:' + str(new_gasthemetext.photo) + ':')
            print('2 the path of .photo2 are:' + str(new_gasthemetext.photo2) + ':')
            new_gasthemetext.save()
            return HttpResponseRedirect(reverse('main_app:gasthemetext', args=[gastheme_id]))

    context = {'gastheme':gastheme,'form':form}
    return render(request, 'main_app/new_gasthemetext.html', context)


@login_required
def new_gastopictext(request, gastopic_id):
    '''add a  new gas_themetext by the user'''
    gastopic = GasTopic.objects.get(id=gastopic_id)
    if request.method != 'POST':
        # no data submitte; create a blank form
        form = GasTopicTextForm()
    else:
        # POST data submitted; process data
        form = GasTopicTextForm(request.POST, request.FILES)
        if form.is_valid():
            new_gastopictext = form.save(commit=False)
            new_gastopictext.gas_topic = gastopic
            print('1 the path of .photo are:' + str(new_gastopictext.photo) + ':')
            print('1 the path of .photo2 are:' + str(new_gastopictext.photo2) + ':')
            if str(new_gastopictext.photo) == '':
                new_gastopictext.photo = 'pictures/pic.bmp'
            if str(new_gastopictext.photo2) == '':
                new_gastopictext.photo2 = 'pictures/pic.bmp'
            if str(new_gastopictext.photo3) == '':
                new_gastopictext.photo3 = 'pictures/pic.bmp'
            print('2 the path of .photo are:' + str(new_gastopictext.photo) + ':')
            print('2 the path of .photo2 are:' + str(new_gastopictext.photo2) + ':')
            new_gastopictext.save()
            return HttpResponseRedirect(reverse('main_app:gastopictext', args=[gastopic_id]))

    context = {'gastopic': gastopic, 'form': form}
    return render(request, 'main_app/new_gastopictext.html', context)


@login_required
def edit_gasthemetext(request, gasthemetext_id):
    # edit an existing gasthemetext
    gasthemetext = GasThemeText.objects.get(id=gasthemetext_id)
    gastheme = gasthemetext.gas_theme
    if request.method != 'POST':
        # initial request pre-fill form with current gasthemetext
        form = GasThemeTextForm(instance=gasthemetext)
    else:
        # POST data submitted; process data.
        form = GasThemeTextForm(request.POST, request.FILES, instance=gasthemetext)
        if form.is_valid():
            edited_gasthemetext = form.save(commit=False)
            edited_gasthemetext.gas_theme = gastheme
            if str(edited_gasthemetext.photo) == '':
                edited_gasthemetext.photo = 'pictures/pic.bmp'
            if str(edited_gasthemetext.photo2) == '':
                edited_gasthemetext.photo2 = 'pictures/pic.bmp'
            if str(edited_gasthemetext.photo3) == '':
                edited_gasthemetext.photo3 = 'pictures/pic.bmp'
            print('2 the path of .photo are:' + str(edited_gasthemetext.photo) + ':')
            print('2 the path of .photo2 are:' + str(edited_gasthemetext.photo2) + ':')
            edited_gasthemetext.save()
        return HttpResponseRedirect(reverse('main_app:gasthemetext', args=[gastheme.id]))

    context = {'gasthemetext': gasthemetext, 'gastheme': gastheme, 'form':form}
    return render(request, 'main_app/edit_gasthemetext.html', context)


@login_required
def edit_gastopictext(request, gastopictext_id):
    # edit an existing gasthemetext
    gastopictext = GasTopicText.objects.get(id=gastopictext_id)
    gastopic = gastopictext.gas_topic
    if request.method != 'POST':
        # initial request pre-fill form with current gastopictext
        form = GasTopicTextForm(instance=gastopictext)
    else:
        # POST data submitted; process data.
        form = GasTopicTextForm(request.POST, request.FILES, instance=gastopictext)
        if form.is_valid():
            edited_gastopictext = form.save(commit=False)
            edited_gastopictext.gas_theme = gastopic
            if str(edited_gastopictext.photo) == '':
                edited_gastopictext.photo = 'pictures/pic.bmp'
            if str(edited_gastopictext.photo2) == '':
                edited_gastopictext.photo2 = 'pictures/pic.bmp'
            if str(edited_gastopictext.photo3) == '':
                edited_gastopictext.photo3 = 'pictures/pic.bmp'
            print('2 the path of .photo are:' + str(edited_gastopictext.photo) + ':')
            print('2 the path of .photo2 are:' + str(edited_gastopictext.photo2) + ':')
            edited_gastopictext.save()
        return HttpResponseRedirect(reverse('main_app:gastopictext', args=[gastopic.id]))

    context = {'gastopictext': gastopictext,
               'gastopic': gastopic,
               'form':form,
               }
    return render(request, 'main_app/edit_gastopictext.html', context)


def new_gasthemecomment(request, gastheme_id):
    '''add a  new gas_themetext by the user'''
    gastheme = GasTheme.objects.get(id=gastheme_id)
    if request.method != 'POST':
        # no data submitte; create a blank form
        form = GasThemeCommentForm()
    else:
        # POST data submitted; process data
        form = GasThemeCommentForm(request.POST)
        if form.is_valid():
            new_gasthemecomment = form.save(commit=False)
            new_gasthemecomment.gas_topic = gastheme
            new_gasthemecomment.save()
            return HttpResponseRedirect(reverse('main_app:gasthemetext', args=[gastheme_id]))

    context = {'gastheme': gastheme, 'form': form}
    return render(request, 'main_app/new_gasthemecomment.html', context)


def new_gasthemecommentreply(request, gasthemecomment_id):
    '''add a  new gas_themecommentreply by the user'''
    gasthemecomment = GasThemeComment.objects.get(id=gasthemecomment_id)
    if request.method != 'POST':
        # no data submitte; create a blank form
        form = GasThemeCommentReplyForm()
    else:
        # POST data submitted; process data
        form = GasThemeCommentReplyForm(request.POST)
        if form.is_valid():
            new_gasthemecommentreply = form.save(commit=False)
            new_gasthemecommentreply.gasthemecomment = gasthemecomment
            new_gasthemecommentreply.save()
            return HttpResponseRedirect(reverse('main_app:gasthemetext', args=[gasthemecomment.gas_topic.id]))

    context = {'gasthemecomment': gasthemecomment, 'form': form}
    return render(request, 'main_app/new_gasthemecommentreply.html', context)




def new_gastopiccomment(request, gastopic_id):
    '''add a  new gas_topiccomment by the user'''
    gastopic = GasTopic.objects.get(id=gastopic_id)
    if request.method != 'POST':
        # no data submitte; create a blank form
        form = GasTopicCommentForm()
    else:
        # POST data submitted; process data
        form = GasTopicCommentForm(request.POST)
        if form.is_valid():
            new_gastopiccomment = form.save(commit=False)
            new_gastopiccomment.gas_topic = gastopic
            new_gastopiccomment.save()
            return HttpResponseRedirect(reverse('main_app:gastopictext', args=[gastopic_id]))

    context = {'gastopic': gastopic, 'form': form}
    return render(request, 'main_app/new_gastopiccomment.html', context)
















