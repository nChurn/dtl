from modeltranslation.translator import register, TranslationOptions

from .models import *

@register(MainPage)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('first_subtext', 'second_text', 'second_subtext', 'third_text', 'fourth_text',)

@register(Contacts)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'address',)

@register(About)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'block1_pretext', 'block1_text', 'block2_title', 'block2_text', 'block2_quote',
     'block2_text2', 'block3_title', 'block3_text', 'block4_title', 'block4_subtitle1', 'block4_item1',
     'block4_item2', 'block4_subtitle2', 'block4_item3', 'block4_item4',)

@register(Team)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'pretext',)

@register(ActionDirection)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'pretext', 'text', 'subtitle',)

@register(ActionDirectionItems)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('text',)

@register(Person)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'job', 'pretext',)

@register(PersonBio)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('period', 'text',)

@register(Career)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'pretext', 'specialists_text', 'students_text',)

@register(CareerAdvantages)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('text',)

@register(CareerDemands)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('text',)

@register(Actives)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'pretext', 'block1_title', 'block1_subtitle', 'block1_text', 'block2_subtitle',
     'block2_item1', 'block2_item2', 'block2_item3', 'block3_subtitle', 'block3_text', 'block4_subtitle',
     'block4_text',)

@register(Expertise)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'pretext',)

@register(Industry)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(Project)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('client', 'title', 'title_preview', 'inv', 'inv_text', 'per', 'per_text', 'geo', 'geo_text',
     'pretext', 'text', 'subtitle',)

@register(ProjectPage)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(ProjectItem)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('text',)

@register(NewsPage)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(News)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'pretext', 'text', 'subtitle1', 'text1', 'subtitle2', 'text2', 'button_text',)
