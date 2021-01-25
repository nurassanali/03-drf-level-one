from datetime import datetime
from rest_framework import serializers
from django.utils.timesince import timesince
from news.models import Article, Journalist

class ArticleSerializer(serializers.ModelSerializer):

  time_since_publication = serializers.SerializerMethodField()
  # author = JournalistSerializer()
  # author = serializers.StringRelatedField()
  class Meta:
    model = Article
    exclude = ("id",)
    # fields = "__all__" #to serialize all the fields from our model
    # fields = {"title", "description", "body"} #to serialize couple of fields

  def get_time_since_publication(self, object):
    publication_date = object.publication_date
    now = datetime.now()
    time_delta = timesince(publication_date, now)
    return time_delta

  def validate(self, data):
    """ check that description and title are differen """
    if data["title"] == data["description"]:
      raise serializers.ValidationError("Title and description must be different from one another")
    return data

  def validate_title(self, value):
    if len(value) < 30:
      raise serializers.ValidationError("The title should be more then 30 symbols")
    return value

class JournalistSerializer(serializers.ModelSerializer):
  articles = serializers.HyperlinkedRelatedField(many=True,
                                                  read_only=True,
                                                  view_name="article-detail")
  # articles = ArticleSerializer(many=True, read_only=True)
  class Meta:
    model = Journalist
    fields = "__all__"
