# Autocomplete project

## Part 1. Autocomplete script

This script proposes the most used words, starting with given *prefix*.
In other words, it makes autocompletion, based on
[prefix trees](https://en.wikipedia.org/wiki/Trie),
constructed from input.

This script requires *python 3.5* installed. It uses no side packages, so
there is no *requirements.txt* in the project. Input should be `utf-8`
enсoded.

The script takes no arguments.

To use it, just run the following command in the terminal:
   ```bash
   $ python autocompleter.py
   ```

  After the script runs, it is waiting for input. Input data shoulв be
  in the certain format. The first line should be integer **N**
  (1 <= **N** <= 10<sup>5</sup>), representing the number of words in the
  dictionary. Next N lines consist of a word and it's frequency
  (integer) of use. On the (N+2)<sup>th</sup> line, there is an
  integer **K**, representing the number of prefixes to autocomplete. The
  next **K** lines consist of prefixes (one per line).
  Example of input:
  ```
  5
  kare 10
  kanojo 20
  karetachi 1
  korosu 7
  sakura 3
  3
  k
  ka
  kar
  ```
Once input received by the script, it produces top 10 words
(one per line, sorted at first by frequency *descending*,
then alphabetically *ascending*), starting with specified prefixes.
Words for different prefixes are separated by empty line.
Example of output for earlier
specified input:
  ```
  kanojo
  kare
  korosu
  karetachi

  kanojo
  kare
  karetachi

  kare
  karetachi
  ```

## Part 2. Autocomplete TCP/IPv4 server/client apps.
To run both server and client scripts, one should have *python 3.5*
installed, no side packages required.
### Server script.
Autocomplete server script allows to run **TCP server**, which process
autocomplete for *prefixes*, received from **clients**.

Server script takes 2 positional arguments:
* file_path: path to the file with words-frequency pairs. Example of file
content:
  ```
  kare 10
  kanojo 20
  karetachi 1
  korosu 7
  sakura 3
  ```
* port: the port, specified for TCP communication with clients.

Example of use (*host: 'localhost', port: 8080*):
```bash
  $ python autocomplete_server.py './dictionary.txt' 8080
  starting server...
  waiting for requests...
```
Now server is listening 8080 port, and waiting for client requests.
It can serve only requests in the following format `GET <PREFIX>`
(*utf-8 encoded*),
otherwise *error 400* is returned. Handlers of client requests are
processed in separate threads, so the main process is not blocked.
Request handlers use *autocomplete_engine.py* to produce autocompletion.
If no words found, empty bytes object in sent.
Response in the form of top 10 words (one per line), encoded in *utf-8*
is sent to client.

### Client script.
Client script makes requests to server in format `GET <PREFIX>`, and
receives most frequently used words for given *prefix*. If no possible
words found, server sends empty bytes object.

Script runs in infinite loop waiting for input from user,
to specify *prefix* of interest. Once *prefix* given,
it prints the most used words, starting with this
*prefix*. If empty prefix is sent, server can't recognise request format,
consequently *error 400* is received.

Script takes 2 positional arguments:
* host: host or ip-adress of server
* port: port used by server for TCP communication

Example of use:
```bash
$ python autocomplete_client.py 'localhost' 8080
Prefix: k
kanojo
kare
korosu
karetachi
Prefix: kar
kare
karetachi
Prefix: **&^&*^

Prefix:
Error 400.
Bad request.

```

## Project Goals
The project is a solution of a certain coding interview challenge.
