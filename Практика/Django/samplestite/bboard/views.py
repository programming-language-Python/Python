from django.shortcuts import render
from django.http import HttpResponse
from .models import Bd
from django.template import loader
from .models import Rubric
# Create your views here.
def index(request):
    '''
    s = 'Список объявлений\r\n\r\n\r\n'
    # сортировка объявлений по убыванию
    for bb in Bd.objects.order_by('-published'):
# Список объявлений мы представили в виде обычного текста, разбитого на строки последоватнльности
# специальных символов возврата каретки (Возвра́т каре́тки — управляющий символ или механизм,
# используемый для возвращения позиции устройства к началу строки.
# Часто обозначается как CR (от англ. carriage return).) и перевода строки: \r\n
        s+= bb.title + '\r\n' + bb.content + '\r\n\r\n'
    return HttpResponse(s, content_type='text/plain; charset=utf-8')
    '''
    '''
# Сначало загружаем шаблон, воспользовавшись функцией get_template() из модуля django.template.loader.
# В качестве параметра мы указали строку с путем к файлу шаблона, отсчитанному от папки templates.
# Результатом, возвращенным функцией, станет экземпляр класса Template,
# представляющий хранящийся в заданном файле шаблон.
# Далее мы формируем контекст для нашего шаблона. Контекстом шаблона называется набор данных,
# которые должны быть доступны внутри шаблона в виде переменных и с которыми шаблонизатор
# объединит этот шаблон для получения выходного документа.
# это низко уровневый вариант записи:
    
    template = loader.get_template('bboard/index.html')
    bbs = Bd.objects.order_by('-published')
    context = {'bbs':bbs}
    return HttpResponse(template.render(context, request))
    '''
    '''
# Django предоставляет средства и более высокого уровня - функции-сокращения (shortcuts).
# В частности, функция-сокращение render () из модуля django.shortcuts позволяет выполнить
# рендеринг шаблона в одном выражении.
    # bbs = Bd.objects.order_by('-published') # можем убрать т.к. написано в models.py в class Meta ordering = ['-published']
    # и написать:
    bbs = Bd.objects.all()
    return render(request, 'bboard/index.html', {'bbs':bbs})
    '''
    bbs = Bd.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs':bbs,'rubrics':rubrics}
    return render(request, 'bboard/index.html', context)
def by_rubric(request, rubric_id):
    bbs = Bd.objects.filter (rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get (pk=rubric_id)
    context = {'bbs':bbs,'rubrics':rubrics,'current_rubric':current_rubric}
    return render(request,'bboard/by_rubric.html', context)

'''
Контроллер-класс мы сделали производным от класса CreateView из модуля
django.views.generic.edit. Базовый класс реализует функциональность по созданию
формы, выводу ее на экран с применением указанного шаблона, получению
занесенных в форму данных, проверке их на корректность, сохранению их в новой
записи модели и перенаправлению в случае успеха на интернет-адрес, который мы
зададим. Вот какой полезный класс этот CreateView!
Все необходимые сведения мы указали в атрибутах объявленного класса:
template_name- путь к файлу шаблона, ~по будет использован для вывода страницы
с формой;
form _ class - сам класс формы, связанной с моделью;
success_url- интернет-адрес, по которому будет выполнено перенаправление
после успешного сохранения данных (в нашем случае это адрес главной страницы).

Собственно, этим можно было бы и ограничиться. Но у нас на каждой странице, не
исключая и страницу добавления объявления, должна выводиться панель навигации,
содержащая список рубрик. Следовательно, нам нужно добавить в контекст
шаблона, формируемый классом CreateView, еще и этот список.
'''
from django.views.generic.edit import CreateView
from .forms import BdForm
# Функция reverse_lazy() из модуля django.urls в качестве параметров принимает
# имя маршруrа и значения всех входящих в маршруr URL-параметров (если они там есть).
# Результатом станет готовый интернет-адрес.
from django.urls import reverse_lazy
class BdCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BdForm
    success_url = reverse_lazy('index')
    '''
Метод get_context_data() этого класса формирует контекст шаблона. Мы переопределили
метод, чтобы добавить в контекст дополнительные данные - список
рубрик. В теле этого метода мы сначала получаем контекст шаблона от метода
базового класса, затем добавляем в него список рубрик и, наконец, возвращаем
в качестве результата.

**kwargs - Имя значения не имеет. Главное — это два символа **. Благодаря им создаётся словарь,
в котором содержатся именованные аргументы, переданные функции при её вызове.
    '''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

