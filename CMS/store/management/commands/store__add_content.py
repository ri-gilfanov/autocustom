from django.core.management.base import BaseCommand, CommandError
from ...models import Category, Product
from django.utils.text import slugify
from unidecode import unidecode
from random import uniform
from decimal import Decimal

class Command(BaseCommand):
    help = 'Импорт товаров, цен и остатков'

    def handle(self, *args, **options):
        name = 'Категория 1'
        category_1, created = Category.objects.update_or_create(
            pk=1,
            defaults={'name': name, 'slug': slugify(unidecode(name)), 'parent': None},
        )
        name = 'Категория 1-1'
        category_1_1, created = Category.objects.update_or_create(
            pk=2,
            defaults={'name': name, 'slug': slugify(unidecode(name)), 'parent': category_1},
        )
        name = 'Категория 1-2'
        category_1_2, created = Category.objects.update_or_create(
            pk=3,
            defaults={'name': name, 'slug': slugify(unidecode(name)), 'parent': category_1},
        )
        name = 'Категория 1-2-1'
        category_1_2_1, created = Category.objects.update_or_create(
            pk=4,
            defaults={'name': name, 'slug': slugify(unidecode(name)), 'parent': category_1_2},
        )
        name = 'Категория 1-2-2'
        category_1_2_2, created = Category.objects.update_or_create(
            pk=5,
            defaults={'name': name, 'slug': slugify(unidecode(name)), 'parent': category_1_2},
        )
        name = 'Категория 1-2-2-1'
        category_1_2_2_1, created = Category.objects.update_or_create(
            pk=6,
            defaults={'name': name, 'slug': slugify(unidecode(name)), 'parent': category_1_2_2},
        )
        name = 'Категория 1-2-2-2'
        category_1_2_2_2, created = Category.objects.update_or_create(
            pk=7,
            defaults={'name': name, 'slug': slugify(unidecode(name)), 'parent': category_1_2_2},
        )
        name = 'Автоаксессуары'
        avtoaksessuary, created = Category.objects.update_or_create(
            pk=8,
            defaults={'name': name, 'slug': slugify(unidecode(name)), 'parent': None},
        )
        name = 'Автозапчасти'
        avtozapchasti, created = Category.objects.update_or_create(
            pk=9,
            defaults={'name': name, 'slug': slugify(unidecode(name)), 'parent': None},
        )
        name = 'Внутренняя отделка / система безопасности'
        Category.objects.update_or_create(
            pk=10,
            defaults={'name': name, 'slug': slugify(unidecode(name)), 'parent': avtozapchasti},
        )
        name = 'Двигатель'
        Category.objects.update_or_create(
            pk=11,
            defaults={'name': name, 'slug': slugify(unidecode(name)), 'parent': avtozapchasti},
        )
        name = 'Коврики автомобильные'
        Category.objects.update_or_create(
            pk=12,
            defaults={'name': name, 'slug': slugify(unidecode(name)), 'parent': avtozapchasti},
        )
        name = 'Коробка передач'
        Category.objects.update_or_create(
            pk=13,
            defaults={'name': name, 'slug': slugify(unidecode(name)), 'parent': avtozapchasti},
        )
        name = 'Кузов'
        Category.objects.update_or_create(
            pk=14,
            defaults={'name': name, 'slug': slugify(unidecode(name)), 'parent': avtozapchasti},
        )
        name = 'Отопление / вентиляция / кондиционирование'
        Category.objects.update_or_create(
            pk=15,
            defaults={'name': name, 'slug': slugify(unidecode(name)), 'parent': avtozapchasti},
        )
        name = 'Подвеска / амортизация / рулевое управление'
        Category.objects.update_or_create(
            pk=16,
            defaults={'name': name, 'slug': slugify(unidecode(name)), 'parent': avtozapchasti},
        )
        name = 'Привод колеса'
        Category.objects.update_or_create(
            pk=17,
            defaults={'name': name, 'slug': slugify(unidecode(name)), 'parent': avtozapchasti},
        )
        name = 'Ремни'
        Category.objects.update_or_create(
            pk=18,
            defaults={'name': name, 'slug': slugify(unidecode(name)), 'parent': avtozapchasti},
        )
        name = 'Система выпуска'
        Category.objects.update_or_create(
            pk=19,
            defaults={'name': name, 'slug': slugify(unidecode(name)), 'parent': avtozapchasti},
        )
        name = 'Система охлаждения'
        Category.objects.update_or_create(
            pk=20,
            defaults={'name': name, 'slug': slugify(unidecode(name)), 'parent': avtozapchasti},
        )
        name = 'Система сцепления'
        Category.objects.update_or_create(
            pk=21,
            defaults={'name': name, 'slug': slugify(unidecode(name)), 'parent': avtozapchasti},
        )
        name = 'Топливная система'
        Category.objects.update_or_create(
            pk=22,
            defaults={'name': name, 'slug': slugify(unidecode(name)), 'parent': avtozapchasti},
        )
        name = 'Тормозная система'
        Category.objects.update_or_create(
            pk=23,
            defaults={'name': name, 'slug': slugify(unidecode(name)), 'parent': avtozapchasti},
        )
        name = 'Фары и свет'
        Category.objects.update_or_create(
            pk=24,
            defaults={'name': name, 'slug': slugify(unidecode(name)), 'parent': avtozapchasti},
        )
        name = 'Электрика'
        Category.objects.update_or_create(
            pk=25,
            defaults={'name': name, 'slug': slugify(unidecode(name)), 'parent': avtozapchasti},
        )
        name = 'Автосвет'
        avtosvet, created = Category.objects.update_or_create(
            pk=26,
            defaults={'name': name, 'slug': slugify(unidecode(name)), 'parent': None},
        )
        pk = 0
        avtoaksessuary_products = [
            'Airlaine Огнетушитель порошковый ОП1 АО-ОР1',
            'JM-FS48 к-кт проводов / Ford Fiesta/',
            'ST7121-10 Перчатки латексные хозяйственные размер №10',
            'USB-адаптер гнезда прикуривателя',
            'Автокипятильник Alco 2V',
            'Брелок в ассортименте',
            'Детское удерживающее устройство от 22-36кг группа 3 (6-12лет)',
            'Домкрат гидравлический телескопический AUTOPROFI 2тн',
            'Домкрат гидравлический телескопический AUTOPROFI 4тн',
            'Домкрат гидравлический телескопический AUTOPROFI 6тн',
            'Домкрат гидравлический телескопический AUTOPROFI 8тн',
            'Защитная накладка заднего бампера Hyundai (IX35/Solaris)',
            'Изолента синяя 15мм*10м SafeLine',
            'Изолента синяя 19мм*20м SafeLine',
            'Изолента черная 15мм*10м SafeLine',
            'Изолента черная 19мм*20м SafeLine',
            'Изолента черная 19мм*20м Terminator',
            'Изолента черная 19мм*25м Neomatec',
            'Канистра стальная оцинкованная AUTOPROFI 5л',
            'Клещи для снятия изоляции',
            'Ключ свечной Airline (гаечный торцевой) 16*21',
            'Комплект плавких автомобильных предохранителей SCT',
            'Компрессор воздушный "АГРЕССОР" 50л/мин',
            'Компрессор воздушный "АГРЕССОР" 75л/мин',
            'Компрессор воздушный AUTOPROFI 35л/мин',
            'Крючки на подголовник',
            'Лапата саперная большая AIRLINE 60см',
            'Лапата саперная маленькая AIRLINE',
            'Набор для ремонта бескамерных шин',
            'Набор ключей TORX стандартные',
            'Набор шестигранников L-образных',
            'Накладки порогов Elegance Chevrolet Aveo Dollex',
            'Накладки порогов Elegance Chevrolet Cruze (<-2013) Dollex',
            'Накладки порогов Elegance Chevrolet Cruze Dollex',
            'Накладки порогов Elegance Mazda 3 Dollex',
            'Накладки порогов Elegance Nissan Qashqai Dollex',
            'Накладки порогов Elegance VW Polo Dollex',
            'Накладки порогов Elegance ВАЗ-2170, 21104, 21124 Dollex',
            'Наклейка автомобильная "Дьявол"',
            'Наклейка автомобильная "Крылья"',
            'Наклейка знак ш',
            'Наклейка на присоске "Ребенок в машине"',
            'Наклейка на стекло "Держи дистанцию"',
            'Наклейка на стекло "За рулем шумахер"',
            'Наклейка на стекло "Каблук"',
            'Наклейка на стекло "Мужик за рулем"',
            'Насос ручной для перекачки ГСМ/SCT 9316',
            'Отвертка с трещеткой',
            'Парковочный радар SVS LED 013-4 4 датчика Черный',
            'Перчатки х/б с покрытием ПВХ размер 9 (7,5 класс вязки, 4 нити)',
            'Провода прикуривания Alligator -40C 400amp 2,5м',
            'Провода прикуривания Alligator -40C 600amp 3м',
            'Разветвитель-удленитель на 3 гензда прикуривателя с USB-портом',
            'Рамка номерного знака (Камуфляж) Airline',
            'Рамка номерного знака (Карбон) Airline',
            'Рамка номерного знака Dollex',
            'Рамка номерного знака Dollex антивандальная',
            'Рамка номерного знака декоративная',
            'Рамка номерного знака круглая Dollex антивандальная из нержавеющей стали',
            'Сабвуфер Graund Zero GZTB-300BR',
            'Салфетки в тубе CityUP 40*32 синтетическая замшевая с термическим тиснением',
            'Салфетки в тубе замшевые Kanebo 43*32',
            'Салфетки в тубе замшевые Kanebo 68*43',
            'Салфетки для кожанных салонов с натуральным воском IVF 10шт.',
            'Салфетки для рук HG 20шт.',
            'Трос буксировочный эластичный AUTOPROFI 2тн',
            'Трос буксировочный эластичный AUTOPROFI 3тн',
            'Шторки каркасные Toyota Camry V40 комплект 2шт.',
            'Щетка для снега со скребком распущенная щетина STARTUL 84см',
            'Щетка с водосгоном телескопическая STARTUL 58-96x24см'
        ]
        for name in avtoaksessuary_products:
            pk += 1
            Product.objects.update_or_create(
                pk=pk,
                defaults={'name': name, 'slug': slugify(unidecode(name)), 'category': avtoaksessuary, 'base_price': Decimal(uniform(250, 50000))}
            )
        for category in Category.objects.exclude(pk=8):
            if not category.get_children().exists():
                for i in range(1, 20):
                    pk += 1
                    name = 'товар {0}'.format(pk)
                    Product.objects.update_or_create(
                        pk=pk,
                        defaults={'name': name, 'slug': slugify(unidecode(name)), 'category': category, 'base_price': Decimal(uniform(250, 50000))}
                    )
        self.stdout.write(self.style.SUCCESS('Категории созданы'))
