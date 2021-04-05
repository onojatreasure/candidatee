from django.shortcuts import render, redirect

from .forms import CandidateForm
from .models import Candidate

# Create your views here.
candidateCount = 0

def candidate_list(request):
    context = {'candidate_list': Candidate.objects.all()}
    global candidateCount
    candidateCount = Candidate.objects.count()
    print('get all candudates', candidateCount)
    return render(request, "candidate_register/candidate_list.html", context)


def candidate_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = CandidateForm()
        else:
            candidate = Candidate.objects.get(pk=id)
            print('candidate')
            form = CandidateForm(instance=candidate)
        return render(request, "candidate_register/candidate_form.html", {'form': form})
    else:

        if id == 0: #This is an insert operation
            form = CandidateForm(request.POST)
        else: #Id exists and is an update operation
            candidate = Candidate.objects.get(pk=id)
            form = CandidateForm(request.POST,instance= candidate)
        if form.is_valid():
            #Check if the total number of candidate is less thean before saving. Can only add candidates if it is not more than 10.
            if candidateCount < 10:
                form.save()
            else: 
                return redirect("candidate_register/candidate_form.html")

            #form.save()
        return redirect('/candidate/list')


def candidate_delete(request,id):
    candidate = Candidate.objects.get(pk=id)
    candidate.delete()
    return redirect('/candidate/list')