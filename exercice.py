#!/usr/bin/env python
# -*- coding: utf-8 -*-



def order(values: list = None) -> bool:
    if values is None:
        values = [input("Veuillez entre une valeur") for _ in range(10)]


    return sorted(values) == values
#marche pas avec des entier, il faut mettre un key particulier



def anagrams(words: list = None) -> bool:
    if words is None:
        mot1, mot2 = input("ecrire un mot"), input("ecrire un mot")
        liste1, liste2 = list(mot1), list(mot2)

    return sorted(liste1) == sorted(liste2)

def anagrams2(words: list = None) -> bool:
    if words is None:
        words = [input() for _ in range(2)]

    sorted_words = set()
    for word in words:
        set(word)
        sorted_words.add(sorted(str(word)))

    return len(sorted_words) == 1


def anagrams3(words: list = None) -> bool:
    if words is None:
        words = [input() for _ in range(2)]
    word_dicts = [{}, {}]
    for i, word in enumerate(words):
        for letter in word:
            if letter in word_dicts[1]:
                word_dicts[i][letter] += 1
            else: word_dicts[i][letter] = 1

    return word_dicts[0] == word_dicts[1]




def contains_doubles(items: list) -> bool:
    unique = set(items)
    return len(items) == len(unique)


def best_grades(student_grades: dict) -> tuple:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    return "", 0.0


def histogram(sentence: str) -> tuple:
    # TODO: Créer l'histogramme a l'aide d'un dictionnaire
    #       Afficher l'histogramme et les lettres les plus fréquentes
    #       Retourner l'histogramme et le tableau de lettres

    return {}, []


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingrédients et enregistrer dans une structure de données 
    pass


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    pass


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    print(order())

    print(f"On vérifie les anagrammes...")
    print(anagrams())

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    #grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    #name, result = best_grades(grades)
    #print(f"{name} a la meilleure moyenne: {result}")
    
    #print("On enregistre les recettes...")
    #recipes = get_recipes()

    #print("On affiche une recette au choix...")
    #print_recipe(recipes)


if __name__ == '__main__':
    main()
