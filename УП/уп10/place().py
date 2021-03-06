# place представляет собой простой упаковщик, позволяющий размещать виджет в фиксированном месте с фиксированным размером.
# Также он позволяет указывать координаты размещения в относительных единицах для реализации "резинового" размещения.
# При использовании этого упаковщика, нам необходимо указывать координаты каждого виджета. Например:

# button1.place(x=0,y=0)
# Этот упаковщик, хоть и кажется неудобным, предоставляет полную свободу в размещении виджетов на окне.

# Аргументы
# anchor ("n", "s", "e", "w", "ne", "nw", "se", "sw" или "center") - какой угол или сторона размещаемого виджета будет указана
# в аргументах x/y/relx/rely. По умолчанию "nw" - левый верхний
# bordermode ("inside", "outside", "ignore") - определяет в какой степени будут учитываться границы при размещении виджета.
# in_ - явное указание в какой родительский виджет должен быть помещён.
# x и y - абсолютные координаты (в пикселях) размещения виджета.
# width и height - абсолютные ширина и высота виджета.
# relx и rely - относительные координаты (от 0.0 до 1.0) размещения виджета.
# relwidth и relheight - относительные ширина и высота виджета.
# Относительные и абсолютные координаты (а также ширину и высоту) можно комбинировать.
# Так например, relx=0.5, x=-2 означает размещение виджета в двух пикселях слева от центра родительского виджета,
# relheight=1.0, height=-2 - высота виджета на два пикселя меньше высоты родительского виджета.

# Дополнительные функции
# place_slaves, place_forget, place_info - см. описание аналогичных методов упаковщика pack.