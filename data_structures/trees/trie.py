from typing import Optional

class Node:
    """Represents a node in the trie (prefix tree) data structure.

    Each node contains a character, a flag indicating if it marks the end
    of a complete word, and a dictionary mapping children characters to
    their respective nodes.

    Attributes:
        char: The character stored in this node
        is_end: True if this node marks the end of a complete word
        children: Dictionary mapping child characters to child nodes
    """
    def __init__(self, char: str, is_end: bool = False) -> None:
        """Initialize a new trie node.

        Args:
            char: The character to store in this node
            is_end: Whether this node marks the end of a word
        """
        self.char = char
        self.is_end = is_end
        self.children = {}


class Trie:
    """A trie (prefix tree) data structure for efficient string storage and search.

    A trie is a tree-like structure where each node represents a character
    of a string. It enables efficient insertion, search, and prefix lookup
    operations. All strings sharing a common prefix form a branch of the tree.

    Time Complexity:
        - insert: O(L) where L is the length of the word
        - search: O(L) where L is the length of the word
        - search_prefix: O(P) where P is the length of the prefix
    Space Complexity: O(Total characters in all inserted words)
    """

    def __init__(self) -> None:
        """Initialize an empty trie.

        Creates a root node with a special character (asterisk) that serves
        as the starting point for all strings. This root node itself does not
        represent a valid character and has no children.
        """
        self.root = Node("*")

    def insert(self, word: str) -> None:
        """Insert a word into the trie.

        Algorithm:
            1. Traverse from the root, following existing nodes for each character
            2. If a node doesn't exist for a character, create it
            3. Mark the final node as `is_end = True` to indicate completion of the word
            4. For existing nodes, simply move to the next level without modification

        The algorithm efficiently reuses existing nodes when they exist, sharing
        the memory used for common prefixes across multiple words.

        Time Complexity: O(L) where L is the length of the word
        Space Complexity: O(L) for the newly created nodes (if word is new)

        Args:
            word: The string to insert into the trie
        """
        root = self.root

        last_letter = len(word) - 1
        for idx, letter in enumerate(word):
            curr = root.children.get(letter)
            if curr is None:
                curr = Node(letter, idx == last_letter)
                root.children[letter] = curr
            root = curr

    def search(self, word: str) -> bool:
        """Search for a complete word in the trie.

        Algorithm:
            1. Traverse the trie following the characters of the word
            2. If any character is not found in the current node's children,
               return False (word doesn't exist)
            3. If all characters are found, check if the final node has
               `is_end = True` (indicates word is actually stored)
            4. If the final node is marked as end-of-word, return True

        Time Complexity: O(L) where L is the length of the word
        Space Complexity: O(1)

        Args:
            word: The string to search for in the trie

        Returns:
            True if the complete word exists in the trie, False otherwise
        """
        root = self.root

        last_letter = len(word) - 1
        for idx, letter in enumerate(word):
            curr = root.children.get(letter)
            if curr is None:
                return False
            if curr.is_end and idx == last_letter:
                return True

        return False

    def search_prefix(self, prefix: str) -> bool:
        """Check if a prefix exists in the trie.

        Algorithm:
            1. Traverse from the root following the characters of the prefix
            2. If any character is not found in the current node's children,
               return False (prefix doesn't exist)
            3. If all characters are found, return True

        This method checks if there are any words that start with the given
        prefix. It doesn't require the prefix to be a complete word, only that
        all characters of the prefix exist as a path from the root.

        Time Complexity: O(P) where P is the length of the prefix
        Space Complexity: O(1)

        Args:
            prefix: The string prefix to search for

        Returns:
            True if the prefix exists in the trie, False otherwise
        """
        root = self.root

        for letter in prefix:
            curr = root.children.get(letter)
            if curr is None:
                return False

        return True
