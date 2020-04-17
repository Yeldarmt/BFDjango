import logging
import os
from rest_framework import serializers
from main.models import Todo, MyUser

split_text = os.path.splitext(__name__)
logger = logging.getLogger(split_text[0])


class MyUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = MyUser
        fields = ('id', 'username', 'email', 'password')


class TodoShortSerializer(serializers.ModelSerializer):
    description = serializers.CharField()
    created_by_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'completed', 'created_by_id', )

    def validate_description(self, value):
        if len(value) < 20:
            logger.debug('description must be more than 20 character, description length now : {}'.format(len(value)))
            logger.info('description must be more than 20 character, description length now : {}'.format(len(value)))
            logger.warning('description must be more than 20 character, description length now : {}'.format(len(value)))
            logger.error('description must be more than 20 character, description length now : {}'.format(len(value)))
            logger.critical('description must be more than 20 character, description length now : {}'.format(len(value)))
            raise serializers.ValidationError('very short text')
        return value

    def validate(self, attrs):
        return attrs


class TodoFullSerializer(TodoShortSerializer):
    created_by = MyUserSerializer(read_only=True)

    class Meta(TodoShortSerializer.Meta):
        fields = TodoShortSerializer.Meta.fields + ('created_by', )
