#from memories.webapp.models import ratings
from rest_framework import serializers
from webapp.models import Senior,Seniorinfo,awards,imagegallery,ratings

class SeniorSerializer(serializers.ModelSerializer):

    class Meta:
        model= Senior
        fields = '__all__'


class awardsSerializer(serializers.ModelSerializer):

    class Meta:
        model= awards
        fields = '__all__'


class imagegallerySerializer(serializers.ModelSerializer):

    class Meta:
        model= imagegallery
        fields = '__all__'

class ratingsSerializer(serializers.ModelSerializer):

    class Meta:
        model= ratings
        fields='__all__'


class SeniorinfoSerializer(serializers.ModelSerializer):
    award = awardsSerializer(many=True,read_only=True)
    #awards= serializers.SerializerMethodField()
    #awards = serializers.RelatedField(many=True, read_only=True)
    gall = imagegallerySerializer(many=True,read_only=True)
    rat = ratingsSerializer(many=True,read_only=True)

    class Meta:
        model= Seniorinfo
        fields= ('description','sname','pic','award','gall','rat')
        
        #fields ='__all__'

      #  def get_awrds(self, obj):
      #      return awardsSerializer(obj.awards.all(), many=True, read_only=True).data
