from django.shortcuts import render

def index (request):

	return render(request, 'basicTemplate/home.html',
		{'values':[['1','Первая партия','11 кг','30000 руб.'], ['2','Вторая партия','8 кг','15000 руб.'],['3','Третья партия','5 кг','3000 руб.']]})

def batch (request):
	return render(request, 'basicTemplate/batch.html', {'values': ['Контактные данные','(123)132-12-12','123@123.ru']})
