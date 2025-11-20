#Перед запуском необходимо создать файл input.txt

#!/bin/bash

# Создадим input.txt для теста, если его нет
if [ ! -f input.txt ]; then
    echo "Hello World" > input.txt
    echo "Bash scripting is fun" >> input.txt
    echo "Line 3" >> input.txt
fi

# 1. Читаем данные
echo "--- Чтение из input.txt ---"
cat input.txt

# 2. Перенаправляем wc -l в output.txt
# (< читает из файла, > пишет в файл)
wc -l < input.txt > output.txt
echo "--- Результат wc -l записан в output.txt ---"

# 3. Ошибка ls в error.log
# (2> перенаправляет поток ошибок stderr)
ls non_existent_file_123 2> error.log
echo "--- Ошибка команды ls записана в error.log ---"
