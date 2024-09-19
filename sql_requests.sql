/*1 Выведите все уникальные названия продуктов.*/
SELECT DISTINCT product_name 
FROM products;

/*2 Выведите id, название и стоимость 
продуктов с содержанием клетчатки (fiber) 
более 5 граммов.*/
SELECT p.product_id, p.product_name, p.price
FROM products AS p
JOIN nutritional_information AS n
ON p.product_id=n.product_id
WHERE fiber > 5
/*Уточнение: "более 5 граммов" будет ли число 5
входить в поиск или нет? Если да, то требуется:
WHERE fiber >= 5
*/

/*3 Выведите название продукта 
с самым высоким содержанием белка (protein).*/
SELECT p.product_name
FROM products AS p
JOIN nutritional_information AS n
ON p.product_id=n.product_id
WHERE protein=(SELECT MAX(protein) FROM nutritional_information);

/*4 Подсчитайте общую сумму калорий 
для продуктов каждой категории, 
но не учитывайте продукты с нулевым жиром (fat = 0). 
Выведите id категории, сумму калорий.*/
SELECT p.category_id, SUM(p.calories)
FROM products AS p
JOIN nutritional_information AS n
ON p.product_id=n.product_id
WHERE n.fat is not null
GROUP BY category_id

/*5 Рассчитайте среднюю цену товаров каждой категории. 
Выведите название категории, среднюю цену.*/
SELECT c.category_name, ROUND(AVG(p.price)::numeric, 2)
FROM categories AS c
RIGHT JOIN products AS p
ON c.category_id=p.category_id
GROUP BY category_name