from django.shortcuts import render

creators = [
	{
		'name':'SMEET KOTHARI',
		'roll_no':'18BCE230'
	},
	{
		'name':'ZEEL SHAH',
		'roll_no':'18BCE222'
	},
	{
		'name':'SUMIT PATEL',
		'roll_no':'18BCE236'
	}
]

def homepage(request):
	return render(request, 'blog/homepage.html')

"""from .df_bse import df_bse
def dfbse(requets):
	DataFrame = df_bse
	return render(request, 'blog/dfbse.html', {'DataFrame': DataFrame})"""

"""from .df_nse import df_nse
def dfnse(requets):
	DataFrame = df_nse
	return render(request, 'blog/dfnse.html', {'DataFrame': DataFrame})"""

def dashboard(request):
	context = {
		'creators':creators
	}
	return render(request, 'blog/aboutme.html', context)