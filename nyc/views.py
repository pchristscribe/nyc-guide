from django.shortcuts import render
from django.views import View

from nyc.boroughs import boroughs


class CityView(View):
    def get(self, request):
        return render(
            request=request, 
            template_name='city.html', 
            context={'boroughs': boroughs.keys()})


class BoroughView(View):
    def get(self, request, borough):
        return render(
            request=request,
            template_name='borough.html',
            context={
                'borough': borough, 
                'activities': boroughs[borough].keys(),
                },
        )

#just copied above class, changing template and adding the get for the activity and the next level down (activities)in the boroughs dictionary
class ActivityView(View):
    def get (self, request, borough, activity):
        return render(
            request= request, 
            template_name= "activity.html",
            context={
                'borough': borough, 
                'activity': activity,
                'venues': boroughs[borough][activity].keys(),
                }
       )
    

#just copied above class, changing template and adding the get for the venue and next level down (venues) in the boroughs dictionary
class VenueView(View):
    def get (self, request, borough, activity, venue):
        return render(
            request= request, 
            template_name= "venue.html",
            context={
                'borough': borough, 
                'activity': activity,
                'venue': venue,
                'venue_description': boroughs[borough][activity][venue]['description'],
                }
        )
