import json
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.urls import reverse
from app_chat.models import Chat
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from app_base.models import Course
from django.contrib.auth.decorators import login_required


def home(request):
    ctx = {}
    ctx['courses'] = Course.objects.all()
    return render(request, 'home.html', ctx)


def course_detail(request, slug):
    ctx = {}
    ctx['course'] = course = Course.objects.get(slug=slug)
    ctx['courses'] = Course.objects.all().exclude(slug=slug)
    return render(request, 'course-detail.html', ctx)


def course_session_detail(request, course_slug, session_slug):
    ctx = {}
    course = Course.objects.get(slug=course_slug)
    ctx['session'] = course.coursesession_set.get(slug=session_slug)
    return render(request, 'course-session-detail.html', ctx)


def course_session_exercise_detail(request, course_slug, session_slug, exercise_slug):
    ctx = {}
    course = Course.objects.get(slug=course_slug)
    session = course.coursesession_set.get(slug=session_slug)
    ctx['exercise'] = session.coursesessionexercise_set.get(slug=exercise_slug)
    return render(request, 'exercise-detail.html', ctx)


@login_required
def register_course(request, course_id):
    course = Course.objects.get(id=course_id)
    if course not in [rc.course for rc in request.user.registeredcourse_set.all()]:
        request.user.registeredcourse_set.create(course=course)
        messages.success(
            request, '%s عزیز، خوشحالم که در این دوره شرکت کردی. حالا میتونی این دوره رو از توی پروفایلت با من شروع کنی :)' % request.user.username)
    else:
        messages.success(
            request, '%s عزیز، شما قبلا در این دوره ثبت نام کرده اید!' % request.user.username)
    return HttpResponseRedirect(reverse('app-accounts:profile'))


@login_required
def change_seen_status(request):
    msg_id = request.GET.get('msg_id')
    if msg_id:
        try:
            msg_id = int(msg_id)
            msg = Chat.objects.filter(id=msg_id)
            if msg:
                msg_owner_groups = [gp.name for gp in msg[0].user.groups.all()]
                requested_user_groups = [gp.name for gp in request.user.groups.all()]
                if ('students' in msg_owner_groups and 'operators' in requested_user_groups) or \
                        ('operators' in msg_owner_groups and 'students' in requested_user_groups):
                    msg = msg[0]
                    msg.seen = True
                    msg.save()
        except ValueError:
            return HttpResponseBadRequest()
    response_data = {}
    return HttpResponse(json.dumps(response_data), content_type="application/json")