#!/bin/bash

# Запрос ввода числа
read -p "Введите число: " number

# Проверка if
if [ "$number" -gt 0 ]; then
    echo "Число положительное."
    
    # Цикл while (считаем от 1 до number)
    echo "Считаем от 1 до $number:"
    count=1
    while [ $count -le "$number" ]; do
        echo $count
        ((count++))
    done

elif [ "$number" -lt 0 ]; then
    echo "Число отрицательное."
else
    echo "Число равно нулю."
fi
