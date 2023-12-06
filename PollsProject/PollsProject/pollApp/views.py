from django.shortcuts import render, redirect
from .forms import CreatePollForm
from .models import poll
# Create your views here.
def home(request):
    allPolls = poll.objects.all()
    context = {"allPolls" : allPolls}
    return render(request, "home.html", context)

def create(request):
    if request.method == "POST":
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = CreatePollForm()
    context = {"form" : form, }
    return render(request, "create.html", context)

def vote(request, poll_id):
    curr_poll = poll.objects.get(pk = poll_id)

    if(request.method == "POST"):
        poll_res = request.POST['polls']
        #print(poll_res)
        if poll_res == 'option1':
            curr_poll.opt1_count += 1
        elif poll_res == 'option2':
            curr_poll.opt2_count += 1
        elif poll_res == 'option3':
            curr_poll.opt3_count += 1
        else:
            print('Error no valid option')
        curr_poll.save()
        return redirect('results', poll_id)
    
    context = {"curr_poll" : curr_poll}
    return render(request, "vote.html", context)

def results(request, poll_id):
    curr_poll = poll.objects.get(pk = poll_id)
    context = {"curr_poll" : curr_poll}
    return render(request, "results.html", context)