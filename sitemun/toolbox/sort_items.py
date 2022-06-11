def sort_chrono(liste):
    sorted_list = []
    endpoint = len(liste)
    while len(sorted_list) < endpoint:
        biggest = liste[0]
        for comparaison in liste:
            if biggest.pk >= comparaison.pk:
                biggest = biggest
            else:
                biggest = comparaison
        sorted_list.append(biggest)
        liste.pop(liste.index(biggest))
    return sorted_list
