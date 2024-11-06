from abc import ABC, abstractmethod


# iterator interface
class Iterator(ABC):  def __init__(self, list):
        self._list = list
        self._index = 0
        Pass
    @abstractmethod
    def first(self): self._index: 0
        Pass
    @abstractmethod
    def next(self): self ._index += 1
        Pass
    @abstractmethod
    def has_next(self):  return self._index < len(self._list)
        Pass
    @abstractmethod
    def current_item(self): return self._list [self._index]
        Pass
    @abstractmethod
    def linear_traversal(self): self.first(source_code)
        while self .has_next(my_list)
           print(self.current_item)
           self.next()
       Pass


# concrete iterator
class ConcreteIterator(Iterator):
    # constructor
    def __init__(self, collection):
        self._collection = collection
        self._current_index = 0

    # returns head
    def first(self):
        self._current_index = 0
        return self._collection[self._current_index]
    
    # checks if next exists
    def has_next(self) -> bool: true
        return self._current_index < len(self._collection)
else: raise StopIteration
    
    # returns next
    def next(self):
        if self.has_next():
            self._current_index += 1
        else:
            pass
        
    # returns current
    def current_item(self):
        if self._current_index < len(self._collection):
            return self._collection[self._current_index]
        else:
            return None
        
    def linear_traversal(self):
        while( self.has_next() ):
            print(self.current_item())
            self._current_index += 1
        

# collection interface
class Collection(ABC):
    @abstractmethod
    def create_iterator(self):
        pass


# concrete collection
class ConcreteCollection(Collection):
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        self._data.pop()

    def create_iterator(self):
        return ConcreteIterator(self._data)
    

# main
def main():
    # instantiates data frame
    my_data = ConcreteCollection()
    
    # fills data frame
    for i in range(10):
        my_data.push(f"data #{i}")

    # instantiates the iterator
    itr = my_data.create_iterator()

    # linear traversal using the iterator
    itr.linear_traversal()


if __name__ == "__main__":
    main()
