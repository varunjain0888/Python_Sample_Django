from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,Http404,HttpResponseRedirect
from models import Question, Choice
from django.shortcuts import render,get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic

# This is the same implementation but without using genric view of python i.e this is the core hard work implementation

# def index(request):
#     latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
#     output = ', '.join(question.question_text for question in latest_question_list.get('question_text'))
#     return render(output,'polls/index.html',context = {'latest_question_list':latest_question_list})
#
# def detail(request,question_id):
#     try :
#         question = Question.objects.get(pk = question_id)
#     except Question.DoesNotExist :
#         raise Http404("Question does not exixts")
#     return render(request , 'polls/detail.html' , context = {'question' : question})
#
# def results(request,question_id):
#     question = get_object_or_404(Question,pk=question_id)
#     return render(request , 'polls/results.html',{'question': question})



class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name =  'latest_question_list'

    def get_queryset(self):
        """return last published five questions"""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultViews(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'



def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except (KeyError , Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request , 'polls/detail.html' ,{'question' : question, 'error_message':"You did not select a choice."})
    else:
        selected_choice.votes +=1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
    return HttpResponseRedirect(reverse('polls:results' , args=(question.id,)))

