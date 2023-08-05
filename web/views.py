from django.shortcuts import render
from .models import Income,Expense

def main(request):
    return render(request, 'main.html')

def incomes(request):
    income = income.objects.order_by('-time')
    return render(request, 'incomes_list.html', {'income':income})

def expenses(request):
    expense = Expense.objects.order_by('-time')
    return render(request, 'expense.html', {'expense':expense})
