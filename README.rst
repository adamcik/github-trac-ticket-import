Github Trac Ticket Import
=========================

Simple script for transfering tickets from Trac to Github.

This was written manly for a once off conversion, so this is not well testet or
supported in any way. The ``TRAC_URL`` should be pointed the CSV version of
report 1. ``USERNAME`` is the Github login, ``PROJECT`` the repo name and
``AUTH_TOKEN`` your Github API token.

Known issues
------------

This code does not respect the rate limiting Github has on it's API, thus it
will fail once this limit has been passed.

License
-------

Copyright (c) 2010 Thomas Adamcik

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
