from rest_framework import serializers
from .models import Post, Comment, Reviews, Image

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['user']  # Protege o campo de edição pelo cliente

    def create(self, validated_data):
        # Garantir que o 'user' será atribuído automaticamente ao criar um novo post
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['user']

    def create(self, validated_data):
        # Garantir que o 'user' será atribuído automaticamente ao criar um novo comentário
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'
        read_only_fields = ['user']

    def create(self, validated_data):
        # Garantir que o 'user' será atribuído automaticamente ao criar uma nova avaliação
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image', 'post']  # Inclua o campo 'post' aqui
        read_only_fields = ['user'] #

    def create(self, validated_data):
        # Garantir que o 'user' será atribuído automaticamente ao adicionar uma nova imagem
        validated_data['user'] = self.context['request'].user
        
        # Garantir que o 'post' seja atribuído ao criar a imagem
        validated_data['post'] = self.context['request'].data.get('post')
        
        return super().create(validated_data)
