from django.shortcuts import render

# Create your views here.
def SuperAdmin_index(request):
     return render(request, 'SuperAdmin_index.html')


def SuperAdmin_pay_det(request):
     return render(request, 'SuperAdmin_pay_det.html')


def SuperAdmin_current_trainees(request):
     return render(request, 'SuperAdmin_current_trainees.html')

def SuperAdmin_current_trainees_payment(request):
     return render(request, 'SuperAdmin_current_trainees_payment.html')

def SuperAdmin_current_trainees_payment_add(request):
     return render(request, 'SuperAdmin_current_trainees_payment_add.html')

def SuperAdmin_current_trainees_payment_update(request):
     return render(request, 'SuperAdmin_current_trainees_payment_update.html')




def SuperAdmin_previous_trainees_payment(request):
     return render(request, 'SuperAdmin_previous_trainees_payment.html')
