# Create your views here.
import traceback
import requests
import time
from django.db.models import Q
#from mylogger import LOG
from datetime import timedelta,datetime, timezone ,timedelta
from feed.models import Newsfeed
from django.shortcuts import render, redirect
from urllib.request import urlopen
from django import template
from rest_framework.views import APIView
from newsfeed.settings import (LIST_FEEDS_ID, LIST_FEED_URL, APP_ID, APP_KEY)
from aylienapiclient import textapi                          
#from mysite.core.models impLIST_FEED_URLort Profile


class Newsinfo(APIView):

	def get(request):
		list_feeds_id = LIST_FEEDS_ID
		list_feeds_url = LIST_FEED_URL
		app_id = APP_ID
		app_key = APP_KEY
		#list_accounts = []
		try:
			res = requests.get(list_feeds_id)
			list_id = res.json()
			for id in list_id:
				#LOG.info("sleeping in account urls request...")
				#time.sleep(10)
				res = requests.get(list_feeds_url.format(str(id)))
				resjson = res.json()
				#print("ID ->", resjson.get('id'))
				#print("Author ->", resjson.get('by'))
				#print("Title ->", resjson.get('title'))
				#print("Score ->", resjson.get('score'))
				#print("type ->", resjson.get('type'))
				#print("Url ->", resjson.get('url'))
				#print("Time ->", resjson.get('time'))
				news = Newsfeed()
				news.id = resjson.get('id')
				news.by = resjson.get('by')
				news.title = resjson.get('title')
				news.score = resjson.get('score')
				news.type = resjson.get('type')
				news.url = resjson.get('url')		 #news.time = resjson.get('time')
				#print("Saving Records to DB")				
				#news.save()
				#time.sleep(15)
				#storing = Newsfeed.objects.all()
				#for temp in Newsfeed.objects.all():
				#print(temp.title)
				client = textapi.Client(app_id, app_key)
				sentiment = client.Sentiment({'text': news.title})
				news.computedsentiment = sentiment['polarity']
				news.save()				
				print("Saving Records to DB")
				time.sleep(5)
				#LOG.info(">>> account under project {0}, {1}".format(str(project),resjson))
				#if len(resjson)!=0:
					#for doc in resjson:
						#doc["project_id"] = project["id"]
						#list_accounts.append(doc)
				#if resjson['url'] is None:
					#print("No Key for this Feed")
				#else:
					#pass
			return
			#return list_accounts
		except Exception as e:
			#LOG.error("Error is occurred in list of projects:%s"%e)
			raise
			
indetail = Newsinfo()
indetail.get()

#class RendertoUI(APIView):

def RendertoUI(request):

	#storing = Newsfeed.objects.all()
	list_feeds_id = LIST_FEEDS_ID
	list_feeds_url = LIST_FEED_URL
	try:
		res = requests.get(list_feeds_id)
		list_id = res.json()
		for id in list_id:
			res = requests.get(list_feeds_url.format(str(id)))
			resjson = res.json()
			print("feed->", resjson)
	except Exception as e:
			#LOG.error("Error is occurred in list of projects:%s"%e)
		print("e", e)	
		raise	
	return render(request, 'home.html', {'feeds': resjson })

#def RendertoUI(request):
#	storing = Newsfeed.objects.all()
#	return render(request, 'home.html', {'feeds': storing })

def searchposts(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(title__icontains=query) | Q(url__icontains=query)

            results= Newsfeed.objects.filter(lookups).distinct()
            print("results", results)

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'myfeed.html', context)

        else:
            return render(request, 'myfeed.html')

    else:
        return render(request, 'myfeed.html')