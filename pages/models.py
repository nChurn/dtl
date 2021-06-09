from django.db import models
from proxima.utils.models import PathRename


# Главная

class MainPage(models.Model):

    first_subtext = models.CharField(max_length=300, verbose_name='Подзаголовок слайда')
    second_text = models.TextField(verbose_name='Заголовок слайда')
    second_subtext = models.CharField(max_length=300, verbose_name='Текст справа от кнопки')
    third_text = models.TextField(verbose_name='Заголовок слайда')
    third_bg = models.ImageField(upload_to=PathRename('mainpage'), verbose_name='Фоновое изображение')
    third_bg_mobile = models.ImageField(upload_to=PathRename('mainpage'), verbose_name='Фоновое изображение для адаптива')
    fourth_text = models.TextField(verbose_name='Заголовок слайда')

    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = ' 1. Главная страница'

    def __str__(self):
        return 'Главная страница'


class MainPageLogo(models.Model):
    page = models.ForeignKey(MainPage, verbose_name='Главная страница')
    logo_img = models.ImageField(upload_to=PathRename('mainpage/logos'), verbose_name='Изображение')
    position = models.CharField(max_length=10, verbose_name='Позиция', default=1)

    class Meta:
        ordering = ('position',)
        verbose_name = 'Логотип на главной'
        verbose_name_plural = 'Логотипы на главной'

    def __str__(self):
        return 'Логотип на главной'


# О компании

class About(models.Model):

    title = models.CharField(max_length=40, verbose_name='Заголовок страницы')
    photo = models.ImageField(upload_to=PathRename('about'), verbose_name='Фото под заголовком')
    block1_pretext = models.TextField(verbose_name='Текст цитаты')
    block1_text = models.TextField(verbose_name='Основной текст')
    block2_title = models.CharField(max_length=300, verbose_name='Заголовок')
    block2_text = models.TextField(verbose_name='Основной текст')
    block2_quote = models.TextField(verbose_name='Текст цитаты')
    block2_text2 = models.TextField(verbose_name='Основной текст 2')
    block3_title = models.CharField(max_length=300, verbose_name='Заголовок')
    block3_text = models.TextField(verbose_name='Основной текст')
    block4_title = models.CharField(max_length=300, verbose_name='Заголовок')
    block4_subtitle1 = models.CharField(max_length=300, verbose_name='Первый подзаголовок')
    block4_item1 = models.TextField(verbose_name='Текст пункта 1')
    block4_item2 = models.TextField(verbose_name='Текст пункта 2', blank=True)
    block4_subtitle2 = models.CharField(max_length=300, verbose_name='Второй подзаголовок')
    block4_item3 = models.TextField(verbose_name='Текст пункта 3')
    block4_item4 = models.TextField(verbose_name='Текст пункта 4', blank=True)

    class Meta:
        verbose_name = 'О компании'
        verbose_name_plural = ' 2. О компании'

    def __str__(self):
        return 'О компании'


# Команда

class ActionDirection(models.Model):
    position = models.CharField(max_length=10, verbose_name='Позиция', default=1)
    title = models.CharField(max_length=200, verbose_name='Название')
    photo = models.ImageField(upload_to=PathRename('directions'), verbose_name='Фото под заголовком')
    pretext = models.TextField(verbose_name='Текст цитаты')
    text = models.TextField(verbose_name='Основной текст')
    subtitle = models.CharField(max_length=300, verbose_name='Подзаголовок')


    class Meta:
        ordering = ('position',)
        verbose_name = 'Направление деятельности'
        verbose_name_plural = '10. Направления деятельности'

    def __str__(self):
        return self.title

class ActionDirectionItems(models.Model):
    page = models.ForeignKey(ActionDirection)
    position = models.CharField(max_length=10, verbose_name='Позиция', default=1)
    text = models.TextField(verbose_name='Текст')

    class Meta:
        ordering = ('position',)
        verbose_name = 'Пункт'
        verbose_name_plural = 'Пункты'


class Person(models.Model):
    photo = models.ImageField(upload_to=PathRename('team'), verbose_name='Фото превью', blank=True)
    slug = models.SlugField(blank=True)
    name = models.CharField(max_length=200, verbose_name='Имя и фамилия')
    job = models.CharField(max_length=200, verbose_name='Должность')
    main_photo = models.ImageField(upload_to=PathRename('team'), verbose_name='Основное фото', blank=True)
    pretext = models.TextField(verbose_name='Текст цитаты')
    actions = models.ManyToManyField(ActionDirection, blank=True)
    position = models.CharField(max_length=10, verbose_name='Позиция', default=1)

    class Meta:
        ordering = ('position',)
        verbose_name = 'Сотрудник'
        verbose_name_plural = ' 4. Сотрудники'

    def __str__(self):
        return self.name

class PersonBio(models.Model):
    position = models.CharField(max_length=10, verbose_name='Позиция', default=1)
    person = models.ForeignKey(Person, verbose_name='Сотрудник')
    period = models.CharField(max_length=200, verbose_name='Период', blank=True)
    text = models.TextField(verbose_name='Текст')

    class Meta:
        ordering = ('position',)
        verbose_name = 'Пункт биографии'
        verbose_name_plural = 'Пункты биографии'


class Team(models.Model):

    title = models.CharField(max_length=40, verbose_name='Заголовок страницы')
    photo = models.ImageField(upload_to=PathRename('team'), verbose_name='Фото под заголовком')
    pretext = models.TextField(verbose_name='Текст цитаты')
    people = models.ManyToManyField(Person, blank=True)

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = ' 3. Команда'

    def __str__(self):
        return 'Команда'

# Карьера

class Career(models.Model):

    title = models.CharField(max_length=40, verbose_name='Заголовок страницы')
    photo = models.ImageField(upload_to=PathRename('career'), verbose_name='Фото под заголовком')
    pretext = models.TextField(verbose_name='Текст цитаты')
    specialists_text = models.TextField(verbose_name='Текст «Специалистам»')
    students_text = models.TextField(verbose_name='Текст «Студентам»')


    class Meta:
        verbose_name = 'Карьера'
        verbose_name_plural = ' 5. Карьера'

    def __str__(self):
        return 'Карьера'

class CareerAdvantages(models.Model):
    page = models.ForeignKey(Career, verbose_name='Страница')
    position = models.CharField(max_length=10, verbose_name='Позиция', default=1)
    text = models.TextField(verbose_name='Текст')

    class Meta:
        ordering = ('position',)
        verbose_name = 'Приемущество'
        verbose_name_plural = 'Приемущества'

class CareerDemands(models.Model):
    page = models.ForeignKey(Career, verbose_name='Страница')
    position = models.CharField(max_length=10, verbose_name='Позиция', default=1)
    text = models.TextField(verbose_name='Текст')

    class Meta:
        ordering = ('position',)
        verbose_name = 'Требование'
        verbose_name_plural = 'Требования'


class Resume(models.Model):

    TYPE_CHOICES = (
        ('sp', 'Специалистам'),
        ('st', 'Студентам'),
    )

    type = models.CharField(max_length=2, choices=TYPE_CHOICES, default='sp', verbose_name='Тип')
    name = models.CharField(max_length=200, verbose_name='ФИО')
    email = models.CharField(max_length=200, verbose_name='Email')
    file = models.FileField(upload_to=PathRename('resume'), verbose_name='Файл', blank=True)

    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = ' 6. Резюме'

    def __str__(self):
        return self.name

# Документация

class Documentation(models.Model):

    title = models.CharField(max_length=40, verbose_name='Заголовок страницы')
    photo = models.ImageField(upload_to=PathRename('career'), verbose_name='Фото под заголовком')

    class Meta:
        verbose_name = 'Документация'
        verbose_name_plural = ' 7. Документация'

    def __str__(self):
        return 'Документация'

class Docs(models.Model):
    page = models.ForeignKey(Documentation, verbose_name='Страница')
    title = models.CharField(max_length=140, verbose_name='Название')
    file = models.FileField(upload_to=PathRename('docs'), verbose_name='Файл')
    position = models.CharField(max_length=10, verbose_name='Позиция', default=1)

    def size(self):
        return round(self.file.size / 1024 / 1024, 2)

    def extention(self):
        return self.file.url.split('.')[-1]

    class Meta:
        ordering = ('position',)
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'


# Активы

class Actives(models.Model):

    title = models.CharField(max_length=40, verbose_name='Заголовок страницы')
    photo = models.ImageField(upload_to=PathRename('career'), verbose_name='Фото под заголовком')
    pretext = models.TextField(verbose_name='Текст цитаты')
    block1_title = models.CharField(max_length=300, verbose_name='Заголовок')
    block1_subtitle = models.CharField(max_length=300, verbose_name='Подзаголовок')
    block1_text = models.TextField(verbose_name='Текст')
    block2_subtitle = models.CharField(max_length=300, verbose_name='Подзаголовок')
    block2_item1 = models.TextField(verbose_name='Текст пункта 1')
    block2_item2 = models.TextField(verbose_name='Текст пункта 2')
    block2_item3 = models.TextField(verbose_name='Текст пункта 3')
    block3_subtitle = models.CharField(max_length=300, verbose_name='Подзаголовок')
    block3_text = models.TextField(verbose_name='Текст')
    block4_subtitle = models.CharField(max_length=300, verbose_name='Подзаголовок', blank=True)
    block4_text = models.TextField(verbose_name='Текст', blank=True)


    class Meta:
        verbose_name = 'Активы'
        verbose_name_plural = ' 8. Активы'

    def __str__(self):
        return 'Активы'

# Экспертиза

class Expertise(models.Model):

    title = models.CharField(max_length=240, verbose_name='Заголовок страницы')
    photo = models.ImageField(upload_to=PathRename('expertise'), verbose_name='Фото под заголовком')
    pretext = models.TextField(verbose_name='Текст цитаты')
    actions = models.ManyToManyField(ActionDirection, blank=True)

    class Meta:
        verbose_name = 'Экспертиза'
        verbose_name_plural = ' 9. Экспертиза'

    def __str__(self):
        return 'Экспертиза'

# Активы

class Industry(models.Model):
    position = models.CharField(max_length=10, verbose_name='Позиция', default=1)
    title = models.CharField(max_length=200, verbose_name='Название отрасли')

    class Meta:
        ordering = ('position',)
        verbose_name = 'Отрасль'
        verbose_name_plural = '13. Отрасли'

    def __str__(self):
        return self.title

class Project(models.Model):
    client = models.CharField(max_length=100, verbose_name='Клиент')
    title = models.CharField(max_length=350, verbose_name='Название')
    title_preview = models.CharField(max_length=350, verbose_name='Название в превью', blank=True)
    slug = models.SlugField(blank=True)
    logo = models.ImageField(upload_to=PathRename('projects/logos'), verbose_name='Лого на превью')
    photo = models.ImageField(upload_to=PathRename('projects/previews'), verbose_name='Фото на ховере превью')
    is_active = models.BooleanField(verbose_name='Является ли активом?', default=False)
    is_end = models.BooleanField(verbose_name='Завершен?', default=False)
    position = models.CharField(max_length=10, verbose_name='Позиция', default=1)
    actions = models.ManyToManyField(ActionDirection, blank=True)
    industries = models.ManyToManyField(Industry, blank=True)
    logo_head = models.ImageField(upload_to=PathRename('projects/logos'), verbose_name='Лого в шапке')
    photo_head = models.ImageField(upload_to=PathRename('projects/photos'), verbose_name='Фото в шапке')
    inv = models.CharField(max_length=15, verbose_name='Инвестиции PCG')
    inv_text = models.CharField(max_length=150, verbose_name='Инвестиции PCG текст', blank=True)
    per = models.CharField(max_length=30, verbose_name='Период реализации')
    per_text = models.CharField(max_length=150, verbose_name='Период реализации текст', blank=True)
    geo = models.CharField(max_length=15, verbose_name='География проекта')
    geo_text = models.CharField(max_length=150, verbose_name='География проекта текст', blank=True)
    pretext = models.TextField(verbose_name='Текст цитаты')
    text = models.TextField(verbose_name='Текст основной')
    subtitle = models.CharField(max_length=300, verbose_name='Подзаголовок')

    class Meta:
        ordering = ('position',)
        verbose_name = 'Проект'
        verbose_name_plural = '12. Проекты'

    def __str__(self):
        return self.title

class ProjectPage(models.Model):

    title = models.CharField(max_length=200, verbose_name='Заголовок страницы')
    photo = models.ImageField(upload_to=PathRename('projects'), verbose_name='Фото под заголовком')

    class Meta:
        verbose_name = 'Страница проектов'
        verbose_name_plural = '11. Страница проектов'

    def __str__(self):
        return 'Страница проектов'

class ProjectItem(models.Model):
    page = models.ForeignKey(Project, verbose_name='Проект')
    position = models.CharField(max_length=10, verbose_name='Позиция', default=1)
    text = models.TextField(verbose_name='Текст основной')

    class Meta:
        ordering = ('position',)
        verbose_name = 'Пункт'
        verbose_name_plural = 'Пункты'

# Новости


class NewsPage(models.Model):

    title = models.CharField(max_length=40, verbose_name='Заголовок страницы')
    photo = models.ImageField(upload_to=PathRename('projects'), verbose_name='Фото под заголовком')

    class Meta:
        verbose_name = 'Страница новостей'
        verbose_name_plural = '14. Страница новостей'

    def __str__(self):
        return 'Страница новостей'

class News(models.Model):

    CATEGORY_CHOICES = (
        ('n', 'Новости'),
        ('a', 'Аналитические и экспертные материалы'),
    )

    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES, default='n', verbose_name='Категория')
    title = models.CharField(max_length=240, verbose_name='Название')
    photo = models.ImageField(upload_to=PathRename('news/previews'),
    verbose_name='Фото на ховере превью',blank=True)
    date = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name='Дата')
    pretext = models.TextField(verbose_name='Текст цитаты', blank=True)
    text = models.TextField(verbose_name='Основной текст', blank=True)
    photo1 = models.ImageField(upload_to=PathRename('news/photos'), verbose_name='Фото', blank=True)
    subtitle1 = models.CharField(max_length=300, verbose_name='Подзаголовок 1', blank=True)
    text1 = models.TextField(verbose_name='Текст 1', blank=True)
    subtitle2 = models.CharField(max_length=300, verbose_name='Подзаголовок 2', blank=True)
    text2 = models.TextField(verbose_name='Текст 2', blank=True)
    link = models.CharField(max_length=300, verbose_name='Ссылка (для ссылки на внутренние страницы надо начинать с "/")', blank=True)
    subtitle3 = models.CharField(max_length=300, verbose_name='Подзаголовок 3', blank=True)
    button_text = models.CharField(max_length=100, verbose_name='Текст на кнопке', blank=True)


    class Meta:
        ordering = ('-date',)
        verbose_name = 'Новость'
        verbose_name_plural = '15. Новости'

    def __str__(self):
        return self.title

    def get_year(self):
        return self.date.year


# Контакты

class Contacts(models.Model):
    title = models.CharField(max_length=40, verbose_name='Заголовок страницы')
    address = models.CharField(max_length=120, verbose_name='Адрес')
    phone = models.CharField(max_length=90, verbose_name='Телефон')
    email = models.CharField(max_length=90, verbose_name='E-mail')
    lat = models.CharField(max_length=40, verbose_name='Координата широты')
    lng = models.CharField(max_length=40, verbose_name='Координата долготы')

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = '16. Контакты'

    def __str__(self):
        return 'Контакты'
