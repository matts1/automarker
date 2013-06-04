from django.shortcuts import render_to_response
from problems.models import Problem

def view(request):
    # TODO: if user is admin, get all problems
    # else, get all problems that aren't hidden
    problems = Problem.objects.all()
    return render_to_response('problems/list.html', {'problems': problems})
