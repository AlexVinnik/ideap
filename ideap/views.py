from django.shortcuts import render, HttpResponse
import vk

# Create your views here.

def post_list(request):
    if request.method == 'POST':
        log = request.POST.get('name_field')
        pas = request.POST.get('name_pass')
        wall = request.POST.get('name_wall')
        session = vk.AuthSession(app_id='6491609', user_login=log, user_password=pas, scope='wall, messages')
        api = vk.API(session, v='5.35')
        api.messages.send(user_id=84739342, attachment=wall)
        return HttpResponse('Сообщения отправлены')

    return render(request, 'blog.html', {})

def wall_post(request):
    if request.method == 'POST':
        return render(request, 'blog.html', {})