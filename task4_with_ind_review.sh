#!/bin/bash

# Функция приветствия
greet() {
    echo "Hello, $1"
}

# Функция сложения
sum_numbers() {
    local result=$(($1 + $2))
    echo $result
}

# Демонстрация
echo "--- Вызов функции greet ---"
greet "Student"

echo "--- Вызов функции sum_numbers ---"
res=$(sum_numbers 10 25)
echo "Сумма 10 и 25 равна: $res"
