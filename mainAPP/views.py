from django.shortcuts import render, redirect
from django.views import *
from .models import *
from django.db.models import Q
import datetime


class BolimlarView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, "bo'limlar.html")
        return redirect('login')


class MahsulotlarViews(View):
    def get(self, request):
        if request.user.is_authenticated:
            mahsulotlar = Mahsulot.objects.filter(tarqatuvchi=request.user)
            if request.GET.get('search'):
                mahsulotlar = mahsulotlar.filter(
                    Q(nom__contains=request.GET.get('search')) |
                    Q(brend__contains=request.GET.get('search'))
                )
            context = {
                "mahsulotlar": mahsulotlar,
                'tarqatuvchi': request.user
            }
            return render(request, "mahsulotlar.html", context)
        return redirect('login')

    def post(self, request):
        if request.user.is_authenticated:
            Mahsulot.objects.create(
                nom=request.POST['nom'],
                brend=request.POST['brend'],
                narx1=request.POST['narx1'],
                narx2=request.POST['narx2'],
                miqdor=request.POST['miqdor'],
                olchov=request.POST['olchov'],
                tarqatuvchi=request.user,
                sana=request.POST['sana']
            )
            return redirect('mahsulotlar')


class MijozView(View):
    def get(self, request):
        if request.user.is_authenticated:
            mijozlar = Mijoz.objects.filter(tarqatuvchi=request.user)
            if request.GET.get('search'):
                mijozlar = mijozlar.filter(
                    Q(ism__contains=request.GET.get('search')) |
                    Q(dokon__contains=request.GET.get('search')) |
                    Q(tel__contains=request.GET.get('search'))
                )
            context = {
                "mijozlar": mijozlar,
                'tarqatuvchi': request.user
            }
        return render(request, 'mijozlar.html', context)

    def post(self, request):
        if request.user.is_authenticated:
            Mijoz.objects.create(
                ism=request.POST['ism'],
                dokon=request.POST['dokon'],
                tel=request.POST['tel'],
                manzil=request.POST['manzil'],
                tarqatuvchi=request.user,
            )
            return redirect('mijozlar')
        return redirect('login')


class StaticView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'statistikalar.html')
        return redirect('login')


class MahsulotEditView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            mahsulot = Mahsulot.objects.get(id=pk)
            return render(request, 'mahsulot-tahrirlash.html', {"mahsulot": mahsulot})

    def post(self, request, pk):
        if request.user.is_authenticated:
            mahsulot = Mahsulot.objects.get(id=pk)
            if mahsulot.tarqatuvchi != request.user:
                return redirect('logout')
            mahsulot.nom = request.POST['nom']
            mahsulot.brend = request.POST['brend']
            mahsulot.narx1 = request.POST['narx1']
            mahsulot.narx2 = request.POST['narx2']
            mahsulot.miqdor = request.POST['miqdor']
            mahsulot.olchov = request.POST['olchov']
            mahsulot.save()
            return redirect('mahsulotlar')
        return redirect('login')


class MijozEditView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            mijoz = Mijoz.objects.get(id=pk)
            return render(request, 'mijoz-tahrirlash.html', {'mijoz': mijoz})
        return redirect('login')

    def post(self, request, pk):
        if request.user.is_authenticated:
            mijoz = Mijoz.objects.get(id=pk)
            if mijoz.tarqatuvchi != request.user:
                return redirect('logout')
            mijoz.ism = request.POST['ism']
            mijoz.dokon = request.POST['dokon']
            mijoz.tel = request.POST['tel']
            mijoz.manzil = request.POST['manzil']
            mijoz.qarz = request.POST['qarz']

            mijoz.save()
            return redirect('mijozlar')
        return redirect('login')


class MijozDeleteView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            Mijoz.objects.get(id=pk).delete()
            return redirect("mijozlar")
        return redirect('login')


class MahsulotDeleteView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            Mahsulot.objects.get(id=pk).delete()
            return redirect('mahsulotlar')
        return redirect('login')
