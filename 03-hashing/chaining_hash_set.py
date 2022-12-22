from chaining_hash_node import ChainingHashNode

class ChainingHashSet():
    def __init__(self, capacity=0):
        self.hash_table = [None] * capacity
        self.table_size = 0
        self.capacity = capacity

    def get_hash_code(self, key):
        """Hash function that calculates a hash code for a given key using the modulo division.
        :param key: Key for which a hash code shall be calculated according to the length of the hash table.
        :return: The calculated hash code for the given key.
        """
        return key % len(self.hash_table)

    def get_hash_table(self):
        """(Required for testing only)
        :return the hash table.
        """
        return self.hash_table

    def set_hash_table(self, table):
        """(Required for testing only) Set a given hash table..
        :param table: Given hash table which shall be used.

        !!!
        Since this method is needed for testing we decided to implement it.
        You do not need to change or add anything.
        !!!

        """
        self.hash_table = table
        self.capacity = len(table)
        self.table_size = 0
        for node in table:
            while node is not None:
                self.table_size += 1
                node = node.next

    def get_table_size(self):
        """returns the number of stored keys (keys must be unique!)."""
        return self.table_size

    def insert(self, key):
        """Inserts a key and returns True if it was successful. If there is already an entry with the
          same key, the new key will not be inserted and False is returned.
         :param key: The key which shall be stored in the hash table.
         :return: True if key could be inserted, or False if the key is already in the hash table.
         :raises: a ValueError if any of the input parameters is None.
         """
        if key is None:
            raise ValueError('Key can not be None')

        if self.contains(key):
            return False

        get_hash = self.get_hash_code(key)
        item = self.hash_table[get_hash]

        node = ChainingHashNode(key)
        tmp = item

        if item is None:
            self.hash_table[get_hash] = node
        else:
            while tmp.next is not None:
                tmp = tmp.next
            tmp.next = node

        self.table_size += 1

        return True

    def contains(self, key):
        """Searches for a given key in the hash table.
         :param key: The key to be searched in the hash table.
         :return: True if the key is already stored, otherwise False.
         :raises: a ValueError if the key is None.
         """
        get_hash = self.get_hash_code(key)
        item = self.hash_table[get_hash]

        if item is None:
            return False

        if item.key == key:
            return True
        else:
            while item.next is not None:
                item = item.next
                if item.key == key:
                    return True
            return False

    def remove(self, key):
        """Removes the key from the hash table and returns True on success, False otherwise.
        :param key: The key to be removed from the hash table.
        :return: True if the key was found and removed, False otherwise.
        :raises: a ValueError if the key is None.
        """
        if key is None:
            raise ValueError('Key can not be None')

        get_hash = self.get_hash_code(key)
        item = self.hash_table[get_hash]
        tmp = item

        if item is None:
            return False

        if item.key == key:
            self.hash_table[get_hash] = item.next
            self.table_size -= 1
            return True

        while item.next is not None:
            tmp = item
            item = item.next
            if item.key == key:
                tmp.next = item.next
                self.table_size -= 1
                return True

    def clear(self):
        """Removes all stored elements from the hash table by setting all nodes to None.
        """
        for n in range(len(self.hash_table)):
            self.hash_table[n] = None

        self.table_size = 0

    def to_string(self):
        """Returns a string representation of the hash table (array indices and stored keys) in the format
            Idx_0 {Node, Node, ... }, Idx_1 {...}
            e.g.: 0 {13}, 1 {82, 92, 12}, 2 {2, 32}, """
        hash_table_str = ''
        for ind, el in enumerate(self.hash_table):
            tmp = '' + str(ind) + ' {' + str(el.key)
            tmp_el = el
            while tmp_el.next is not None:
                tmp_el = tmp_el.next
                tmp = tmp + ',' + str(tmp_el.key)

            tmp = tmp + '}, '
            hash_table_str = hash_table_str + tmp

        return hash_table_str
