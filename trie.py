class TrieNode:
    def __init__(self, value):
        self.value = value
        self.children = {}
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode(None)

    # Add a word to the trie
    def add(self, word):
        characters = [i for i in word]
        tmp = self.root
        l = len(characters)
        for i in range(l):
            value = characters[i]
            if value not in tmp.children:
                n = TrieNode(value)
                tmp.children[value] = n
            tmp = tmp.children[value]
        tmp.isWord = True
    
    # Check whether a given word is in the trie
    def hasWord(self, word):
        characters = [i for i in word]
        tmp = self.root
        l = len(characters)
        for i in range(l):
            value = characters[i]
            if value not in tmp.children:
                return False
            tmp = tmp.children[value]
        if i == l - 1 and tmp.isWord == True:
            return True

        return False

    # Check whether a given prefix is available in the Trie
    def hasPrefix(self, word):
        characters = [i for i in word]
        tmp = self.root
        l = len(characters)
        for i in range(l):
            value = characters[i]
            if value not in tmp.children:
                return False
            tmp = tmp.children[value]
            if i == l - 1:
                return True

        return False

    # Get a list with all postfixes starting from a given node
    def __getAllPostfixWordsFromNode(self, root):
        output = []
        if root.isWord:
            output.append('')
        for i in root.children:
            node = root.children[i]
            if node.isWord:
                output.append(i)
            for o in node.children:
                postfixes = self.__getAllPostfixWordsFromNode(node.children[o])
                for postfix in postfixes:
                    output.append(i + node.children[o].value + postfix)
        return output
    
    # Get a list with all posible word endings from the given node
    def __getAllPostFixesFromNode(self, root, length):
        if length == 0:
            return []
        output = []
        if length == 1:
            for i in root.children:
                if root.children[i].isWord:
                    output.append(root.children[i].value)
        else:
            for i in root.children:
                if root.children[i].isWord:
                    output.append(root.children[i].value)
                postfixes = self.__getAllPostFixesFromNode(root.children[i], length-1)
                for postfix in postfixes:
                    output.append(root.children[i].value + postfix)
        return output
            
    # Get all possible words starting with a given prefix
    def getWordsWithPrefix(self, prefix):
        characters = [i for i in prefix]
        l = len(characters)
        levels = characters.count('.')
        characters = characters[:l - levels]
        prefix = ''.join(characters)
        output = []
        if levels == 0:
            if self.hasWord(prefix):
                output.append(prefix)
            tmp = self.__getNodeForPrefix(prefix)
            postfixes = self.__getAllPostfixWordsFromNode(tmp)
        else:
            tmp = self.__getNodeForPrefix(prefix)
            if tmp is None:
                return []
            postfixes = self.__getAllPostFixesFromNode(tmp, levels)
        for postfix in postfixes:
            output.append(prefix + postfix)
        return output

    # Get the node at the end of a given prefix
    def __getNodeForPrefix(self, prefix):
        tmp = self.root
        characters = [i for i in prefix]
        for i in characters:
            if i not in tmp.children:
                return None
            tmp = tmp.children[i]
        return tmp
    
    # Remove a given word from the trie
    def deleteWord(self, word):
        if self.hasWord(word):
            # Get all the characters of the word
            characters = [i for i in word]
            nodesPassed = []
            tmp = self.root
            # make a stack of nodes for the given characters
            for i in characters:
                tmp = tmp.children[i]
                nodesPassed.append(tmp)
            # If the end node has children then we should set that it's not the end of a word and not remove any nodes
            if len(nodesPassed[-1].children) > 0:
                nodesPassed[-1].isWord = False
                return True
            latestValue = None
            # Variables we need to check if we've started removing any nodes
            lenStart = len(nodesPassed)
            lenLeft = lenStart
            while lenLeft > 0:
                node = nodesPassed.pop()
                if latestValue != None:
                    # Check if we've reached the end of a shorter word, in this case we shoud not remove the node
                    if node.children[latestValue].isWord == True and lenLeft != lenStart:
                        return True
                    # Remove the node and decrement the counter of nodes to be removed
                    node.children.pop(latestValue)
                    lenLeft -= 1
                # Get the value of the node that needs to be removed from it's parent
                latestValue = node.value
                # if there are any children left, then stop removing nodes for it will remove another words as well
                if len(node.children) > 1:
                    return True
            return True
        return False
