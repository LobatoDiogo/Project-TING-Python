from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.queue = list()

    def __len__(self):
        return self.size()

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def search(self, index):
        if index < 0 or index >= len(self.queue):
            raise IndexError("Índice Inválido ou Inexistente")
        return self.queue[index]

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0
