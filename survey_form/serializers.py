from rest_framework import serializers
from survey_form.models import Category

class CategorySerializer(serializers.ModelSerializer):
  # specify model and fields
    class Meta:
        model = Category
        fields = "__all__"
