# Dataset: Books Collection

## Descriere
Acest dataset conține informații despre 100 de cărți populare din literatură mondială. Fiecare rând reprezintă o carte și include date despre autor, titlu, numărul de pagini și anul publicării. 

## Structura dataset-ului
Dataset-ul este stocat într-un fișier CSV cu următoarele coloane:

| Coloana           | Tip     | Descriere                                                      |
|-------------------|---------|----------------------------------------------------------------|
| `author_name`     | string  | Numele autorului                                               |
| `book_title`      | string  | Titlul complet al cărții                                       |
| `pages`           | int     | Numărul de pagini ale cărții                                   |
| `publishing_year` | int     | Anul publicării                                                |

## Exemple de date

| author_name             | book_title                                                       | pages | publishing_year|
|-------------------------|------------------------------------------------------------------|-------|----------------|
| Suzanne Collins         | The Hunger Games (The Hunger Games, #1)                          | 374   | 2008           |
| J.K. Rowling            | Harry Potter and the Order of the Phoenix (Harry Potter, #5)     | 912   | 2003           |
| Jane Austen             | Pride and Prejudice                                              | 279   | 1813           |
| Harper Lee              | To Kill a Mockingbird                                            | 323   | 1960           |
| Markus Zusak            | The Book Thief                                                   | 592   | 2005           |


## Surse
- Titlurile și autorii provin din colecții literare populare și liste de best-seller.

## Utilizare
Acest dataset poate fi utilizat pentru:
- Sistem de recomandare cărți
