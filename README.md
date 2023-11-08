В качестве источника данных у вас есть созданный сотрудником компании excel-файл case03_input_file.xlsx, содержащий в себе коэффициент эффективности партнёрской сети в стандартной для всех партнеров объемов продаж.

К сожалению, данные в файле структурированы не самым оптимальным для загрузки в hdfs образом.  См. лист data.

Описание файла:
1.	Размер таблиц всегда одинаковый (9 строк, 9 столбцов).
2.	В одном файле содержится только один лист с данными и в нем может быть более 10 000 таблиц.
3.	Таблицы всегда разделены пустой строкой. 
4.	Значения «диапазон», всегда одинаковы: 0 – 10, 100 – 500, 500 - 1 000, 1 000 - 5 000, 5 000 - 10 000, 10 000 - 100 000, > 100 000
5.	Название региона, всегда содержится в первой строке – в первом столбце таблицы

Ваша задача - написать скрипт обработки данного файла с использованием языка Python (3.х). Результатом обработки должен быть csv файл, состоящий из следующих столбцов:

1.	File_Name
2.	Region
3.	Partner
4.	Range,Value

Имена столбцов должны содержаться в первой строке файла. Пример см. на листе «Result».

Требования к результату:
В качестве результата ожидается файл <Фамилия Имя Отчество>_task03.py,  в котором будет содержаться код с краткими комментариями