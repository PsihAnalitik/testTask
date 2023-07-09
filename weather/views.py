from django.shortcuts import render
from . import script
from .models import Comment
from .forms import CommentForm

def index(request):
    prediction = 0
    content = ''
    isPositive = ''
    form = CommentForm()
    if(request.method == 'POST'):
        form = CommentForm(request.POST)
        form.save()
        form = CommentForm()

        curComment = Comment.objects.last()
        prediction = script.BERT(curComment.name)

        if prediction > 4:
                isPositive  = 'Положительный :)'
        elif prediction > 0:
                isPositive = 'Отрицательный :('

        result = {
                'comment': curComment.name,
                'rating':  prediction,
                'isPositive': isPositive
        }
        context = {'info': result, 'form': form}

        return render(request, 'weather/index.html', context)
    return render(request, 'weather/index.html', {'form': form})

