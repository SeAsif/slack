from rest_framework import serializers

from .models.channel import Channel
from .models.company import Company 
from .models.message import Message

class ChannelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Channel
		fields = '__all__'
		read_only_fields = ('id',)


class CompanySerializer(serializers.ModelSerializer):
	class Meta: 
		model = Company
		fields = '__all__'
		read_only_fields = ('id', 'owner')


class MessageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Message
		fields = '__all__'
		read_only_fields = ('id', 'sender')
