GitHub Trac Ticket Import
=========================

Simple script for transferring tickets from Trac to GitHub.

This was written manly for a once off conversion, so this is not well tested or
supported in any way.

``TRAC_URL``
    should be pointed the CSV version of report 1.
``USERNAME``
    is your GitHub login.
``ORGNAME``
    is the organization name where the repo is located, if different than your
    GitHub login. (You must have appropriate permissions in the organization to
    import issues, if the organization is different than your GitHub login.) If
    left empty, then this will default to your GitHub login.
``PROJECT``
    the repo name.
``AUTH_TOKEN``
    your GitHub API token.
``TAGS``
    Additonal tags to add to project.

Known issues
------------

This code does not respect the rate limiting GitHub has on it's API, thus it
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
