from django.shortcuts import render, redirect
from django.views import *
from .models import *


class StatistikaView(View):
    def get(self, request):
        if request.user.is_authenticated:
            sotuvlar = Sotuv.objects.filter(tarqatuvchi=request.user)
            mahsulot = Mahsulot.objects.filter(tarqatuvchi=request.user)
            mijoz = Mijoz.objects.filter(tarqatuvchi=request.user)
            context = {
                "sotuvlar": sotuvlar,
                'mahsulotlar': mahsulot,
                'mijozlar': mijoz,
                'tarqatuvchi': request.user
            }
            return render(request, 'statistikalar.html', context)
        return redirect('login')

    def post(self, request):
        if request.user.is_authenticated:
            Sotuv.objects.create(
                mahsulot=Mahsulot.objects.get(id=request.POST.get('mahsulot')),
                mijoz=Mijoz.objects.get(id=request.POST.get('mijoz')),
                sana=request.GET.get('sana'),
                miqdor=request.GET.get('miqdor'),
                summa=request.GET.get('summa'),
                tolandi=request.GET.get('tolandi'),
                qarz=request.GET.get('qarz'),
                tarqatuvchi=request.user
                )
            return redirect('statistika')
        return redirect('login')
