# Функции

## Объявление функции
Функции объявляются с помощью ключевого слова `def` (от слова define – определять). За ключевым словом `def` следуют название функции, круглые скобки `()`, и двоеточие `:`.
```py
def название_функции():  # заголовком функции
    блок кода            # тело функции
```

Иногда, при объявлении функции требуется сделать своего рода заглушку, чтобы функция ничего не выполняла. Тогда мы используем ключевое слово `pass`: 
```py
def do_nothing():
    pass
```


## Вызов функции
Для вызова функции пишут ее название и круглые скобки.
```py
# создание функции:
def draw_box():  
    for _ in range(5):
        print('*' * 7)

# вызов функции:
draw_box()
```

## Именование функций
Python требует соблюдения тех же правил, что при именовании переменных:
- в имени функции используются только латинские буквы a-z, A-Z, цифры и символ нижнего подчеркивания (_);
- имя функции не может начинаться с цифры;
- имя функции по возможности должно отражать ее назначение;
- символы верхнего и нижнего регистра различаются. 

## Функции с параметрами
```py
def название_функции(параметры):
    блок кода
```

```py
def draw_box(height, width):    # функция принимает два параметра
    for i in range(height):
        print('*' * width)
```

## Параметры VS аргументы
**Аргумент** – это любая порция данных, которая передается в функцию, когда функция вызывается.  
**Параметр** – это переменная, которая получает аргумент, переданный в функцию. (Параметры функций часто называют параметрическими переменными)

Иногда вместо параметров и аргументов говорят о **формальных параметрах** и **фактических параметрах**:
- **Формальные параметры** – переменные, которые мы пишем при описании функции. 
- **Фактические параметры** – то, что реально подставляется при вызове функции.



## Области видимости переменных
**Локальными** называются переменные, объявленные внутри функции и доступные только ей самой. Программный код за пределами функции к ним доступа не имеет.

**Область действия переменной** – часть программы, в которой можно к ней обращаться, та функция, где она создана. Переменная видима только программному коду в области ее действия. Никакая инструкция за пределами функции не может обращаться к такой переменной.

**Область действия параметрической переменной** — функция, в которой этот параметр используется. К параметрической переменной имеет доступ весь программный код этой функции.

**Глобальными** называются переменные, объявленные в основной программе и доступные как программе, так и всем ее функциям.

## Ключевое слово global
Python предлагает ключевое слово global, которое используется для изменения значения глобальной переменной в функции. Оно нужно для изменения значения.  
 Правила использования global:
 - Если значение определено на выходе функции, то оно автоматически станет глобальной переменной.
 - Ключевое слово global используется для объявления глобальной переменной внутри функции.
 - Нет необходимости использовать global для объявления глобальной переменной вне функции.
 - Переменные, на которые есть ссылка внутри функции, неявно являются глобальными.
  
```py
def print_texas():
    global birds
    birds = 5000
    print('В Техасе обитает', birds, 'птиц.')

def print_california():
    print('В Калифорнии обитает', birds, 'птиц.')

print_texas()      # В Техасе обитает 5000 птиц.
print_california() # В Калифорнии обитает 5000 птиц.
```


## Функция с возвратом значения
Функция с возвратом значения имеет инструкцию `return`, возвращающую значение в ту часть программы,  которая ее вызвала.
Общий формат определения функции с возвратом значения в Python:

```py
def название_функции():
    блок кода
    return выражение
```

## Возвращение булевых значений
Python позволяет писать булевы функции, возвращающие либо истину (`True`), либо ложь (`False`). Булеву функцию можно применять для проверки условия, тогда значения `True` и `False` будут сигнализировать о его выполнении.

Булевы функции широко применяются для упрощения сложных условий, проверяемых в структурах принятия решения и структурах с повторением.


## Функции с возвратом нескольких значений
В Python функции не ограничены возвратом всего одного значения. После инструкции return можно определить много выражений, разделенных запятыми:
```py
return выражение 1, выражение 2, выражение 3 ...
```

