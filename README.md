##postactivate
```
#!/bin/bash
# This hook is sourced after this virtualenv is activated.

export DJANGO_MODE='Local'
export SECRET_KEY='l*rb6x&i3%1z5r4@*qyl^zcb+58_@c)3uw8i(pg3#y=ndryxl'
export ALLOWED_HOST='*'
```
---
##predeactivate
```
#!/bin/bash
# This hook is sourced before this virtual is deactivated.

unset DJANGO_MODE
unset SECRET_KEY
unset ALLOWED_HOSTS
```