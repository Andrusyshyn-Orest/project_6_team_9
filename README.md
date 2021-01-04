Тема проекту: 6. Аналіз відношень.
Команда: Бодаковський Юрій, Андрусишин Орест, Брик Богдан, Гентош Петро, Хімка Вікторія.

Проект складається з таких модулів:

**read_and_write.py** - складається з функцій, які забезпучують читання
відношень з файлу і запис відношень у файл.
read_file - читає відношення з файлу
Функція приймає шлях до файлу в якому записане відношення у вигляді
матриці n x n; повертає це відношення як множину кортежів і n.
write_file - записує відношення у файл
Функція приймає відношення у вигляді множини кортежів,
n (n x n матриця), шлях куди записати відношення. Функція записує
відношення по заданому шляху.


**closures.py** - складається з функцій, які використовуються
для знаходження замикань відношення. 
transform_relation_into_matrix - функція приймає відношення як множину
кортежів і розмір матриці; повертає матрицю як список списків на основі
цього відношення.
transform_matrix_into_relation - приймає матрицю як список списків і
повертає відношення як множину кортежів на основі цієї матриці.
find_transitive_closure приймає відношення як множину кортежів і розмір
матриці; повертає транзитивне замикання цього відношення як множину
кортежів.
reflexive_closure - шукає рефлексивне замикання.
Функція приймає відношення, n (n x n матриця) і шлях до файлу (якщо
не даний, то пустий стрінг); повертає рефлексивне замикання даного
відношення і якщо був вказаний шлях, то записує відповідь у цей файл
symmetric_closure - шукає симетричне замикання. Функція приймає
відношення, n (n x n матриця) і шлях до файлу (якщо не даний, то
пустий стрінг); повертає симетричне замикання даного відношення і якщо
був вказаний шлях, то записує відповідь у цей файл


**equivalence_classes.py** - складається з функції, яка працює на
визначення класів еквівалентності відношення еквівалентності.
find_classes - повертає класи еквівалентності
Функція приймає віношення і n (n x n матриця); повертає класи
еквівалентності у вигляді списку списку, де кожен список це клас
еквівалентності.


**transitive.py** - складається з функцій які досліджують транзитивність
відношень.
check_if_transitive приймає відношення як множину кортежів і повертає
булеве значення (True, якщо відношення транзитивне і False в
протилежному випадку).
find_number_of_transitives приймає розмір множини як ціле число і
повертає кількість усіх можливих транзитивних відношень на множині
такого розміру. 


**main.py** - основний модуль проекту. Містить функцію main, яка
запускає програму.


Використані принципи дискретної математики:
1) Алгоритми побудови рефлексивного, симетричного і транзитивного
замикань (Алгоритм Воршалла).
2) Поняття класів еквівалентності відношення еквівалентності. 


Процес виконання проекту:

30.12.2020 - Обговорення проекту і розподіл обов'язків по виконанню
проекту в онлайн режимі.
02.01.2021 і 03.01.2021 - написання модулів проекту.
04.01.2021 - тестування проекту і написання звіту.

Розподіл роботи в команді:
Бодаковський Юрій - модулі equivalence_classes.py, main.py;
Андрусишин Орест - модуль transitive.py;
Брик Богдан - функції transform_relation_into_matrix,
transform_matrix_into_relation, find_transitive_closure
модуля closures.py;
Вікторія Хімка - функції reflexive_closure, symmetric_closure модуля
closures.py;
Гентош Петро - модуль read_and_write.py.


Запуск проекту:
Програма запускається з теки, у якій знаходяться модулі програми,
запусканням модуля main.py


Враження від виконання та фідбек викладачам та асистентам:
Дуже корисний досвід роботи в команді. Ми навчилися ефективно
розподіляти обов'язки між усіма її членами для досягнення хорошого
результату. Дякуємо викладачам та асистентам за цікаві теми для
проектів і своєчасні відповіді на усі питання, які виникали.

 

