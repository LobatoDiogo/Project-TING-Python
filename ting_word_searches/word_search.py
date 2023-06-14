def exists_word(word, instance):
    response = []

    for index in range(len(instance)):
        data = instance.search(index)
        file = data["nome_do_arquivo"]
        occurrences = [
            {"linha": line_index}
            for line_index, line
            in enumerate(data["linhas_do_arquivo"], start=1)
            if word.lower() in line.lower()
        ]

        if occurrences:
            response.append({
                "palavra": word,
                "arquivo": file,
                "ocorrencias": occurrences
            })

    return response


def search_by_word(word, instance):
    response = []

    for index in range(len(instance)):
        data = instance.search(index)
        file = data["nome_do_arquivo"]
        occurrences = [
            {"linha": line_index, "conteudo": line}
            for line_index, line
            in enumerate(data["linhas_do_arquivo"], start=1)
            if word.lower() in line.lower()
        ]

        if occurrences:
            response.append({
                "palavra": word,
                "arquivo": file,
                "ocorrencias": occurrences
            })

    return response
