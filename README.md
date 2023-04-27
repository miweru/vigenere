# Vigenère Cipher Reinforcement Learning Project

Dieses Projekt implementiert ein System, das Reinforcement Learning und Transformer-Modelle verwendet, um Vigenère-Verschlüsselungen zu knacken.

## VigenereCipher-Klasse

Die `VigenereCipher`-Klasse ist in der Datei `vigenere_cipher.py` definiert und bietet grundlegende Funktionen zum Verschlüsseln und Entschlüsseln von Texten unter Verwendung des Vigenère-Chiffres.

### Verwendung

Um die `VigenereCipher`-Klasse zu verwenden, erstellen Sie zuerst eine Instanz der Klasse und geben Sie den Schlüssel an, den Sie für die Verschlüsselung und Entschlüsselung verwenden möchten:

```python
from vigenere_cipher import VigenereCipher

cipher = VigenereCipher("MYSECRETKEY")
```

Verwenden Sie anschließend die `encrypt`-Methode, um einen Klartext zu verschlüsseln:

```python
ciphertext = cipher.encrypt("Hello, World!")
```

Verwenden Sie die `decrypt-Methode, um einen verschlüsselten Text zu entschlüsseln:

```python
plaintext = cipher.decrypt(ciphertext)
```

### Einschränkungen
Die aktuelle Implementierung der VigenereCipher-Klasse verwendet das englische Alphabet (A-Z) und ignoriert alle anderen Zeichen. Sie könnten die Implementierung anpassen, um zusätzliche Zeichen oder andere Alphabete zu unterstützen, wenn dies für Ihre Anwendung erforderlich ist.

## Weitere Komponenten
