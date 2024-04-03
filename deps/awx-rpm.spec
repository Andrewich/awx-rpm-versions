%global python3_pkgversion 3.11

%define  debug_package %{nil}
%define _prefix /opt/awx-rpm
%define _mandir %{_prefix}/share/man
%global __os_install_post %{nil}

%define service_user awx
%define service_group awx
%define service_homedir /var/lib/tower
%define service_logdir /var/log/tower
%define service_configdir /etc/tower

Summary: Ansible AWX-RPM
Name: awx-rpm
Version: 24.1.0
Release: 7%{dist}
Source0: awx-24.1.0.tar.gz
Source1: settings.py-%{version}
Source2: awx-receiver.service-%{version}
Source3: awx-dispatcher.service-%{version}
Source4: awx-wsrelay.service-%{version}
Source5: awx-ws-heartbeat.service-%{version}
Source6: awx-daphne.service-%{version}
Source7: awx-web.service-%{version}
Source20: awx-receptor.service-%{version}
Source21: awx-receptor-hop.service-%{version}
Source22: awx-receptor-worker.service-%{version}
Source23: awx.target-%{version}
Source30: receptor.conf-%{version}
Source31: receptor-hop.conf-%{version}
Source32: receptor-worker.conf-%{version}
Source40: awx-rpm-logo.svg-%{version}
Source8: awx-rpm-nginx.conf-%{version}
Patch0: awx-patch.patch-%{version}
License: GPLv3
Group: AWX
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}.buildroot
Vendor: AWX
Prefix: %{_prefix}
AutoReqProv: false

BuildRequires: make python%{python3_pkgversion} python%{python3_pkgversion}-devel nodejs npm gettext git python%{python3_pkgversion}-build rsync libpq libpq-devel 
BuildRequires: python3.11-adal = 1.2.7
BuildRequires: python3.11-aiodns = 3.1.1
BuildRequires: python3.11-aiohttp = 3.9.3
BuildRequires: python3.11-aiohttp-retry = 2.8.3
BuildRequires: python3.11-aiohttp+speedups = 3.9.3
BuildRequires: python3.11-aioredis = 1.3.1
BuildRequires: python3.11-aiosignal = 1.3.1
BuildRequires: python3.11-annotated-types = 0.6.0
BuildRequires: python3.11-ansible-builder = 3.0.1
BuildRequires: python3.11-ansible-runner = 2.3.6
BuildRequires: python3.11-ansiconv = 1.0.0
BuildRequires: python3.11-asciichartpy = 1.5.25
BuildRequires: python3.11-asgiref = 3.7.2
BuildRequires: python3.11-asn1 = 2.7.0
BuildRequires: python3.11-asyncpg = 0.29.0
BuildRequires: python3.11-async-timeout = 4.0.3
BuildRequires: python3.11-attrs = 23.2.0
BuildRequires: python3.11-autobahn = 23.6.2
BuildRequires: python3.11-autocommand = 2.2.2
BuildRequires: python3.11-automat = 22.10.0
BuildRequires: python3.11-awscrt = 0.16.9
BuildRequires: python3.11-azure-common = 1.1.28
BuildRequires: python3.11-azure-core = 1.30.0
BuildRequires: python3.11-azure-core+aio = 1.30.0
BuildRequires: python3.11-azure-identity = 1.15.0
BuildRequires: python3.11-azure-keyvault = 4.2.0
BuildRequires: python3.11-azure-keyvault-certificates = 4.7.0
BuildRequires: python3.11-azure-keyvault-keys = 4.8.0
BuildRequires: python3.11-azure-keyvault-secrets = 4.7.0
BuildRequires: python3.11-babel = 2.14.0
BuildRequires: python3.11-bcrypt = 4.1.2
BuildRequires: python3.11-bcrypt+tests = 4.1.2
BuildRequires: python3.11-bcrypt+typecheck = 4.1.2
BuildRequires: python3.11-bindep = 2.11.0
BuildRequires: python3.11-blinker = 1.7.0
BuildRequires: python3.11-boto3 = 1.34.47
BuildRequires: python3.11-botocore = 1.34.47
BuildRequires: python3.11-brotli = 1.1.0
BuildRequires: python3.11-build = 1.2.1
BuildRequires: python3.11-cachecontrol = 0.14.0
BuildRequires: python3.11-cachecontrol+filecache = 0.14.0
BuildRequires: python3.11-cachetools = 5.3.2
BuildRequires: python3.11-calver = 2022.6.26
BuildRequires: python3.11-cffi = 1.16.0
BuildRequires: python3.11-channels = 3.0.5
BuildRequires: python3.11-channels-redis = 3.4.1
BuildRequires: python3.11-chardet = 5.2.0
BuildRequires: python3.11-charset-normalizer = 3.3.2
BuildRequires: python3.11-cleo = 2.1.0
BuildRequires: python3.11-click = 8.1.7
BuildRequires: python3.11-constantly = 23.10.4
BuildRequires: python3.11-coreapi = 2.3.3
BuildRequires: python3.11-coreschema = 0.0.4
BuildRequires: python3.11-crashtest = 0.4.1
BuildRequires: python3.11-cryptography = 41.0.7
BuildRequires: python3.11-cython = 0.29.37
BuildRequires: python3.11-daphne = 3.0.2
BuildRequires: python3.11-defusedxml = 0.7.1
BuildRequires: python3.11-distlib = 0.3.8
BuildRequires: python3.11-distro = 1.9.0
BuildRequires: python3.11-django = 4.2.6
BuildRequires: python3.11-django-ansible-base = 20240212
BuildRequires: python3.11-django-ansible-base+jwt_consumer = 20240212
BuildRequires: python3.11-django-ansible-base+rest_filters = 20240212
BuildRequires: python3.11-django-auth-ldap = 4.7.0
BuildRequires: python3.11-django+bcrypt = 4.2.6
BuildRequires: python3.11-django-cors-headers = 4.3.1
BuildRequires: python3.11-django-crum = 0.7.9
BuildRequires: python3.11-django-debug-toolbar = 4.3.0
BuildRequires: python3.11-django-extensions = 3.2.3
BuildRequires: python3.11-django-guid = 3.2.1
BuildRequires: python3.11-django-oauth-toolkit = 1.7.1
BuildRequires: python3.11-django-pglocks = 1.0.4
BuildRequires: python3.11-django-polymorphic = 3.1.0
BuildRequires: python3.11-django-radius = 1.5.0
BuildRequires: python3.11-djangorestframework = 3.14.0
BuildRequires: python3.11-djangorestframework-yaml = 2.0.0
BuildRequires: python3.11-django-rest-swagger = 2.2.0
BuildRequires: python3.11-django-solo = 2.2.0
BuildRequires: python3.11-django-split-settings = 1.0.0
BuildRequires: python3.11-dm-xmlsec-binding = 2.2
BuildRequires: python3.11-docutils = 0.20.1
BuildRequires: python3.11-drf-yasg = 1.21.7
BuildRequires: python3.11-dulwich = 0.21.7
BuildRequires: python3.11-ecdsa = 0.18.0
BuildRequires: python3.11-enum-compat = 0.0.3
BuildRequires: python3.11-expandvars = 0.12.0
BuildRequires: python3.11-fastjsonschema = 2.19.1
BuildRequires: python3.11-filelock = 3.13.1
BuildRequires: python3.11-freezegun = 1.4.0
BuildRequires: python3.11-frozenlist = 1.4.1
BuildRequires: python3.11-future = 0.16.0
BuildRequires: python3.11-gitdb = 4.0.11
BuildRequires: python3.11-gitpython = 3.1.42
BuildRequires: python3.11-google-auth = 2.28.1
BuildRequires: python3.11-h2 = 4.1.0
BuildRequires: python3.11-hatch-fancy-pypi-readme = 24.1.0
BuildRequires: python3.11-hatchling = 1.22.4
BuildRequires: python3.11-hatch-vcs = 0.4.0
BuildRequires: python3.11-hiredis = 2.0.0
BuildRequires: python3.11-hpack = 4.0.0
BuildRequires: python3.11-hyperframe = 6.0.1
BuildRequires: python3.11-hyperlink = 21.0.0
BuildRequires: python3.11-idna = 3.6
BuildRequires: python3.11-importlib-metadata = 6.2.1
BuildRequires: python3.11-incremental = 22.10.0
BuildRequires: python3.11-inflect = 7.0.0
BuildRequires: python3.11-inflection = 0.5.1
BuildRequires: python3.11-installer = 0.7.0
BuildRequires: python3.11-irc = 20.3.1
BuildRequires: python3.11-isodate = 0.6.1
BuildRequires: python3.11-itypes = 1.2.0
BuildRequires: python3.11-jaraco-classes = 3.3.1
BuildRequires: python3.11-jaraco-collections = 5.0.0
BuildRequires: python3.11-jaraco-context = 4.3.0
BuildRequires: python3.11-jaraco-functools = 4.0.0
BuildRequires: python3.11-jaraco-logging = 3.3.0
BuildRequires: python3.11-jaraco-stream = 3.0.3
BuildRequires: python3.11-jaraco-text = 3.12.0
BuildRequires: python3.11-jeepney = 0.8.0
BuildRequires: python3.11-jinja2 = 3.1.3
BuildRequires: python3.11-jinja2+i18n = 3.1.3
BuildRequires: python3.11-jmespath = 1.0.1
BuildRequires: python3.11-json-log-formatter = 0.5.2
BuildRequires: python3.11-jsonschema = 4.21.1
BuildRequires: python3.11-jsonschema-specifications = 2023.12.1
BuildRequires: python3.11-jwcrypto = 1.5.4
BuildRequires: python3.11-keyring = 24.3.1
BuildRequires: python3.11-kubernetes = 29.0.0
BuildRequires: python3.11-kubernetes+adal = 29.0.0
BuildRequires: python3.11-lockfile = 0.12.2
BuildRequires: python3.11-lxml = 4.9.4
BuildRequires: python3.11-markdown = 3.5.2
BuildRequires: python3.11-markdown-it-py = 3.0.0
BuildRequires: python3.11-markupsafe = 2.1.5
BuildRequires: python3.11-maturin = 1.5.1
BuildRequires: python3.11-mdurl = 0.1.2
BuildRequires: python3.11-more-itertools = 10.2.0
BuildRequires: python3.11-msal = 1.26.0
BuildRequires: python3.11-msal+broker = 1.26.0
BuildRequires: python3.11-msal-extensions = 1.1.0
BuildRequires: python3.11-msgpack = 1.0.5
BuildRequires: python3.11-msrest = 0.7.1
BuildRequires: python3.11-msrest+async = 0.7.1
BuildRequires: python3.11-msrestazure = 0.6.4
BuildRequires: python3.11-multidict = 6.0.5
BuildRequires: python3.11-mypy = 1.9.0
BuildRequires: python3.11-mypy-extensions = 1.0.0
BuildRequires: python3.11-netaddr = 0.8.0
BuildRequires: python3.11-nh3 = 0.2.17
BuildRequires: python3.11-oauthlib = 3.2.2
BuildRequires: python3.11-oauthlib+rsa = 3.2.2
BuildRequires: python3.11-oauthlib+signals = 3.2.2
BuildRequires: python3.11-oauthlib+signedtoken = 3.2.2
BuildRequires: python3.11-openapi-codec = 1.3.2
BuildRequires: python3.11-openshift = 0.13.2
BuildRequires: python3.11-packaging = 23.2
BuildRequires: python3.11-parsley = 1.3
BuildRequires: python3.11-pathspec = 0.12.1
BuildRequires: python3.11-pbr = 6.0.0
BuildRequires: python3.11-pexpect = 4.9.0
BuildRequires: python3.11-pip = 21.2.4
BuildRequires: python3.11-pkgconfig = 1.5.5
BuildRequires: python3.11-pkginfo = 1.10.0
BuildRequires: python3.11-platformdirs = 3.11.0
BuildRequires: python3.11-pluggy = 1.4.0
BuildRequires: python3.11-portalocker = 2.8.2
BuildRequires: python3.11-priority = 1.3.0
BuildRequires: python3.11-prometheus-client = 0.20.0
BuildRequires: python3.11-prometheus-client+twisted = 0.20.0
BuildRequires: python3.11-psutil = 5.9.8
BuildRequires: python3.11-psycopg = 3.1.18
BuildRequires: python3.11-ptyprocess = 0.7.0
BuildRequires: python3.11-pyasn1-modules = 0.5.1
BuildRequires: python3.11-pycares = 4.4.0
BuildRequires: python3.11-pycares+idna = 4.4.0
BuildRequires: python3.11-pycparser = 2.21
BuildRequires: python3.11-pydantic = 2.5.0
BuildRequires: python3.11-pydantic-core = 2.14.1
BuildRequires: python3.11-pygerduty = 0.38.3
BuildRequires: python3.11-pygments = 2.17.2
BuildRequires: python3.11-pyhamcrest = 2.1.0
BuildRequires: python3.11-pyjwt = 2.8.0
BuildRequires: python3.11-pyjwt+crypto = 2.8.0
BuildRequires: python3.11-pyopenssl = 24.0.0
BuildRequires: python3.11-pyparsing = 3.1.2
BuildRequires: python3.11-pyproject-hooks = 1.0.0
BuildRequires: python3.11-pyrad = 2.4
BuildRequires: python3.11-pytest = 8.1.1
BuildRequires: python3.11-pytest-runner = 6.0.1
BuildRequires: python3.11-python3-openid = 3.2.0
BuildRequires: python3.11-python3-saml = 1.16.0
BuildRequires: python3.11-python-daemon = 3.0.1
BuildRequires: python3.11-python-dateutil = 2.9.0^post0
BuildRequires: python3.11-python-dsv-sdk = 1.0.4
BuildRequires: python3.11-python-jose = 3.3.0
BuildRequires: python3.11-python-ldap = 3.4.4
BuildRequires: python3.11-python-ntlm = 1.1.0
BuildRequires: python3.11-python-string-utils = 1.0.0
BuildRequires: python3.11-pytz = 2024.1
BuildRequires: python3.11-pyyaml = 6.0.1
BuildRequires: python3.11-rapidfuzz = 3.7.0
BuildRequires: python3.11-readme-renderer = 43.0
BuildRequires: python3.11-receptorctl = 1.4.4
BuildRequires: python3.11-redis = 5.0.1
BuildRequires: python3.11-referencing = 0.33.0
BuildRequires: python3.11-requests = 2.31.0
BuildRequires: python3.11-requests-oauthlib = 1.3.1
BuildRequires: python3.11-requests-oauthlib+rsa = 1.3.1
BuildRequires: python3.11-requests+socks = 2.31.0
BuildRequires: python3.11-requests-toolbelt = 1.0.0
BuildRequires: python3.11-requests+use-chardet-on-py3 = 2.31.0
BuildRequires: python3.11-requirements-parser = 0.7.0
BuildRequires: python3.11-resolvelib = 1.0.1
BuildRequires: python3.11-rfc3986 = 2.0.0
BuildRequires: python3.11-rfc3986+idna2008 = 2.0.0
BuildRequires: python3.11-rich = 13.7.1
BuildRequires: python3.11-rpds-py = 0.18.0
BuildRequires: python3.11-rsa = 4.9
BuildRequires: python3.11-s3transfer = 0.10.0
BuildRequires: python3.11-scikit-build = 0.17.6
BuildRequires: python3.11-secretstorage = 3.3.3
BuildRequires: python3.11-semantic-version = 2.10.0
BuildRequires: python3.11-service-identity = 24.1.0
BuildRequires: python3.11-setuptools = 69.0.2
BuildRequires: python3.11-setuptools-rust = 1.8.1
BuildRequires: python3.11-setuptools_scm = 8.0.4
BuildRequires: python3.11-setuptools_scm+toml = 8.0.4
BuildRequires: python3.11-setuptools-twine = 0.1.3
BuildRequires: python3.11-shellingham = 1.5.4
BuildRequires: python3.11-simplejson = 3.19.2
BuildRequires: python3.11-six = 1.16.0
BuildRequires: python3.11-slack-sdk = 3.27.0
BuildRequires: python3.11-smmap = 5.0.1
BuildRequires: python3.11-social-auth-app-django = 5.4.0
BuildRequires: python3.11-social-auth-core = 4.4.2
BuildRequires: python3.11-social-auth-core+all = 4.4.2
BuildRequires: python3.11-social-auth-core+allpy3 = 4.4.2
BuildRequires: python3.11-social-auth-core+azuread = 4.4.2
BuildRequires: python3.11-social-auth-core+openidconnect = 4.4.2
BuildRequires: python3.11-social-auth-core+saml = 4.4.2
BuildRequires: python3.11-sqlparse = 0.4.4
BuildRequires: python3.11-tacacs-plus = 1.0
BuildRequires: python3.11-tempora = 5.5.1
BuildRequires: python3.11-tomli = 2.0.1
BuildRequires: python3.11-tomlkit = 0.12.4
BuildRequires: python3.11-trove-classifiers = 2024.3.25
BuildRequires: python3.11-twilio = 8.13.0
BuildRequires: python3.11-twine = 5.0.0
BuildRequires: python3.11-twisted = 23.10.0
BuildRequires: python3.11-twisted+http2 = 23.10.0
BuildRequires: python3.11-twisted+tls = 23.10.0
BuildRequires: python3.11-txaio = 23.1.1
BuildRequires: python3.11-types-psutil = 5.9.5.20240316
BuildRequires: python3.11-types-setuptools = 69.2.0.20240317
BuildRequires: python3.11-typing-extensions = 4.9.0
BuildRequires: python3.11-uritemplate = 4.1.1
BuildRequires: python3.11-urllib3 = 1.26.18
BuildRequires: python3.11-uwsgi = 2.0.24
BuildRequires: python3.11-uwsgitop = 0.11
BuildRequires: python3.11-versioneer = 0.29
BuildRequires: python3.11-versioneer+toml = 0.29
BuildRequires: python3.11-virtualenv = 20.25.1
BuildRequires: python3.11-websocket-client = 1.7.0
BuildRequires: python3.11-xmlsec = 1.3.13
BuildRequires: python3.11-yarl = 1.9.4
BuildRequires: python3.11-zipp = 3.17.0
BuildRequires: python3.11-zope-interface = 6.2
BuildRequires: python3.11-pyasn1 

Requires: python%{python3_pkgversion} nodejs >= 18 npm gettext git nginx redis xmlsec1-openssl xmlsec1 podman sscg awx-receptor libpq 
Requires: python3.11-adal = 1.2.7
Requires: python3.11-aiodns = 3.1.1
Requires: python3.11-aiohttp = 3.9.3
Requires: python3.11-aiohttp-retry = 2.8.3
Requires: python3.11-aiohttp+speedups = 3.9.3
Requires: python3.11-aioredis = 1.3.1
Requires: python3.11-aiosignal = 1.3.1
Requires: python3.11-annotated-types = 0.6.0
Requires: python3.11-ansible-builder = 3.0.1
Requires: python3.11-ansible-runner = 2.3.6
Requires: python3.11-ansiconv = 1.0.0
Requires: python3.11-asciichartpy = 1.5.25
Requires: python3.11-asgiref = 3.7.2
Requires: python3.11-asn1 = 2.7.0
Requires: python3.11-asyncpg = 0.29.0
Requires: python3.11-async-timeout = 4.0.3
Requires: python3.11-attrs = 23.2.0
Requires: python3.11-autobahn = 23.6.2
Requires: python3.11-autocommand = 2.2.2
Requires: python3.11-automat = 22.10.0
Requires: python3.11-awscrt = 0.16.9
Requires: python3.11-azure-common = 1.1.28
Requires: python3.11-azure-core = 1.30.0
Requires: python3.11-azure-core+aio = 1.30.0
Requires: python3.11-azure-identity = 1.15.0
Requires: python3.11-azure-keyvault = 4.2.0
Requires: python3.11-azure-keyvault-certificates = 4.7.0
Requires: python3.11-azure-keyvault-keys = 4.8.0
Requires: python3.11-azure-keyvault-secrets = 4.7.0
Requires: python3.11-babel = 2.14.0
Requires: python3.11-bcrypt = 4.1.2
Requires: python3.11-bcrypt+tests = 4.1.2
Requires: python3.11-bcrypt+typecheck = 4.1.2
Requires: python3.11-bindep = 2.11.0
Requires: python3.11-blinker = 1.7.0
Requires: python3.11-boto3 = 1.34.47
Requires: python3.11-botocore = 1.34.47
Requires: python3.11-brotli = 1.1.0
Requires: python3.11-build = 1.2.1
Requires: python3.11-cachecontrol = 0.14.0
Requires: python3.11-cachecontrol+filecache = 0.14.0
Requires: python3.11-cachetools = 5.3.2
Requires: python3.11-calver = 2022.6.26
Requires: python3.11-cffi = 1.16.0
Requires: python3.11-channels = 3.0.5
Requires: python3.11-channels-redis = 3.4.1
Requires: python3.11-chardet = 5.2.0
Requires: python3.11-charset-normalizer = 3.3.2
Requires: python3.11-cleo = 2.1.0
Requires: python3.11-click = 8.1.7
Requires: python3.11-constantly = 23.10.4
Requires: python3.11-coreapi = 2.3.3
Requires: python3.11-coreschema = 0.0.4
Requires: python3.11-crashtest = 0.4.1
Requires: python3.11-cryptography = 41.0.7
Requires: python3.11-cython = 0.29.37
Requires: python3.11-daphne = 3.0.2
Requires: python3.11-defusedxml = 0.7.1
Requires: python3.11-distlib = 0.3.8
Requires: python3.11-distro = 1.9.0
Requires: python3.11-django = 4.2.6
Requires: python3.11-django-ansible-base = 20240212
Requires: python3.11-django-ansible-base+jwt_consumer = 20240212
Requires: python3.11-django-ansible-base+rest_filters = 20240212
Requires: python3.11-django-auth-ldap = 4.7.0
Requires: python3.11-django+bcrypt = 4.2.6
Requires: python3.11-django-cors-headers = 4.3.1
Requires: python3.11-django-crum = 0.7.9
Requires: python3.11-django-debug-toolbar = 4.3.0
Requires: python3.11-django-extensions = 3.2.3
Requires: python3.11-django-guid = 3.2.1
Requires: python3.11-django-oauth-toolkit = 1.7.1
Requires: python3.11-django-pglocks = 1.0.4
Requires: python3.11-django-polymorphic = 3.1.0
Requires: python3.11-django-radius = 1.5.0
Requires: python3.11-djangorestframework = 3.14.0
Requires: python3.11-djangorestframework-yaml = 2.0.0
Requires: python3.11-django-rest-swagger = 2.2.0
Requires: python3.11-django-solo = 2.2.0
Requires: python3.11-django-split-settings = 1.0.0
Requires: python3.11-dm-xmlsec-binding = 2.2
Requires: python3.11-docutils = 0.20.1
Requires: python3.11-drf-yasg = 1.21.7
Requires: python3.11-dulwich = 0.21.7
Requires: python3.11-ecdsa = 0.18.0
Requires: python3.11-enum-compat = 0.0.3
Requires: python3.11-expandvars = 0.12.0
Requires: python3.11-fastjsonschema = 2.19.1
Requires: python3.11-filelock = 3.13.1
Requires: python3.11-freezegun = 1.4.0
Requires: python3.11-frozenlist = 1.4.1
Requires: python3.11-future = 0.16.0
Requires: python3.11-gitdb = 4.0.11
Requires: python3.11-gitpython = 3.1.42
Requires: python3.11-google-auth = 2.28.1
Requires: python3.11-h2 = 4.1.0
Requires: python3.11-hatch-fancy-pypi-readme = 24.1.0
Requires: python3.11-hatchling = 1.22.4
Requires: python3.11-hatch-vcs = 0.4.0
Requires: python3.11-hiredis = 2.0.0
Requires: python3.11-hpack = 4.0.0
Requires: python3.11-hyperframe = 6.0.1
Requires: python3.11-hyperlink = 21.0.0
Requires: python3.11-idna = 3.6
Requires: python3.11-importlib-metadata = 6.2.1
Requires: python3.11-incremental = 22.10.0
Requires: python3.11-inflect = 7.0.0
Requires: python3.11-inflection = 0.5.1
Requires: python3.11-installer = 0.7.0
Requires: python3.11-irc = 20.3.1
Requires: python3.11-isodate = 0.6.1
Requires: python3.11-itypes = 1.2.0
Requires: python3.11-jaraco-classes = 3.3.1
Requires: python3.11-jaraco-collections = 5.0.0
Requires: python3.11-jaraco-context = 4.3.0
Requires: python3.11-jaraco-functools = 4.0.0
Requires: python3.11-jaraco-logging = 3.3.0
Requires: python3.11-jaraco-stream = 3.0.3
Requires: python3.11-jaraco-text = 3.12.0
Requires: python3.11-jeepney = 0.8.0
Requires: python3.11-jinja2 = 3.1.3
Requires: python3.11-jinja2+i18n = 3.1.3
Requires: python3.11-jmespath = 1.0.1
Requires: python3.11-json-log-formatter = 0.5.2
Requires: python3.11-jsonschema = 4.21.1
Requires: python3.11-jsonschema-specifications = 2023.12.1
Requires: python3.11-jwcrypto = 1.5.4
Requires: python3.11-keyring = 24.3.1
Requires: python3.11-kubernetes = 29.0.0
Requires: python3.11-kubernetes+adal = 29.0.0
Requires: python3.11-lockfile = 0.12.2
Requires: python3.11-lxml = 4.9.4
Requires: python3.11-markdown = 3.5.2
Requires: python3.11-markdown-it-py = 3.0.0
Requires: python3.11-markupsafe = 2.1.5
Requires: python3.11-maturin = 1.5.1
Requires: python3.11-mdurl = 0.1.2
Requires: python3.11-more-itertools = 10.2.0
Requires: python3.11-msal = 1.26.0
Requires: python3.11-msal+broker = 1.26.0
Requires: python3.11-msal-extensions = 1.1.0
Requires: python3.11-msgpack = 1.0.5
Requires: python3.11-msrest = 0.7.1
Requires: python3.11-msrest+async = 0.7.1
Requires: python3.11-msrestazure = 0.6.4
Requires: python3.11-multidict = 6.0.5
Requires: python3.11-mypy = 1.9.0
Requires: python3.11-mypy-extensions = 1.0.0
Requires: python3.11-netaddr = 0.8.0
Requires: python3.11-nh3 = 0.2.17
Requires: python3.11-oauthlib = 3.2.2
Requires: python3.11-oauthlib+rsa = 3.2.2
Requires: python3.11-oauthlib+signals = 3.2.2
Requires: python3.11-oauthlib+signedtoken = 3.2.2
Requires: python3.11-openapi-codec = 1.3.2
Requires: python3.11-openshift = 0.13.2
Requires: python3.11-packaging = 23.2
Requires: python3.11-parsley = 1.3
Requires: python3.11-pathspec = 0.12.1
Requires: python3.11-pbr = 6.0.0
Requires: python3.11-pexpect = 4.9.0
Requires: python3.11-pip = 21.2.4
Requires: python3.11-pkgconfig = 1.5.5
Requires: python3.11-pkginfo = 1.10.0
Requires: python3.11-platformdirs = 3.11.0
Requires: python3.11-pluggy = 1.4.0
Requires: python3.11-portalocker = 2.8.2
Requires: python3.11-priority = 1.3.0
Requires: python3.11-prometheus-client = 0.20.0
Requires: python3.11-prometheus-client+twisted = 0.20.0
Requires: python3.11-psutil = 5.9.8
Requires: python3.11-psycopg = 3.1.18
Requires: python3.11-ptyprocess = 0.7.0
Requires: python3.11-pyasn1-modules = 0.5.1
Requires: python3.11-pycares = 4.4.0
Requires: python3.11-pycares+idna = 4.4.0
Requires: python3.11-pycparser = 2.21
Requires: python3.11-pydantic = 2.5.0
Requires: python3.11-pydantic-core = 2.14.1
Requires: python3.11-pygerduty = 0.38.3
Requires: python3.11-pygments = 2.17.2
Requires: python3.11-pyhamcrest = 2.1.0
Requires: python3.11-pyjwt = 2.8.0
Requires: python3.11-pyjwt+crypto = 2.8.0
Requires: python3.11-pyopenssl = 24.0.0
Requires: python3.11-pyparsing = 3.1.2
Requires: python3.11-pyproject-hooks = 1.0.0
Requires: python3.11-pyrad = 2.4
Requires: python3.11-pytest = 8.1.1
Requires: python3.11-pytest-runner = 6.0.1
Requires: python3.11-python3-openid = 3.2.0
Requires: python3.11-python3-saml = 1.16.0
Requires: python3.11-python-daemon = 3.0.1
Requires: python3.11-python-dateutil = 2.9.0^post0
Requires: python3.11-python-dsv-sdk = 1.0.4
Requires: python3.11-python-jose = 3.3.0
Requires: python3.11-python-ldap = 3.4.4
Requires: python3.11-python-ntlm = 1.1.0
Requires: python3.11-python-string-utils = 1.0.0
Requires: python3.11-pytz = 2024.1
Requires: python3.11-pyyaml = 6.0.1
Requires: python3.11-rapidfuzz = 3.7.0
Requires: python3.11-readme-renderer = 43.0
Requires: python3.11-receptorctl = 1.4.4
Requires: python3.11-redis = 5.0.1
Requires: python3.11-referencing = 0.33.0
Requires: python3.11-requests = 2.31.0
Requires: python3.11-requests-oauthlib = 1.3.1
Requires: python3.11-requests-oauthlib+rsa = 1.3.1
Requires: python3.11-requests+socks = 2.31.0
Requires: python3.11-requests-toolbelt = 1.0.0
Requires: python3.11-requests+use-chardet-on-py3 = 2.31.0
Requires: python3.11-requirements-parser = 0.7.0
Requires: python3.11-resolvelib = 1.0.1
Requires: python3.11-rfc3986 = 2.0.0
Requires: python3.11-rfc3986+idna2008 = 2.0.0
Requires: python3.11-rich = 13.7.1
Requires: python3.11-rpds-py = 0.18.0
Requires: python3.11-rsa = 4.9
Requires: python3.11-s3transfer = 0.10.0
Requires: python3.11-scikit-build = 0.17.6
Requires: python3.11-secretstorage = 3.3.3
Requires: python3.11-semantic-version = 2.10.0
Requires: python3.11-service-identity = 24.1.0
Requires: python3.11-setuptools = 69.0.2
Requires: python3.11-setuptools-rust = 1.8.1
Requires: python3.11-setuptools_scm = 8.0.4
Requires: python3.11-setuptools_scm+toml = 8.0.4
Requires: python3.11-setuptools-twine = 0.1.3
Requires: python3.11-shellingham = 1.5.4
Requires: python3.11-simplejson = 3.19.2
Requires: python3.11-six = 1.16.0
Requires: python3.11-slack-sdk = 3.27.0
Requires: python3.11-smmap = 5.0.1
Requires: python3.11-social-auth-app-django = 5.4.0
Requires: python3.11-social-auth-core = 4.4.2
Requires: python3.11-social-auth-core+all = 4.4.2
Requires: python3.11-social-auth-core+allpy3 = 4.4.2
Requires: python3.11-social-auth-core+azuread = 4.4.2
Requires: python3.11-social-auth-core+openidconnect = 4.4.2
Requires: python3.11-social-auth-core+saml = 4.4.2
Requires: python3.11-sqlparse = 0.4.4
Requires: python3.11-tacacs-plus = 1.0
Requires: python3.11-tempora = 5.5.1
Requires: python3.11-tomli = 2.0.1
Requires: python3.11-tomlkit = 0.12.4
Requires: python3.11-trove-classifiers = 2024.3.25
Requires: python3.11-twilio = 8.13.0
Requires: python3.11-twine = 5.0.0
Requires: python3.11-twisted = 23.10.0
Requires: python3.11-twisted+http2 = 23.10.0
Requires: python3.11-twisted+tls = 23.10.0
Requires: python3.11-txaio = 23.1.1
Requires: python3.11-types-psutil = 5.9.5.20240316
Requires: python3.11-types-setuptools = 69.2.0.20240317
Requires: python3.11-typing-extensions = 4.9.0
Requires: python3.11-uritemplate = 4.1.1
Requires: python3.11-urllib3 = 1.26.18
Requires: python3.11-uwsgi = 2.0.24
Requires: python3.11-uwsgitop = 0.11
Requires: python3.11-versioneer = 0.29
Requires: python3.11-versioneer+toml = 0.29
Requires: python3.11-virtualenv = 20.25.1
Requires: python3.11-websocket-client = 1.7.0
Requires: python3.11-xmlsec = 1.3.13
Requires: python3.11-yarl = 1.9.4
Requires: python3.11-zipp = 3.17.0
Requires: python3.11-zope-interface = 6.2
Requires: python3.11-pyasn1 

%{?systemd_requires}

%description
%{summary}

%prep
%setup -q -n awx
git checkout -f devel
git checkout -f %{version}
%patch0 -p0

%build

%install
echo 'node-options="--openssl-legacy-provider"' >> awx/ui/.npmrc
GIT_BRANCH=%{version} VERSION=%{version} python%{python3_pkgversion} -m build -s
make ui-next/src
cp %{_sourcedir}/awx-rpm-logo.svg-%{version} awx/ui_next/src/frontend/awx/main/awx-rpm-logo.svg
sed -i "s/awx-logo.svg/awx-rpm-logo.svg/g" awx/ui_next/src/frontend/awx/main/AwxMasthead.tsx
make ui-next
make ui-release

mkdir -p /var/log/tower
AWX_SETTINGS_FILE=awx/settings/production.py SKIP_SECRET_KEY_CHECK=yes SKIP_PG_VERSION_CHECK=yes python%{python3_pkgversion} manage.py collectstatic --noinput --clear
mkdir -p %{buildroot}%{_prefix}
for i in `find -type f |grep mappings.wasm`; do
	echo "Removing $i"
	rm -f $i
done
cp dist/awx-*.tar.gz %{buildroot}%{_prefix}/
pushd %{buildroot}%{_prefix}
tar zxvf awx-*.tar.gz
rm awx-*.tar.gz
mv awx-*/* .
rm -rf awx-*
pip%{python3_pkgversion} install --root=%{buildroot}/ .
popd
sed -i "s|/builddir.*.x86_64||g" $RPM_BUILD_ROOT/usr/bin/awx-manage
pushd %{buildroot}/usr/lib/python%{python3_pkgversion}/site-packages/
for i in `find -type f`; do
	sed -i "s|/builddir.*.x86_64||g" $i
done
popd

rsync -avr awx/ $RPM_BUILD_ROOT/opt/awx-rpm/awx/
cp -a /var/lib/awx/public/static /opt/awx-rpm/

mkdir -p $RPM_BUILD_ROOT/var/lib/awx/rsyslog
mkdir -p $RPM_BUILD_ROOT/var/lib/awx/projects
mkdir -p $RPM_BUILD_ROOT/var/lib/awx/job_status

# Collect django static
mkdir -p /var/log/tower/
mkdir -p %{buildroot}%{service_homedir}
mkdir -p %{buildroot}%{service_logdir}
mkdir -p %{buildroot}%{_prefix}/bin
mkdir -p %{buildroot}%{service_configdir}
echo %{version} > %{buildroot}%{service_homedir}/.tower_version

cp %{_sourcedir}/settings.py-%{version} %{buildroot}%{service_configdir}/settings.py
mkdir -p %{buildroot}%{_prefix}/public
rsync -avr /var/lib/awx/public/ %{buildroot}%{_prefix}/public/

mkdir -p %{buildroot}/usr/lib/systemd/system
# awx-channels-worker awx
for service in awx-web awx-wsrelay awx-ws-heartbeat awx-daphne awx-dispatcher awx-receiver awx-receptor awx-receptor-hop awx-receptor-worker; do
    cp %{_sourcedir}/${service}.service-%{version} %{buildroot}/usr/lib/systemd/system/${service}.service
done

cp %{_sourcedir}/awx.target-%{version} %{buildroot}/usr/lib/systemd/system/awx.target

mkdir -p %{buildroot}/etc/receptor

for receptor in receptor receptor-hop receptor-worker; do
	cp %{_sourcedir}/$receptor.conf-%{version} %{buildroot}/etc/receptor/$receptor.conf
done

mkdir -p %{buildroot}/etc/nginx/conf.d

cp %{_sourcedir}/awx-rpm-nginx.conf-%{version} %{buildroot}/etc/nginx/conf.d/awx-rpm.conf

# Create Virtualenv folder
mkdir -p %{buildroot}%{service_homedir}/venv

# Install docs
#cp %{_sourcedir}/nginx.conf.example ./

# Install VENV Script
#cp %{_sourcedir}/awx-create-venv $RPM_BUILD_ROOT/opt/rh/rh-python36/root/usr/bin/
#mkdir -p $RPM_BUILD_ROOT/usr/bin/

mkdir -p $RPM_BUILD_ROOT/etc/nginx/conf.d/

sed -i "s/supervisor_service_command(command='restart', service='awx-rsyslogd')//g" $RPM_BUILD_ROOT/usr/lib/python%{python3_pkgversion}/site-packages/awx/main/utils/external_logging.py

%pre
/usr/bin/getent group %{service_group} >/dev/null || /usr/sbin/groupadd --system %{service_group}
/usr/bin/getent passwd %{service_user} >/dev/null || /usr/sbin/useradd --no-create-home --system -g %{service_group} --home-dir %{service_homedir} -s /bin/bash %{service_user}
/usr/sbin/usermod -s /bin/bash %{service_user}
/usr/bin/gpasswd -a awx redis

%post
if [ ! -f /etc/nginx/nginx.crt ];then
sscg -q --cert-file /etc/nginx/nginx.crt --cert-key-file /etc/nginx/nginx.key --ca-file /etc/nginx/ca.crt --lifetime 3650 --hostname $HOSTNAME --email root@$HOSTNAME
fi

%preun

%postun

%clean

%files
%defattr(0644, awx, awx, 0755)
%attr(0755, root, root) /usr/bin/awx-manage
%attr(0755, root, root) /usr/lib/systemd/system/*.service
%attr(0755, root, root) /usr/lib/python3.9/site-packages/awx*
%attr(0755, awx, awx) %{_prefix}
%dir %attr(0750, %{service_user}, %{service_group}) %{service_homedir}
%dir %attr(0750, %{service_user}, %{service_group}) %{service_homedir}/venv
%{service_homedir}/.tower_version
%dir %attr(0770, %{service_user}, %{service_group}) %{service_logdir}
%config %{service_configdir}/settings.py
%config /etc/nginx/conf.d/awx-rpm.conf
/usr/lib/systemd/system/awx.target
/etc/receptor/receptor-hop.conf
/etc/receptor/receptor-worker.conf
/etc/receptor/receptor.conf
/etc/receptor
#/usr/bin/ansible-tower-service
#/usr/bin/ansible-tower-setup
#/usr/bin/awx-python
#/usr/bin/failure-event-handler
#/usr/share/awx
#/usr/share/sosreport/sos/plugins/tower.py
#/var/lib/awx/favicon.ico
#/var/lib/awx/wsgi.py
/var/lib/awx/rsyslog
/var/lib/awx/projects
/var/lib/awx/job_status

%if 0%{?el7}
%attr(0644, root, root) %{_unitdir}/awx-cbreceiver.service
%attr(0644, root, root) %{_unitdir}/awx-dispatcher.service
%attr(0644, root, root) %{_unitdir}/awx-channels-worker.service
%attr(0644, root, root) %{_unitdir}/awx-daphne.service
%attr(0644, root, root) %{_unitdir}/awx-web.service
%attr(0644, root, root) %{_unitdir}/awx.service
%endif

%changelog
* Wed Apr 03 2024 08:56:52 AM CEST +0200 Martin Juhl <m@rtinjuhl.dk> 24.1.0
- New version build: 24.1.0

