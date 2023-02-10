from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    file_read = txt_importer(path_file)

    for i in range(instance.__len__()):
        dict_item = instance.search(i)
        if dict_item["nome_do_arquivo"] == path_file:
            return None

    dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_read),
        "linhas_do_arquivo": file_read,
    }

    instance.enqueue(dict)
    print(dict)


def remove(instance):
    if instance.__len__() == 0:
        print("Não há elementos")
        return None

    remove_file = instance.dequeue()
    path_file = remove_file["nome_do_arquivo"]
    print(f"Arquivo {path_file} removido com sucesso")


def file_metadata(instance, position):
    try:
        file_search = instance.search(position)
        print(file_search)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
