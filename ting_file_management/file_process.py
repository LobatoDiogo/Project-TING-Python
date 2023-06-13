import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    data = txt_importer(path_file)
    linhas = len(data)

    file_info = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": linhas,
        "linhas_do_arquivo": data,
    }

    for index in range(len(instance)):
        search_result = instance.search(index)
        if search_result == file_info:
            return

    instance.enqueue(file_info)

    print(file_info, file=sys.stdout)


def remove(instance):

    if instance.is_empty():
        print("Não há elementos", file=sys.stdout)
        return

    file_remove = instance.dequeue()['nome_do_arquivo']

    print(f"Arquivo {file_remove} removido com sucesso", file=sys.stdout)


def file_metadata(instance, position):
    if position < 0 or position >= len(instance):
        print("Posição inválida", file=sys.stderr)
        return

    file_info = instance.search(position)

    print(file_info, file=sys.stdout)
