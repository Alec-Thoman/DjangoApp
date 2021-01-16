from django.shortcuts import render, HttpResponse
import pandas as pd

def Table(request):
	df = pd.read_csv("Users/alecthoman/Desktop/NewDjango/freshdjango/DjangoData.csv")

	geeks_object = df.to_html()

	return HttpResponse(geeks_object)

	