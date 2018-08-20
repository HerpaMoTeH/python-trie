# python-trie
Trie data structure implemented in Python


Example usage:

Object creation:
```python
tr = Trie()
```

Adding words to the Trie:
```python
tr.add('word')
tr.add('Ola')
tr.add('Ouch')
tr.add('Olala')
```

Getting words starting with certain prefix and up to n extra characters:
```python
tr.getWordsWithPrefix('Ol...')
```

Getting words starting with a given prefix:
```python
tr.getWordsWithPrefix('O')
```

Deleting a certain word from the Trie:
```python
tr.deleteWord('Olala')
```
