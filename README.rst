state-server
============

Single-purpose server holding the current state of the environment.

Used as an alternative to interprocess communication
or message queuing.

Example:
=========

Legend:
 - `>` - netcat inputs
 - `<` - server response ::

        $ state_server
        INFO:root:Listening on localhost 12300

        $ nc localhost 12300
        > var_name value
        < _ok
        > var_name
        < value
        > var_name new_value
        < _ok
        > var_name
        < new_value
        > no_such_varname
        < _na


Features:
----------
 - TCP enabled, threaded
 - query/set value of the variable
 - 100% test coverage

Requirements:
--------------
 - python 2.6+

Installation:
--------------
 - install state-server (`easy_install state-server` or `pip install state-server`)
 - run `state_server -h`
