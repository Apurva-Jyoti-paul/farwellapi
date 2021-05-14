from django.contrib import admin
from .models import Senior,Seniorinfo,awards,imagegallery, ratings,fav_place



class awardsInline(admin.StackedInline):
    model = awards
    extra = 3

class imagegalleryInline(admin.StackedInline):
    model = imagegallery
    extra = 8

class ratingsInline(admin.StackedInline):
    model = ratings
    extra = 3

class fav_placeInline(admin.StackedInline):
    model = fav_place
    extra = 1



class SeniorinfoAdmin(admin.ModelAdmin):
    fields=['sname','description','description2','senior','pic']
    inlines=[awardsInline,imagegalleryInline,ratingsInline,fav_placeInline]


admin.site.register(Senior)
admin.site.register(Seniorinfo,SeniorinfoAdmin)
admin.site.register(awards)
admin.site.register(imagegallery)
admin.site.register(ratings)



# Register your models here.
