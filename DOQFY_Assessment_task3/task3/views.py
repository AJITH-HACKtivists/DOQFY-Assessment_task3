from django.shortcuts import render
from django.views.generic import TemplateView
from .scapper import scrape_data
from redis import Redis
import json
# Create your views here.
redis_conn = Redis()

class ScrapperView(TemplateView):
    template_name = 'task3/task3.html'
    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        try:

            nifty_data = redis_conn.get('nifty_50')
            if nifty_data:
                nifty_data = json.loads(nifty_data)
                context['nifty_data'] = nifty_data
            else:
                context['nifty_data'] = []
        except Exception as e:
            context['error'] = 'Something wrong with redies Please try Again After sometime'
        
       
        return self.render_to_response(context)