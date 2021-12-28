from ttkthemes import ThemedStyle
style = ThemedStyle()
# Style это класс для работы со стилями и темами. Именно этот класс надо использовать для конфигурирования внешнего вида виджетов.
# Основные методы класса:
# configure
# Конфигурирование внешнего вида виджетов. В качестве аргументов принимает название стиля виджета (например "TButton")
# и список опций конфигурирования. Пример:

# style.configure("TButton", padding=6, relief="flat", background="#ccc")

# map
# Конфигурирование внешнего вида виджетов в зависимости от их состояний (active, pressed, disabled и т.д.).
# В качестве аргументов принимает название стиля виджета и список опций конфигурирования, где опции представлены в виде списка.
# Пример:

style.map("TButton",
    foreground=[('pressed', 'red'), ('active', 'blue')],
    background=[('pressed', '!disabled', 'black'), ('active', 'white')]
    )

# lookup
# Возвращает соответствующую опцию конфигурирования. Пример:

# style.lookup("TButton", "font")

# layout
# Изменяет layout (схему) виджета. Виджеты ttk состоят из отдельных элементов, опций конфигурирования и других вложенных layouts.
# Следующий пример иллюстрирует применение метода layout:
'''
style.layout("TMenubutton", [
   ("Menubutton.background", None),
   ("Menubutton.button", {"children":
       [("Menubutton.focus", {"children":
           [("Menubutton.padding", {"children":
               [("Menubutton.label", {"side": "left", "expand": 1})]
           })]
       })]
   }),
])
'''
# element_create
# Создаёт новый элемент темы.

# element_names
# Возвращает список элементов текущей темы.

# element_options
# Возвращает список опций (конфигурацию), указанного в аргументе элемента.

# theme_create
# Создаёт новую тему. Аргументы те же, что и в theme_settings.

# theme_settings
# Конфигурирует существующую тему. Первый аргумент - название темы, второй аргумент - словарь,
# ключами которого являются названия стилей (TButton и т.п.), а значениями - layout соответствующего стиля.

# theme_names
# Возвращает список доступных тем.

# theme_use
# Изменяет текущую тему на указанную в аргументе.