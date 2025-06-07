
# Step by step making the base structure:

## 1. Making base project structure:

```
$ mkdir <project-root>
$ git init
$ touch README.md .gitignore LICENSE
```
* Edit all new files
```
$ git add .
$ git commit -m "Initial commit"
$ git remote add origin <your/repository/ssh/link>
$ git push origin main
$ pipenv install --python "3.12" 'django>=5.0' 'djangorestframework>=3.14'
$ mkdir requirements
$ pipenv requirements > requirements/requirements.txt
$ pipenv run django-admin startproject rest_starter
$ mv rest_starter/rest_starter rest_starter/config
$ mkdir rest_starter/config/settings
$ mv rest_starter/config/settings.py rest_starter/config/settings/development.py
$ touch rest_starter/config/settings/__init__.py \
        rest_starter/config/settings/production.py \
        rest_starter/config/settings/staging.py
$ mv rest_starter/manage.py .
```
* Open 'manage.py', 'settings/development.py', 'asgi.py', and 'wsgi.py' to change all:
    > rest_starter.

    to 
    > rest_starter.config.


## 2. Adding 'core' app to project
```
$ mkdir rest_starter/apps
$ mkdir rest_starter/apps/core
$ pipenv run django-admin startapp core rest_starter/apps/core
$ touch rest_starter/apps/core/constants.py \
        rest_starter/apps/core/exceptopns.py \
        rest_starter/apps/core/helpers.py \
        rest_starter/apps/core/services.py \
        rest_starter/apps/core/urls.py
$ mkdir rest_starter/apps/core/api
$ mkdir rest_starter/apps/core/api/v1
$ mkdir rest_starter/apps/core/api/v2
$ mkdir rest_starter/apps/core/fixtures
$ mkdir rest_starter/apps/core/management
$ mkdir rest_starter/apps/core/management/commands
$ mkdir rest_starter/apps/core/templates
$ mkdir rest_starter/apps/core/tests
$ mv rest_starter/apps/core/tests.py rest_starter/apps/core/tests/test_core_name.py
$ touch rest_starter/apps/core/tests/__init__.py
$ touch rest_starter/apps/core/api/__init__.py \
$       rest_starter/apps/core/api/v1/__init__.py \
        rest_starter/apps/core/api/v1/serializers.py \
        rest_starter/apps/core/api/v1/urls.py \
        rest_starter/apps/core/api/v1/views.py
$ touch rest_starter/apps/core/api/v2/__init__.py \
        rest_starter/apps/core/api/v2/serializers.py \
        rest_starter/apps/core/api/v2/urls.py \
        rest_starter/apps/core/api/v2/views.py
$ touch rest_starter/apps/core/fixtures/.gitkeep \
        rest_starter/apps/core/management/__init__.py \
        rest_starter/apps/core/management/commands/__init__.py \
        rest_starter/apps/core/management/commands/command.py \
        rest_starter/apps/core/management/commands/__init__.py \
        rest_starter/apps/core/templates/.gitkeep
```
## 3. Adding 'app1' app to project:
```
$ mkdir rest_starter/apps/app1
$ pipenv run django-admin startapp app1 rest_starter/apps/app1
$ mkdir rest_starter/apps/app1/api
$ mkdir rest_starter/apps/app1/api/v1
$ mkdir rest_starter/apps/app1/api/v2
$ mkdir rest_starter/apps/app1/fixtures
$ mkdir rest_starter/apps/app1/management
$ mkdir rest_starter/apps/app1/management/commands
$ mkdir rest_starter/apps/app1/templates
$ mkdir rest_starter/apps/app1/tests
$ mv rest_starter/apps/app1/tests.py rest_starter/apps/app1/tests/test_app1_name.py
$ touch rest_starter/apps/app1/tests/__init__.py 
$ touch rest_starter/apps/app1/api/__init__.py \
        rest_starter/apps/app1/api/v1/__init__.py \
        rest_starter/apps/app1/api/v1/serializers.py \
        rest_starter/apps/app1/api/v1/urls.py \
        rest_starter/apps/app1/api/v1/views.py
$ touch rest_starter/apps/app1/api/v2/__init__.py \
        rest_starter/apps/app1/api/v2/serializers.py \
        rest_starter/apps/app1/api/v2/urls.py \
        rest_starter/apps/app1/api/v2/views.py
$ touch rest_starter/apps/app1/management/__init__.py \
        rest_starter/apps/app1/management/commands/command.py \
        rest_starter/apps/app1/management/commands/__init__.py \
        rest_starter/apps/app1/templates/.gitkeep \
        rest_starter/apps/app1/services.py \
        rest_starter/apps/app1/urls.py
```
## 4. Adding 'app2' app to project:
```
$ mkdir rest_starter/apps/app2
$ pipenv run django-admin startapp app2 rest_starter/apps/app2
$ mkdir rest_starter/apps/app2/api
$ mkdir rest_starter/apps/app2/api/v1
$ mkdir rest_starter/apps/app2/api/v2
$ mkdir rest_starter/apps/app1/fixtures
$ mkdir rest_starter/apps/app1/management
$ mkdir rest_starter/apps/app1/management/commands
$ mkdir rest_starter/apps/app1/templates
$ mkdir rest_starter/apps/app1/tests
$ mv rest_starter/apps/app2/tests.py rest_starter/apps/app2/tests/test_app2_name.py
$ touch rest_starter/apps/app2/tests/__init__.py 
$ touch rest_starter/apps/app2/api/__init__.py \
        rest_starter/apps/app2/api/v1/__init__.py \
        rest_starter/apps/app2/api/v1/serializers.py \
        rest_starter/apps/app2/api/v1/urls.py \
        rest_starter/apps/app2/api/v1/views.py
$ touch rest_starter/apps/app2/api/v2/__init__.py \
        rest_starter/apps/app2/api/v2/serializers.py \
        rest_starter/apps/app2/api/v2/urls.py \
        rest_starter/apps/app2/api/v2/views.py
$ touch rest_starter/apps/app2/management/__init__.py \
        rest_starter/apps/app2/management/commands/command.py \
        rest_starter/apps/app2/management/commands/__init__.py \
        rest_starter/apps/app2/templates/.gitkeep \
        rest_starter/apps/app2/services.py \
        rest_starter/apps/app2/urls.py

```
## 5. Initializing apps configuration in the project:

1. First open 'settings.py' and do bellow changes:
    ```
    INSTALLED_APPS = [
        ... 

        # Add your apps here:
        'rest_starter.apps.core',
        'rest_starter.apps.app1',
        'rest_starter.apps.app2',
    ]
    ```
2. Then open 'apps.py' from all apps and do changes:
    ```
    name = 'apps.core'
    name = 'apps.app1'
    name = 'apps.app2'
    ```
    to 

    ```
    name = 'rest_starter.apps.core'
    name = 'rest_starter.apps.app1'
    name = 'rest_starter.apps.app2'
    ```
## 6. Add other structure to project:
```
$ mkdir rest_starter/common
$ touch rest_starter/common/__init__.py \
        rest_starter/common/common.py \
        rest_starter/common/constants.py \
        rest_starter/common/generics.py \
        rest_starter/common/helpers.py \
        rest_starter/common/mixins.py \
        rest_starter/common/models.py \
        rest_starter/common/serializers.py
$ mkdir deployments docs local_db locale
$ touch deployments/docker-compose.yml \
        deployments/Dockerfile \
        deployments/Dockerfile_dev \
        deployments/Dockerfile_prod
$ touch docs/CHANGELOG.md \
        docs/CONTRIBUTING.md \
        docs/deployment.md \
        docs/local-development.md \
        docs/schema.yml \
        docs/step-by-step.md
$ touch local_db/db.sqlite3.example
$ touch locale/.gitkeep

$ mkdir logs media scripts static static/css
$ mkdir static/css static/images static/js 
$ touch logs/.gitkeep \
        media/.gitkeep \
        scripts/entrypoint.sh \
        static/css/.gitkeep \
        static/images/.gitkeep \
        static/js/.gitkeep

$ touch requirements/common.txt \
        requirements/development.txt \
        requirements/local.txt \
        requirements/production.txt

$ cp .gitignore .dockerignore
$ touch .env \
        .flake8 \
        pyproject.toml \
        pytest.ini \
        setup.cfg \
        setup.py \
        tox.ini \

$ pipenv requirements --dev-only > requirements/requirements-dev.txt
```

