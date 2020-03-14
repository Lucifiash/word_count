from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')


def count(request):
    uesr_text = request.GET['text']
    total_count = len(uesr_text)
    dict_word = {}
    for word in uesr_text:
        if word not in dict_word:
            dict_word[word] = 1
        else:
            dict_word[word] += 1
    sorted_dict =\
        sorted(dict_word.items(),key=lambda  w : w[1] ,reverse=True)

    return render(request, 'count.html',
                  {'count':total_count,'text':uesr_text,
                   'worddict': dict_word,'sorted' : sorted_dict})

def about(request):
    return render(request,'about.html')
