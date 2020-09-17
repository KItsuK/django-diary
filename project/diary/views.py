from django.shortcuts import render, redirect, get_object_or_404
from .forms import DayCreatForm
from .models import Day

def index(request):
    context = {
        'day_list':Day.objects.all(),
    }
    print(context['day_list'])
    return render(request, 'diary/day_list.html', context)

def add(request):
    #送信内容に基づいてフォーム作成。POST出なければ空のフォーム
    form = DayCreatForm(request.POST or None)

    #method=POST
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('diary:index')

    context = {
            'form':form
    }
    return render(request, 'diary/day_form.html', context)

def update(request):
    #urlのpkを基にDayを取得
    day = get_object_or_404(Day, pk=pk)

    #フォームに取得したDayを結びつける
    form = DayCreatForm(request.POST or None, instance=day)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('diary:index')

    context = {
            'form':form
    }
    return render(request, 'diary/day_form.html', context)

def delete(request):
    #urlのpkを基にDayを取得
    day = get_object_or_404(Day, pk=pk)

    if request.method == 'POST':
        day.delete()
        return redirect('diary:index')

    context = {
            'day':day
    }
    return render(request, 'diary/day_confirm_delete.html', context)
