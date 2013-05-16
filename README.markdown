flask-csrf
==========

Quick, easy CSRF protection for your Flask applications.

See the [documentation](http://sjl.bitbucket.org/flask-csrf/) for more information.

## Why the fork?

1. Protects PUT and DELETE methods too, not just POST. To help with this, _csrf_token can be present on the query string too, not just in a form field.
2. Enables [non-standard workflows](https://bitbucket.org/sjl/flask-csrf/issue/4/too-strict-limiting-workflow-assumptions) by storing a single CSRF token in the session and re-using it for every form.
