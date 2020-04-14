from rest_framework import serializers
from main.models import Todo, MyUser


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
            raise serializers.ValidationError('very short text')
        return value

    def validate(self, attrs):
        return attrs


class TodoFullSerializer(TodoShortSerializer):
    created_by = MyUserSerializer(read_only=True)

    class Meta(TodoShortSerializer.Meta):
        fields = TodoShortSerializer.Meta.fields + ('created_by', )
