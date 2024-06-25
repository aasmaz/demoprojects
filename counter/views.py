from django.shortcuts import render

# Create your views here.

# Word counter app
def counter(request):
    if request.method == 'POST':
        text = request.POST['texttoword']
        if text!= '':
            word = len(text.split())
            char = len(text)
            i = True
            return render(request, 'counter.html', {'word': word, 'char': char, 'text': text, 'i': i, 'on': 'active'})
        else:
            return render(request, 'counter.html', {'on': 'active'})
    else:
        return render(request, 'counter.html', {'on':'active'})
    
