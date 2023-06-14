from ting_file_management.priority_queue import PriorityQueue
import pytest


priority = {
        "nome_do_arquivo": "arquivo_teste.txt",
        "qtd_linhas": 1,
        "linhas_do_arquivo": [],
    }

not_priority = {
        "nome_do_arquivo": "arquivo_teste.txt",
        "qtd_linhas": 9,
        "linhas_do_arquivo": [],
    }


def test_basic_priority_queueing():
    queue = PriorityQueue()

    queue.enqueue(not_priority)
    queue.enqueue(priority)

    assert len(queue) == 2
    assert queue.search(0) == priority

    result = queue.dequeue()
    assert result == priority
    assert len(queue) == 1

    with pytest.raises(IndexError):
        queue.search(3)
