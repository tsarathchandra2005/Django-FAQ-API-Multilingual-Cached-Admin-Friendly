from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator
from django.core.cache import cache
# from rest_framework import serializers
# Create your models here.
# hi-hindi bn-bengali fr-french es-spanish
# te-telugu ru-russian de-German zh-chinese
Languages = ["hi", "bn", "fr", "es", "te", "ru", "de", "zh"]


class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def get_translation(self, lang):
        """Retrived or recieved a generated question """
        if lang not in Languages:
            return self.question  # Default to English

        cache_key = f"faq_{self.id}_question_{lang}"
        translated_text = cache.get(cache_key)

        if not translated_text:
            translator = Translator()
            translated_text = translator.translate(
                self.question, dest=lang).text
            # cache is set for 1day
            cache.set(cache_key, translated_text, timeout=86400)

        return translated_text

    def __str__(self):
        return self.question
