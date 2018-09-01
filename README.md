# Отчёт
Для оценки улучшения быстродействия был запущен скрипт ***task_3_tester.py***, который фиксирует время инициализации, затем посылает 10 собщений, ожидает и   фиксирует время ответа. Для наглядности все 10 сообщений содержали число 75000, взятие факториала от этого числа - заведомо долгая операция. Результаты тестов приведены в таблице; видно, что многопоточная реализация позволяет улучшить результаты более чем в два раза.

Затем аналогичные тесты были проведены для чисел 100 и 150000.

 Msg     |  N of workers  |  N of packages  |  Init time           |  Finish time         |  Overall time 
 ------  |  ------------  |  -------------  |  ------------------  |  ------------------  |  ------------ 
 75000   |  1             |  10             |  1535838688.15093    |  1535838712.88457    |  24.73363996  
 75000   |  5             |  10             |  1535839007.03864    |  1535839018.12669    |  11.08804989  
 75000   |  10            |  10             |  1535839086.20633    |  1535839093.86074    |  7.654409885  
 150000  |  5             |  10             |  1535841234.7742994  |  1535841321.35584    |  86.58154988  
 150000  |  10            |  10             |  1535841113.26905    |  1535841168.89178    |  55.62273002  
 100     |  1             |  10             |  1535841460.2974412  |  1535841460.326346   |  0.02889990807
 100     |  10            |  10             |  1535841531.7132382  |  1535841531.7767572  |  0.0635201931 

### 1 worker
![1 worker](https://github.com/EgorOs/osinkin_hw9/blob/master/pictures/1_worker.png)

### 5 workers
![5 workers](https://github.com/EgorOs/osinkin_hw9/blob/master/pictures/1_worker.png)

### 10 workers
![10 workers](https://github.com/EgorOs/osinkin_hw9/blob/master/pictures/1_worker.png)
