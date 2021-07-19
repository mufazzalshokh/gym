from modeltranslation.translator import register, TranslationOptions

from blog.models import CategoryModel


@register(CategoryModel)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)
