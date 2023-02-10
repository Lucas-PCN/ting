def exists_word(word, instance):
    result = []
    word_occurrences = []

    for data in range(instance.__len__()):
        file_search = instance.search(data)

        for index, line in enumerate(file_search["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                word_occurrences.append({"linha": index + 1})

        if len(word_occurrences) > 0:
            result.append(
                {
                    "palavra": word,
                    "arquivo": file_search["nome_do_arquivo"],
                    "ocorrencias": word_occurrences,
                }
            )

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
