from .models import Transaction, customerdetails
from django.shortcuts import redirect, render

# Create your views here.


def home(request):
    return render(request, 'index.html')


def customer(request):
    customers = customerdetails.objects.all()

    if request.method == 'POST':
        email = request.POST['email']
        send_email = request.POST['semail']
        amt = request.POST['amt']
        try:
            amt = int(amt)
        except:
            print('enter gain')
        for i in customers:
            if(i.email == email):
                temp = i
                sl = i.id
                break
        for i in customers:
            if i.email == send_email and amt < i.curr_bal and amt > 0:
                curr_bal = i.curr_bal - amt
                new_bal = temp.curr_bal + amt
                try:
                    line1 = Transaction(
                        name=i.name, email=i.email, deb_amt=amt, cr_amt=0, acc_bal=curr_bal)
                    line2 = customerdetails(
                        id=i.id, curr_bal=curr_bal, email=i.email, name=i.name)
                    line3 = Transaction(
                        name=temp.name, email=temp.email, deb_amt=0, cr_amt=amt, acc_bal=new_bal)
                    line4 = customerdetails(
                        id=temp.id, curr_bal=new_bal, email=temp.email, name=temp.name)
                    line1.save()
                    line2.save()
                    line3.save()
                    line4.save()
                    return redirect('customer')
                except:
                    print('error')

    return render(request, 'customer.html', {'cust': customers})


def transactions(request):
    transactions = Transaction.objects.all()
    return render(request, 'transaction.html', {'transact': transactions})
