from typing import List, Dict


class Node:
    def __init__(self, is_end: bool, children: Dict):
        self.is_end = False
        self.children = children


class Trie:
    def __init__(self):
        self.root = Node(False, {})

    def insert(self, word: str) -> None:
        # Start from root
        current_node = self.root
        for c in word:
            # Look for exiting letters
            child = current_node.children.get(c, None)
            if child:
                current_node = child
            else:
                new_node = Node(False, {})
                current_node.children[c] = new_node
                current_node = new_node
        
        # Mark last node as the one which is the end of the word
        current_node.is_end = True

    def _get_leaf(self, prefix) -> Node:
        current_node = self.root
        for c in prefix:
            child = current_node.children.get(c, None)
            if not child:
                return None

            current_node = child

        return current_node

    def search(self, word: str) -> bool:
        leaf = self._get_leaf(word)
        return leaf and leaf.is_end

    def startsWith(self, prefix: str) -> bool:
        return self._get_leaf(prefix) != None


# Your Trie object will be instantiated and called as such:
word = "app"
obj = Trie()
assert not obj.search("test")
obj.insert(word)
assert obj.startsWith("ap")
assert not obj.startsWith("ao")

assert obj.search("app")
assert not obj.search("ap")
pass
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)