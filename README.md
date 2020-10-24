# subdomain-demo

## Setting up a development environment

    python -m venv venv
    pip install -r requirements.txt

## Changes

- create `/subdomain/urls` folder/package to hold urls conf per sub-domain

- update `hosts.py`
- update `settings.py`
- update `wsgi.py` (see deployemnt section)

- update `template/base.html` use `url` instead of `host_url`

- update `blog/urls` add `name='index'`

## deployment
- install `mod_wsgi` globally (out of your current `virtual environment`) see https://pypi.org/project/mod-wsgi/

- create `vhost` (see `deployment` folder, it ship an Apache sample vhost conf, you need to adapt it and put the right path)
- `wsgi.py` is updated with paths ..
- since you choose `venv` over `mkviratualenv` you need to download `activate_this.py` from `virtualenv` repository
https://github.com/dcreager/virtualenv/blob/master/virtualenv_support/activate_this.py and put it under `venv/Scripts`

refer to this thread onb Stackoverflow
https://stackoverflow.com/questions/27462582/how-can-i-activate-a-pyvenv-vitrualenv-from-within-python-activate-this-py-was 