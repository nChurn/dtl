from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import *

# MAINPAGE

class MainPageForm(forms.ModelForm):
    class Meta:
        model = MainPage
        widgets = {
            'second_text_ru' : SummernoteWidget(),
            'third_text_ru' : SummernoteWidget(),
            'fourth_text_ru' : SummernoteWidget(),
            'second_text_en' : SummernoteWidget(),
            'third_text_en' : SummernoteWidget(),
            'fourth_text_en' : SummernoteWidget(),
        }
        fields = '__all__'

class MainPageLogoInline(admin.StackedInline):
    model = MainPageLogo
    extra = 0

class MainPageAdmin(TranslationAdmin):
    form = MainPageForm
    fieldsets = (
        ('Первый слайд', {
            'fields': ('first_subtext',)
        }),
        ('Второй слайд', {
            'fields': ('second_text', 'second_subtext',)
        }),
        ('Третий слайд', {
            'fields': ('third_text', 'third_bg', 'third_bg_mobile',)
        }),
        ('Четвёртый слайд', {
            'fields': ('fourth_text',)
        }),
    )
    inlines = (MainPageLogoInline,)



admin.site.register(MainPage, MainPageAdmin)
admin.site.register(Resume)


# ABOUT

class AboutPageForm(forms.ModelForm):
    class Meta:
        model = About
        widgets = {
            'block1_pretext_ru' : SummernoteWidget(),
            'block2_quote_ru' : SummernoteWidget(),
            'block1_pretext_en' : SummernoteWidget(),
            'block2_quote_en' : SummernoteWidget(),
        }
        fields = '__all__'

class AboutPageAdmin(TranslationAdmin):
    form = AboutPageForm
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'photo',)
        }),
        ('Первый блок', {
            'fields': ('block1_pretext', 'block1_text',)
        }),
        ('Второй блок', {
            'fields': ('block2_title', 'block2_text', 'block2_quote', 'block2_text2',)
        }),
        ('Третий блок', {
            'fields': ('block3_title', 'block3_text',)
        }),
        ('Четвёртый блок', {
            'fields': ('block4_title', 'block4_subtitle1', 'block4_item1', 'block4_item2', 'block4_subtitle2', 'block4_item3', 'block4_item4',)
        }),
    )

admin.site.register(About, AboutPageAdmin)

# TEAM

class TeamPageForm(forms.ModelForm):
    class Meta:
        model = Team
        widgets = {
            'pretext_ru' : SummernoteWidget(),
            'pretext_en' : SummernoteWidget(),
        }
        fields = '__all__'

class TeamPageAdmin(TranslationAdmin):
    form = TeamPageForm
    filter_horizontal = ('people', )

class ActionDirectionInline(admin.StackedInline):
    model = ActionDirectionItems
    extra = 0

class ActionDirectionAdmin(TranslationAdmin):
    inlines = (ActionDirectionInline,)

admin.site.register(Team, TeamPageAdmin)
admin.site.register(ActionDirection, ActionDirectionAdmin)

class PersonPageForm(forms.ModelForm):
    class Meta:
        model = Person
        widgets = {
            'pretext_ru' : SummernoteWidget(),
            'pretext_en' : SummernoteWidget(),
        }
        fields = '__all__'

class PersonPageInline(admin.StackedInline):
    model = PersonBio
    extra = 0

class PersonPageAdmin(TranslationAdmin):
    form = PersonPageForm
    filter_horizontal = ('actions', )
    inlines = (PersonPageInline,)
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Person, PersonPageAdmin)


# CAREER

class CareerPageForm(forms.ModelForm):
    class Meta:
        model = Career
        widgets = {
            'pretext_ru' : SummernoteWidget(),
            'pretext_en' : SummernoteWidget(),
        }
        fields = '__all__'

class CareerAdvantagesInline(admin.StackedInline):
    model = CareerAdvantages
    extra = 0

class CareerDemandsInline(admin.StackedInline):
    model = CareerDemands
    extra = 0

class CareerPageAdmin(TranslationAdmin):
    form = CareerPageForm
    inlines = (CareerAdvantagesInline, CareerDemandsInline,)


admin.site.register(Career, CareerPageAdmin)


# Documentation

class DocsInline(admin.StackedInline):
    model = Docs
    extra = 0

class DocumentationPageAdmin(admin.ModelAdmin):
    inlines = (DocsInline,)

admin.site.register(Documentation, DocumentationPageAdmin)


# ACtIVES

class ActivePageForm(forms.ModelForm):
    class Meta:
        model = Actives
        widgets = {
            'pretext_ru' : SummernoteWidget(),
            'pretext_en' : SummernoteWidget(),
        }
        fields = '__all__'

class ActivePageAdmin(TranslationAdmin):
    form = ActivePageForm
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'photo', 'pretext', )
        }),
        ('Первый блок', {
            'fields': ('block1_title', 'block1_subtitle', 'block1_text',)
        }),
        ('Второй блок', {
            'fields': ('block2_subtitle', 'block2_item1', 'block2_item2', 'block2_item3',)
        }),
        ('Третий блок', {
            'fields': ('block3_subtitle', 'block3_text',)
        }),
        ('Четвёртый блок', {
            'fields': ('block4_subtitle', 'block4_text',)
        }),
    )

admin.site.register(Actives, ActivePageAdmin)


# EXPERTISE

class ExpertisePageForm(forms.ModelForm):
    class Meta:
        model = Expertise
        widgets = {
            'pretext_ru' : SummernoteWidget(),
            'pretext_en' : SummernoteWidget(),
        }
        fields = '__all__'

class ExpertisePageAdmin(TranslationAdmin):
    form = ExpertisePageForm
    filter_horizontal = ('actions', )

admin.site.register(Expertise, ExpertisePageAdmin)


# PROJECTS
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        widgets = {
            'pretext_ru' : SummernoteWidget(),
            'pretext_en' : SummernoteWidget(),
        }
        fields = '__all__'

class ProjectInline(admin.StackedInline):
    model = ProjectItem
    extra = 0

class ProjectAdmin(TranslationAdmin):
    form = ProjectForm
    filter_horizontal = ('actions', 'industries',)
    inlines = (ProjectInline,)
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(ProjectPage)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Industry)


class ContactsAdmin(TranslationAdmin):
    pass
admin.site.register(Contacts, ContactsAdmin)

# NEWS

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        widgets = {
            'pretext_ru' : SummernoteWidget(),
            'text1_ru' : SummernoteWidget(attrs={'toolbar': [['style', ['bold','italic','clear']], ['para', ['ul', 'ol']],]}),
            'text2_ru' : SummernoteWidget(attrs={'toolbar': [['style', ['bold','italic','clear']], ['para', ['ul', 'ol']],]}),
            'pretext_en' : SummernoteWidget(),
            'text1_en' : SummernoteWidget(attrs={'toolbar': [['style', ['bold','italic','clear']], ['para', ['ul', 'ol']],]}),
            'text2_en' : SummernoteWidget(attrs={'toolbar': [['style', ['bold','italic','clear']], ['para', ['ul', 'ol']],]}),
        }
        fields = '__all__'


class NewsAdmin(TranslationAdmin):
    form = NewsForm

admin.site.register(NewsPage)
admin.site.register(News, NewsAdmin)
