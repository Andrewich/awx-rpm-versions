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
Version: 24.6.1
Release: 4%{dist}
Source: https://github.com/ansible/awx/archive/refs/tags/%{version}.tar.gz
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
Patch1: awx-rpm-extract-strings.patch-%{version}
Patch2: awx-rpm-branding.patch-%{version}
License: GPLv3
Group: AWX
URL: https://awx.wiki
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}.buildroot
Vendor: AWX
Prefix: %{_prefix}
AutoReqProv: false

BuildRequires: make python%{python3_pkgversion} python%{python3_pkgversion}-devel nodejs npm gettext git python%{python3_pkgversion}-build rsync libpq libpq-devel 
BuildRequires: python%{python3_pkgversion}-adal = 1.2.7
BuildRequires: python%{python3_pkgversion}-aiodns = 3.2.0
BuildRequires: python%{python3_pkgversion}-aiohttp = 3.9.5
BuildRequires: python%{python3_pkgversion}-aiohttp-retry = 2.8.3
BuildRequires: python%{python3_pkgversion}-aiohttp+speedups = 3.9.5
BuildRequires: python%{python3_pkgversion}-aioredis = 1.3.1
BuildRequires: python%{python3_pkgversion}-aiosignal = 1.3.1
BuildRequires: python%{python3_pkgversion}-annotated-types = 0.6.0
BuildRequires: python%{python3_pkgversion}-ansible-builder = 3.1.0
BuildRequires: python%{python3_pkgversion}-ansible-runner = 2.4.0
BuildRequires: python%{python3_pkgversion}-ansiconv = 1.0.0
BuildRequires: python%{python3_pkgversion}-asciichartpy = 1.5.25
BuildRequires: python%{python3_pkgversion}-asgiref = 3.7.2
BuildRequires: python%{python3_pkgversion}-asn1 = 2.7.0
BuildRequires: python%{python3_pkgversion}-async-timeout = 4.0.3
BuildRequires: python%{python3_pkgversion}-attrs = 23.2.0
BuildRequires: python%{python3_pkgversion}-autobahn = 23.6.2
BuildRequires: python%{python3_pkgversion}-autocommand = 2.2.2
BuildRequires: python%{python3_pkgversion}-automat = 22.10.0
BuildRequires: python%{python3_pkgversion}-awscrt = 0.16.9
BuildRequires: python%{python3_pkgversion}-azure-common = 1.1.28
BuildRequires: python%{python3_pkgversion}-azure-core = 1.30.0
BuildRequires: python%{python3_pkgversion}-azure-core+aio = 1.30.0
BuildRequires: python%{python3_pkgversion}-azure-identity = 1.15.0
BuildRequires: python%{python3_pkgversion}-azure-keyvault = 4.2.0
BuildRequires: python%{python3_pkgversion}-azure-keyvault-certificates = 4.7.0
BuildRequires: python%{python3_pkgversion}-azure-keyvault-keys = 4.8.0
BuildRequires: python%{python3_pkgversion}-azure-keyvault-secrets = 4.7.0
BuildRequires: python%{python3_pkgversion}-babel = 2.15.0
BuildRequires: python%{python3_pkgversion}-bcrypt = 4.1.3
BuildRequires: python%{python3_pkgversion}-bcrypt+tests = 4.1.3
BuildRequires: python%{python3_pkgversion}-bcrypt+typecheck = 4.1.3
BuildRequires: python%{python3_pkgversion}-bindep = 2.11.0
BuildRequires: python%{python3_pkgversion}-blinker = 1.8.2
BuildRequires: python%{python3_pkgversion}-boto3 = 1.34.47
BuildRequires: python%{python3_pkgversion}-botocore = 1.34.47
BuildRequires: python%{python3_pkgversion}-brotli = 1.1.0
BuildRequires: python%{python3_pkgversion}-build = 1.2.1
BuildRequires: python%{python3_pkgversion}-cachecontrol = 0.14.0
BuildRequires: python%{python3_pkgversion}-cachecontrol+filecache = 0.14.0
BuildRequires: python%{python3_pkgversion}-cachetools = 5.3.2
BuildRequires: python%{python3_pkgversion}-calver = 2022.6.26
BuildRequires: python%{python3_pkgversion}-certifi = 2024.7.4
BuildRequires: python%{python3_pkgversion}-cffi = 1.16.0
BuildRequires: python%{python3_pkgversion}-channels = 3.0.5
BuildRequires: python%{python3_pkgversion}-channels-redis = 3.4.1
BuildRequires: python%{python3_pkgversion}-chardet = 5.2.0
BuildRequires: python%{python3_pkgversion}-charset-normalizer = 3.3.2
BuildRequires: python%{python3_pkgversion}-cleo = 2.1.0
BuildRequires: python%{python3_pkgversion}-click = 8.1.7
BuildRequires: python%{python3_pkgversion}-constantly = 23.10.4
BuildRequires: python%{python3_pkgversion}-coreapi = 2.3.3
BuildRequires: python%{python3_pkgversion}-coreschema = 0.0.4
BuildRequires: python%{python3_pkgversion}-crashtest = 0.4.1
BuildRequires: python%{python3_pkgversion}-cryptography = 41.0.7
BuildRequires: python%{python3_pkgversion}-cython = 0.29.37
BuildRequires: python%{python3_pkgversion}-daphne = 3.0.2
BuildRequires: python%{python3_pkgversion}-defusedxml = 0.7.1
BuildRequires: python%{python3_pkgversion}-deprecated = 1.2.14
BuildRequires: python%{python3_pkgversion}-distlib = 0.3.8
BuildRequires: python%{python3_pkgversion}-distro = 1.9.0
BuildRequires: python%{python3_pkgversion}-django = 4.2.10
BuildRequires: python%{python3_pkgversion}-django-ansible-base = 20240701
BuildRequires: python%{python3_pkgversion}-django-ansible-base+jwt_consumer = 20240701
BuildRequires: python%{python3_pkgversion}-django-ansible-base+rest_filters = 20240701
BuildRequires: python%{python3_pkgversion}-django-auth-ldap = 4.8.0
BuildRequires: python%{python3_pkgversion}-django+bcrypt = 4.2.10
BuildRequires: python%{python3_pkgversion}-django-cors-headers = 4.3.1
BuildRequires: python%{python3_pkgversion}-django-crum = 0.7.9
BuildRequires: python%{python3_pkgversion}-django-debug-toolbar = 4.4.2
BuildRequires: python%{python3_pkgversion}-django-extensions = 3.2.3
BuildRequires: python%{python3_pkgversion}-django-guid = 3.2.1
BuildRequires: python%{python3_pkgversion}-django-oauth-toolkit = 1.7.1
BuildRequires: python%{python3_pkgversion}-django-pglocks = 1.0.4
BuildRequires: python%{python3_pkgversion}-django-polymorphic = 3.1.0
BuildRequires: python%{python3_pkgversion}-django-radius = 1.5.1
BuildRequires: python%{python3_pkgversion}-djangorestframework = 3.15.1
BuildRequires: python%{python3_pkgversion}-djangorestframework-yaml = 2.0.0
BuildRequires: python%{python3_pkgversion}-django-rest-swagger = 2.2.0
BuildRequires: python%{python3_pkgversion}-django-solo = 2.2.0
BuildRequires: python%{python3_pkgversion}-django-split-settings = 1.0.0
BuildRequires: python%{python3_pkgversion}-dm-xmlsec-binding = 3.0
BuildRequires: python%{python3_pkgversion}-docutils = 0.20.1
BuildRequires: python%{python3_pkgversion}-drf-yasg = 1.21.7
BuildRequires: python%{python3_pkgversion}-drf-yasg+coreapi = 1.21.7
BuildRequires: python%{python3_pkgversion}-drf-yasg+validation = 1.21.7
BuildRequires: python%{python3_pkgversion}-dulwich = 0.21.7
BuildRequires: python%{python3_pkgversion}-ecdsa = 0.18.0
BuildRequires: python%{python3_pkgversion}-enum-compat = 0.0.3
BuildRequires: python%{python3_pkgversion}-expandvars = 0.12.0
BuildRequires: python%{python3_pkgversion}-fastjsonschema = 2.20.0
BuildRequires: python%{python3_pkgversion}-filelock = 3.13.1
BuildRequires: python%{python3_pkgversion}-freezegun = 1.5.1
BuildRequires: python%{python3_pkgversion}-frozenlist = 1.4.1
BuildRequires: python%{python3_pkgversion}-gitdb = 4.0.11
BuildRequires: python%{python3_pkgversion}-gitpython = 3.1.42
BuildRequires: python%{python3_pkgversion}-googleapis-common-protos = 1.63.0
BuildRequires: python%{python3_pkgversion}-google-auth = 2.28.1
BuildRequires: python%{python3_pkgversion}-grpcio = 1.64.1
BuildRequires: python%{python3_pkgversion}-h2 = 4.1.0
BuildRequires: python%{python3_pkgversion}-hatch-fancy-pypi-readme = 24.1.0
BuildRequires: python%{python3_pkgversion}-hatchling = 1.25.0
BuildRequires: python%{python3_pkgversion}-hatch-vcs = 0.4.0
BuildRequires: python%{python3_pkgversion}-hiredis = 2.0.0
BuildRequires: python%{python3_pkgversion}-hpack = 4.0.0
BuildRequires: python%{python3_pkgversion}-hyperframe = 6.0.1
BuildRequires: python%{python3_pkgversion}-hyperlink = 21.0.0
BuildRequires: python%{python3_pkgversion}-idna = 3.6
BuildRequires: python%{python3_pkgversion}-importlib-metadata = 6.2.1
BuildRequires: python%{python3_pkgversion}-importlib-resources = 6.4.0
BuildRequires: python%{python3_pkgversion}-incremental = 22.10.0
BuildRequires: python%{python3_pkgversion}-inflect = 7.0.0
BuildRequires: python%{python3_pkgversion}-inflection = 0.5.1
BuildRequires: python%{python3_pkgversion}-installer = 0.7.0
BuildRequires: python%{python3_pkgversion}-irc = 20.3.1
BuildRequires: python%{python3_pkgversion}-isodate = 0.6.1
BuildRequires: python%{python3_pkgversion}-itypes = 1.2.0
BuildRequires: python%{python3_pkgversion}-jaraco-classes = 3.4.0
BuildRequires: python%{python3_pkgversion}-jaraco-collections = 5.0.0
BuildRequires: python%{python3_pkgversion}-jaraco-context = 4.3.0
BuildRequires: python%{python3_pkgversion}-jaraco-functools = 4.0.0
BuildRequires: python%{python3_pkgversion}-jaraco-logging = 3.3.0
BuildRequires: python%{python3_pkgversion}-jaraco-stream = 3.0.3
BuildRequires: python%{python3_pkgversion}-jaraco-text = 3.12.0
BuildRequires: python%{python3_pkgversion}-jeepney = 0.8.0
BuildRequires: python%{python3_pkgversion}-jinja2 = 3.1.3
BuildRequires: python%{python3_pkgversion}-jinja2+i18n = 3.1.3
BuildRequires: python%{python3_pkgversion}-jmespath = 1.0.1
BuildRequires: python%{python3_pkgversion}-json-log-formatter = 0.5.2
BuildRequires: python%{python3_pkgversion}-jsonschema = 4.21.1
BuildRequires: python%{python3_pkgversion}-jsonschema-specifications = 2023.12.1
BuildRequires: python%{python3_pkgversion}-jwcrypto = 1.5.4
BuildRequires: python%{python3_pkgversion}-keyring = 24.3.1
BuildRequires: python%{python3_pkgversion}-kubernetes = 29.0.0
BuildRequires: python%{python3_pkgversion}-kubernetes+adal = 29.0.0
BuildRequires: python%{python3_pkgversion}-lockfile = 0.12.2
BuildRequires: python%{python3_pkgversion}-markdown = 3.5.2
BuildRequires: python%{python3_pkgversion}-markdown-it-py = 3.0.0
BuildRequires: python%{python3_pkgversion}-markupsafe = 2.1.5
BuildRequires: python%{python3_pkgversion}-maturin = 1.6.0
BuildRequires: python%{python3_pkgversion}-mdurl = 0.1.2
BuildRequires: python%{python3_pkgversion}-more-itertools = 10.2.0
BuildRequires: python%{python3_pkgversion}-msal = 1.26.0
BuildRequires: python%{python3_pkgversion}-msal+broker = 1.26.0
BuildRequires: python%{python3_pkgversion}-msal-extensions = 1.1.0
BuildRequires: python%{python3_pkgversion}-msgpack = 1.0.5
BuildRequires: python%{python3_pkgversion}-msrest = 0.7.1
BuildRequires: python%{python3_pkgversion}-msrest+async = 0.7.1
BuildRequires: python%{python3_pkgversion}-msrestazure = 0.6.4
BuildRequires: python%{python3_pkgversion}-multidict = 6.0.5
BuildRequires: python%{python3_pkgversion}-mypy = 1.10.1
BuildRequires: python%{python3_pkgversion}-mypy-extensions = 1.0.0
BuildRequires: python%{python3_pkgversion}-netaddr = 0.8.0
BuildRequires: python%{python3_pkgversion}-nh3 = 0.2.17
BuildRequires: python%{python3_pkgversion}-oauthlib = 3.2.2
BuildRequires: python%{python3_pkgversion}-oauthlib+rsa = 3.2.2
BuildRequires: python%{python3_pkgversion}-oauthlib+signals = 3.2.2
BuildRequires: python%{python3_pkgversion}-oauthlib+signedtoken = 3.2.2
BuildRequires: python%{python3_pkgversion}-openapi-codec = 1.3.2
BuildRequires: python%{python3_pkgversion}-openshift = 0.13.2
BuildRequires: python%{python3_pkgversion}-opentelemetry-api = 1.24.0
BuildRequires: python%{python3_pkgversion}-opentelemetry-exporter-otlp = 1.24.0
BuildRequires: python%{python3_pkgversion}-opentelemetry-exporter-otlp-proto-common = 1.24.0
BuildRequires: python%{python3_pkgversion}-opentelemetry-exporter-otlp-proto-grpc = 1.24.0
BuildRequires: python%{python3_pkgversion}-opentelemetry-exporter-otlp-proto-http = 1.24.0
BuildRequires: python%{python3_pkgversion}-opentelemetry-instrumentation = 0.45b0
BuildRequires: python%{python3_pkgversion}-opentelemetry-instrumentation-logging = 0.45b0
BuildRequires: python%{python3_pkgversion}-opentelemetry-proto = 1.24.0
BuildRequires: python%{python3_pkgversion}-opentelemetry-sdk = 1.24.0
BuildRequires: python%{python3_pkgversion}-opentelemetry-semantic-conventions = 0.45b0
BuildRequires: python%{python3_pkgversion}-packaging = 23.2
BuildRequires: python%{python3_pkgversion}-parsley = 1.3
BuildRequires: python%{python3_pkgversion}-pathspec = 0.12.1
BuildRequires: python%{python3_pkgversion}-pbr = 6.0.0
BuildRequires: python%{python3_pkgversion}-pexpect = 4.9.0
BuildRequires: python%{python3_pkgversion}-pkgconfig = 1.5.5
BuildRequires: python%{python3_pkgversion}-pkginfo = 1.11.1
BuildRequires: python%{python3_pkgversion}-platformdirs = 3.11.0
BuildRequires: python%{python3_pkgversion}-pluggy = 1.5.0
BuildRequires: python%{python3_pkgversion}-portalocker = 2.8.2
BuildRequires: python%{python3_pkgversion}-priority = 1.3.0
BuildRequires: python%{python3_pkgversion}-prometheus-client = 0.20.0
BuildRequires: python%{python3_pkgversion}-prometheus-client+twisted = 0.20.0
BuildRequires: python%{python3_pkgversion}-protobuf = 4.25.3
BuildRequires: python%{python3_pkgversion}-psutil = 5.9.8
BuildRequires: python%{python3_pkgversion}-psycopg = 3.1.18
BuildRequires: python%{python3_pkgversion}-ptyprocess = 0.7.0
BuildRequires: python%{python3_pkgversion}-pyasn1-modules = 0.5.1
BuildRequires: python%{python3_pkgversion}-pycares = 4.4.0
BuildRequires: python%{python3_pkgversion}-pycares+idna = 4.4.0
BuildRequires: python%{python3_pkgversion}-pycparser = 2.21
BuildRequires: python%{python3_pkgversion}-pydantic = 2.5.0
BuildRequires: python%{python3_pkgversion}-pydantic-core = 2.14.1
BuildRequires: python%{python3_pkgversion}-pygerduty = 0.38.3
BuildRequires: python%{python3_pkgversion}-pygments = 2.18.0
BuildRequires: python%{python3_pkgversion}-pyhamcrest = 2.1.0
BuildRequires: python%{python3_pkgversion}-pyjwt = 2.8.0
BuildRequires: python%{python3_pkgversion}-pyjwt+crypto = 2.8.0
BuildRequires: python%{python3_pkgversion}-pyopenssl = 24.0.0
BuildRequires: python%{python3_pkgversion}-pyparsing = 3.1.2
BuildRequires: python%{python3_pkgversion}-pyproject-hooks = 1.1.0
BuildRequires: python%{python3_pkgversion}-pyrad = 2.4
BuildRequires: python%{python3_pkgversion}-pytest = 8.2.2
BuildRequires: python%{python3_pkgversion}-pytest-runner = 6.0.1
BuildRequires: python%{python3_pkgversion}-python3-openid = 3.2.0
BuildRequires: python%{python3_pkgversion}-python3-saml = 1.16.0
BuildRequires: python%{python3_pkgversion}-python-daemon = 3.0.1
BuildRequires: python%{python3_pkgversion}-python-dateutil = 2.9.0.post0
BuildRequires: python%{python3_pkgversion}-python-dsv-sdk = 1.0.4
BuildRequires: python%{python3_pkgversion}-python-jose = 3.3.0
BuildRequires: python%{python3_pkgversion}-python-ldap = 3.4.4
BuildRequires: python%{python3_pkgversion}-python-ntlm = 1.1.0
BuildRequires: python%{python3_pkgversion}-python-string-utils = 1.0.0
BuildRequires: python%{python3_pkgversion}-pytz = 2024.1
BuildRequires: python%{python3_pkgversion}-pyyaml = 6.0.1
BuildRequires: python%{python3_pkgversion}-pyzstd = 0.16.0
BuildRequires: python%{python3_pkgversion}-rapidfuzz = 3.9.3
BuildRequires: python%{python3_pkgversion}-readme-renderer = 43.0
BuildRequires: python%{python3_pkgversion}-receptorctl = 1.4.4
BuildRequires: python%{python3_pkgversion}-redis = 5.0.1
BuildRequires: python%{python3_pkgversion}-referencing = 0.33.0
BuildRequires: python%{python3_pkgversion}-requests = 2.31.0
BuildRequires: python%{python3_pkgversion}-requests-oauthlib = 1.3.1
BuildRequires: python%{python3_pkgversion}-requests-oauthlib+rsa = 1.3.1
BuildRequires: python%{python3_pkgversion}-requests+socks = 2.31.0
BuildRequires: python%{python3_pkgversion}-requests-toolbelt = 1.0.0
BuildRequires: python%{python3_pkgversion}-requirements-parser = 0.9.0
BuildRequires: python%{python3_pkgversion}-resolvelib = 1.0.1
BuildRequires: python%{python3_pkgversion}-rfc3986 = 2.0.0
BuildRequires: python%{python3_pkgversion}-rfc3986+idna2008 = 2.0.0
BuildRequires: python%{python3_pkgversion}-rich = 13.7.1
BuildRequires: python%{python3_pkgversion}-rpds-py = 0.18.0
BuildRequires: python%{python3_pkgversion}-rsa = 4.9
BuildRequires: python%{python3_pkgversion}-s3transfer = 0.10.0
BuildRequires: python%{python3_pkgversion}-scikit-build = 0.17.6
BuildRequires: python%{python3_pkgversion}-secretstorage = 3.3.3
BuildRequires: python%{python3_pkgversion}-semantic-version = 2.10.0
BuildRequires: python%{python3_pkgversion}-service-identity = 24.1.0
BuildRequires: python%{python3_pkgversion}-setuptools = 69.0.2
BuildRequires: python%{python3_pkgversion}-setuptools-rust = 1.8.1
BuildRequires: python%{python3_pkgversion}-setuptools_scm = 8.0.4
BuildRequires: python%{python3_pkgversion}-setuptools_scm+toml = 8.0.4
BuildRequires: python%{python3_pkgversion}-setuptools-twine = 0.1.3
BuildRequires: python%{python3_pkgversion}-shellingham = 1.5.4
BuildRequires: python%{python3_pkgversion}-simplejson = 3.19.2
BuildRequires: python%{python3_pkgversion}-six = 1.16.0
BuildRequires: python%{python3_pkgversion}-slack-sdk = 3.27.0
BuildRequires: python%{python3_pkgversion}-smmap = 5.0.1
BuildRequires: python%{python3_pkgversion}-social-auth-app-django = 5.4.0
BuildRequires: python%{python3_pkgversion}-social-auth-core = 4.4.2
BuildRequires: python%{python3_pkgversion}-social-auth-core+all = 4.4.2
BuildRequires: python%{python3_pkgversion}-social-auth-core+allpy3 = 4.4.2
BuildRequires: python%{python3_pkgversion}-social-auth-core+azuread = 4.4.2
BuildRequires: python%{python3_pkgversion}-social-auth-core+openidconnect = 4.4.2
BuildRequires: python%{python3_pkgversion}-social-auth-core+saml = 4.4.2
BuildRequires: python%{python3_pkgversion}-sqlparse = 0.4.4
BuildRequires: python%{python3_pkgversion}-swagger-spec-validator = 3.0.4
BuildRequires: python%{python3_pkgversion}-tacacs-plus = 1.0
BuildRequires: python%{python3_pkgversion}-tempora = 5.5.1
BuildRequires: python%{python3_pkgversion}-tomli = 2.0.1
BuildRequires: python%{python3_pkgversion}-tomlkit = 0.12.5
BuildRequires: python%{python3_pkgversion}-trove-classifiers = 2024.7.2
BuildRequires: python%{python3_pkgversion}-twilio = 8.13.0
BuildRequires: python%{python3_pkgversion}-twine = 5.1.1
BuildRequires: python%{python3_pkgversion}-twisted = 23.10.0
BuildRequires: python%{python3_pkgversion}-twisted+http2 = 23.10.0
BuildRequires: python%{python3_pkgversion}-twisted+tls = 23.10.0
BuildRequires: python%{python3_pkgversion}-txaio = 23.1.1
BuildRequires: python%{python3_pkgversion}-types-psutil = 6.0.0.20240621
BuildRequires: python%{python3_pkgversion}-types-setuptools = 70.1.0.20240627
BuildRequires: python%{python3_pkgversion}-typing-extensions = 4.9.0
BuildRequires: python%{python3_pkgversion}-uritemplate = 4.1.1
BuildRequires: python%{python3_pkgversion}-urllib3 = 1.26.18
BuildRequires: python%{python3_pkgversion}-uwsgi = 2.0.26
BuildRequires: python%{python3_pkgversion}-uwsgitop = 0.11
BuildRequires: python%{python3_pkgversion}-versioneer = 0.29
BuildRequires: python%{python3_pkgversion}-versioneer+toml = 0.29
BuildRequires: python%{python3_pkgversion}-virtualenv = 20.26.3
BuildRequires: python%{python3_pkgversion}-websocket-client = 1.7.0
BuildRequires: python%{python3_pkgversion}-wrapt = 1.16.0
BuildRequires: python%{python3_pkgversion}-xmlsec = 1.3.13
BuildRequires: python%{python3_pkgversion}-yarl = 1.9.4
BuildRequires: python%{python3_pkgversion}-zipp = 3.17.0
BuildRequires: python%{python3_pkgversion}-zope-interface = 6.2
BuildRequires: python%{python3_pkgversion}-pyasn1 python3.11-pip 

Requires: python%{python3_pkgversion} nodejs >= 18 npm gettext git nginx redis xmlsec1-openssl xmlsec1 podman sscg awx-receptor libpq 
Requires: python%{python3_pkgversion}-adal = 1.2.7
Requires: python%{python3_pkgversion}-aiodns = 3.2.0
Requires: python%{python3_pkgversion}-aiohttp = 3.9.5
Requires: python%{python3_pkgversion}-aiohttp-retry = 2.8.3
Requires: python%{python3_pkgversion}-aiohttp+speedups = 3.9.5
Requires: python%{python3_pkgversion}-aioredis = 1.3.1
Requires: python%{python3_pkgversion}-aiosignal = 1.3.1
Requires: python%{python3_pkgversion}-annotated-types = 0.6.0
Requires: python%{python3_pkgversion}-ansible-builder = 3.1.0
Requires: python%{python3_pkgversion}-ansible-runner = 2.4.0
Requires: python%{python3_pkgversion}-ansiconv = 1.0.0
Requires: python%{python3_pkgversion}-asciichartpy = 1.5.25
Requires: python%{python3_pkgversion}-asgiref = 3.7.2
Requires: python%{python3_pkgversion}-asn1 = 2.7.0
Requires: python%{python3_pkgversion}-async-timeout = 4.0.3
Requires: python%{python3_pkgversion}-attrs = 23.2.0
Requires: python%{python3_pkgversion}-autobahn = 23.6.2
Requires: python%{python3_pkgversion}-autocommand = 2.2.2
Requires: python%{python3_pkgversion}-automat = 22.10.0
Requires: python%{python3_pkgversion}-awscrt = 0.16.9
Requires: python%{python3_pkgversion}-azure-common = 1.1.28
Requires: python%{python3_pkgversion}-azure-core = 1.30.0
Requires: python%{python3_pkgversion}-azure-core+aio = 1.30.0
Requires: python%{python3_pkgversion}-azure-identity = 1.15.0
Requires: python%{python3_pkgversion}-azure-keyvault = 4.2.0
Requires: python%{python3_pkgversion}-azure-keyvault-certificates = 4.7.0
Requires: python%{python3_pkgversion}-azure-keyvault-keys = 4.8.0
Requires: python%{python3_pkgversion}-azure-keyvault-secrets = 4.7.0
Requires: python%{python3_pkgversion}-babel = 2.15.0
Requires: python%{python3_pkgversion}-bcrypt = 4.1.3
Requires: python%{python3_pkgversion}-bcrypt+tests = 4.1.3
Requires: python%{python3_pkgversion}-bcrypt+typecheck = 4.1.3
Requires: python%{python3_pkgversion}-bindep = 2.11.0
Requires: python%{python3_pkgversion}-blinker = 1.8.2
Requires: python%{python3_pkgversion}-boto3 = 1.34.47
Requires: python%{python3_pkgversion}-botocore = 1.34.47
Requires: python%{python3_pkgversion}-brotli = 1.1.0
Requires: python%{python3_pkgversion}-build = 1.2.1
Requires: python%{python3_pkgversion}-cachecontrol = 0.14.0
Requires: python%{python3_pkgversion}-cachecontrol+filecache = 0.14.0
Requires: python%{python3_pkgversion}-cachetools = 5.3.2
Requires: python%{python3_pkgversion}-calver = 2022.6.26
Requires: python%{python3_pkgversion}-certifi = 2024.7.4
Requires: python%{python3_pkgversion}-cffi = 1.16.0
Requires: python%{python3_pkgversion}-channels = 3.0.5
Requires: python%{python3_pkgversion}-channels-redis = 3.4.1
Requires: python%{python3_pkgversion}-chardet = 5.2.0
Requires: python%{python3_pkgversion}-charset-normalizer = 3.3.2
Requires: python%{python3_pkgversion}-cleo = 2.1.0
Requires: python%{python3_pkgversion}-click = 8.1.7
Requires: python%{python3_pkgversion}-constantly = 23.10.4
Requires: python%{python3_pkgversion}-coreapi = 2.3.3
Requires: python%{python3_pkgversion}-coreschema = 0.0.4
Requires: python%{python3_pkgversion}-crashtest = 0.4.1
Requires: python%{python3_pkgversion}-cryptography = 41.0.7
Requires: python%{python3_pkgversion}-cython = 0.29.37
Requires: python%{python3_pkgversion}-daphne = 3.0.2
Requires: python%{python3_pkgversion}-defusedxml = 0.7.1
Requires: python%{python3_pkgversion}-deprecated = 1.2.14
Requires: python%{python3_pkgversion}-distlib = 0.3.8
Requires: python%{python3_pkgversion}-distro = 1.9.0
Requires: python%{python3_pkgversion}-django = 4.2.10
Requires: python%{python3_pkgversion}-django-ansible-base = 20240701
Requires: python%{python3_pkgversion}-django-ansible-base+jwt_consumer = 20240701
Requires: python%{python3_pkgversion}-django-ansible-base+rest_filters = 20240701
Requires: python%{python3_pkgversion}-django-auth-ldap = 4.8.0
Requires: python%{python3_pkgversion}-django+bcrypt = 4.2.10
Requires: python%{python3_pkgversion}-django-cors-headers = 4.3.1
Requires: python%{python3_pkgversion}-django-crum = 0.7.9
Requires: python%{python3_pkgversion}-django-debug-toolbar = 4.4.2
Requires: python%{python3_pkgversion}-django-extensions = 3.2.3
Requires: python%{python3_pkgversion}-django-guid = 3.2.1
Requires: python%{python3_pkgversion}-django-oauth-toolkit = 1.7.1
Requires: python%{python3_pkgversion}-django-pglocks = 1.0.4
Requires: python%{python3_pkgversion}-django-polymorphic = 3.1.0
Requires: python%{python3_pkgversion}-django-radius = 1.5.1
Requires: python%{python3_pkgversion}-djangorestframework = 3.15.1
Requires: python%{python3_pkgversion}-djangorestframework-yaml = 2.0.0
Requires: python%{python3_pkgversion}-django-rest-swagger = 2.2.0
Requires: python%{python3_pkgversion}-django-solo = 2.2.0
Requires: python%{python3_pkgversion}-django-split-settings = 1.0.0
Requires: python%{python3_pkgversion}-dm-xmlsec-binding = 3.0
Requires: python%{python3_pkgversion}-docutils = 0.20.1
Requires: python%{python3_pkgversion}-drf-yasg = 1.21.7
Requires: python%{python3_pkgversion}-drf-yasg+coreapi = 1.21.7
Requires: python%{python3_pkgversion}-drf-yasg+validation = 1.21.7
Requires: python%{python3_pkgversion}-dulwich = 0.21.7
Requires: python%{python3_pkgversion}-ecdsa = 0.18.0
Requires: python%{python3_pkgversion}-enum-compat = 0.0.3
Requires: python%{python3_pkgversion}-expandvars = 0.12.0
Requires: python%{python3_pkgversion}-fastjsonschema = 2.20.0
Requires: python%{python3_pkgversion}-filelock = 3.13.1
Requires: python%{python3_pkgversion}-freezegun = 1.5.1
Requires: python%{python3_pkgversion}-frozenlist = 1.4.1
Requires: python%{python3_pkgversion}-gitdb = 4.0.11
Requires: python%{python3_pkgversion}-gitpython = 3.1.42
Requires: python%{python3_pkgversion}-googleapis-common-protos = 1.63.0
Requires: python%{python3_pkgversion}-google-auth = 2.28.1
Requires: python%{python3_pkgversion}-grpcio = 1.64.1
Requires: python%{python3_pkgversion}-h2 = 4.1.0
Requires: python%{python3_pkgversion}-hatch-fancy-pypi-readme = 24.1.0
Requires: python%{python3_pkgversion}-hatchling = 1.25.0
Requires: python%{python3_pkgversion}-hatch-vcs = 0.4.0
Requires: python%{python3_pkgversion}-hiredis = 2.0.0
Requires: python%{python3_pkgversion}-hpack = 4.0.0
Requires: python%{python3_pkgversion}-hyperframe = 6.0.1
Requires: python%{python3_pkgversion}-hyperlink = 21.0.0
Requires: python%{python3_pkgversion}-idna = 3.6
Requires: python%{python3_pkgversion}-importlib-metadata = 6.2.1
Requires: python%{python3_pkgversion}-importlib-resources = 6.4.0
Requires: python%{python3_pkgversion}-incremental = 22.10.0
Requires: python%{python3_pkgversion}-inflect = 7.0.0
Requires: python%{python3_pkgversion}-inflection = 0.5.1
Requires: python%{python3_pkgversion}-installer = 0.7.0
Requires: python%{python3_pkgversion}-irc = 20.3.1
Requires: python%{python3_pkgversion}-isodate = 0.6.1
Requires: python%{python3_pkgversion}-itypes = 1.2.0
Requires: python%{python3_pkgversion}-jaraco-classes = 3.4.0
Requires: python%{python3_pkgversion}-jaraco-collections = 5.0.0
Requires: python%{python3_pkgversion}-jaraco-context = 4.3.0
Requires: python%{python3_pkgversion}-jaraco-functools = 4.0.0
Requires: python%{python3_pkgversion}-jaraco-logging = 3.3.0
Requires: python%{python3_pkgversion}-jaraco-stream = 3.0.3
Requires: python%{python3_pkgversion}-jaraco-text = 3.12.0
Requires: python%{python3_pkgversion}-jeepney = 0.8.0
Requires: python%{python3_pkgversion}-jinja2 = 3.1.3
Requires: python%{python3_pkgversion}-jinja2+i18n = 3.1.3
Requires: python%{python3_pkgversion}-jmespath = 1.0.1
Requires: python%{python3_pkgversion}-json-log-formatter = 0.5.2
Requires: python%{python3_pkgversion}-jsonschema = 4.21.1
Requires: python%{python3_pkgversion}-jsonschema-specifications = 2023.12.1
Requires: python%{python3_pkgversion}-jwcrypto = 1.5.4
Requires: python%{python3_pkgversion}-keyring = 24.3.1
Requires: python%{python3_pkgversion}-kubernetes = 29.0.0
Requires: python%{python3_pkgversion}-kubernetes+adal = 29.0.0
Requires: python%{python3_pkgversion}-lockfile = 0.12.2
Requires: python%{python3_pkgversion}-markdown = 3.5.2
Requires: python%{python3_pkgversion}-markdown-it-py = 3.0.0
Requires: python%{python3_pkgversion}-markupsafe = 2.1.5
Requires: python%{python3_pkgversion}-maturin = 1.6.0
Requires: python%{python3_pkgversion}-mdurl = 0.1.2
Requires: python%{python3_pkgversion}-more-itertools = 10.2.0
Requires: python%{python3_pkgversion}-msal = 1.26.0
Requires: python%{python3_pkgversion}-msal+broker = 1.26.0
Requires: python%{python3_pkgversion}-msal-extensions = 1.1.0
Requires: python%{python3_pkgversion}-msgpack = 1.0.5
Requires: python%{python3_pkgversion}-msrest = 0.7.1
Requires: python%{python3_pkgversion}-msrest+async = 0.7.1
Requires: python%{python3_pkgversion}-msrestazure = 0.6.4
Requires: python%{python3_pkgversion}-multidict = 6.0.5
Requires: python%{python3_pkgversion}-mypy = 1.10.1
Requires: python%{python3_pkgversion}-mypy-extensions = 1.0.0
Requires: python%{python3_pkgversion}-netaddr = 0.8.0
Requires: python%{python3_pkgversion}-nh3 = 0.2.17
Requires: python%{python3_pkgversion}-oauthlib = 3.2.2
Requires: python%{python3_pkgversion}-oauthlib+rsa = 3.2.2
Requires: python%{python3_pkgversion}-oauthlib+signals = 3.2.2
Requires: python%{python3_pkgversion}-oauthlib+signedtoken = 3.2.2
Requires: python%{python3_pkgversion}-openapi-codec = 1.3.2
Requires: python%{python3_pkgversion}-openshift = 0.13.2
Requires: python%{python3_pkgversion}-opentelemetry-api = 1.24.0
Requires: python%{python3_pkgversion}-opentelemetry-exporter-otlp = 1.24.0
Requires: python%{python3_pkgversion}-opentelemetry-exporter-otlp-proto-common = 1.24.0
Requires: python%{python3_pkgversion}-opentelemetry-exporter-otlp-proto-grpc = 1.24.0
Requires: python%{python3_pkgversion}-opentelemetry-exporter-otlp-proto-http = 1.24.0
Requires: python%{python3_pkgversion}-opentelemetry-instrumentation = 0.45b0
Requires: python%{python3_pkgversion}-opentelemetry-instrumentation-logging = 0.45b0
Requires: python%{python3_pkgversion}-opentelemetry-proto = 1.24.0
Requires: python%{python3_pkgversion}-opentelemetry-sdk = 1.24.0
Requires: python%{python3_pkgversion}-opentelemetry-semantic-conventions = 0.45b0
Requires: python%{python3_pkgversion}-packaging = 23.2
Requires: python%{python3_pkgversion}-parsley = 1.3
Requires: python%{python3_pkgversion}-pathspec = 0.12.1
Requires: python%{python3_pkgversion}-pbr = 6.0.0
Requires: python%{python3_pkgversion}-pexpect = 4.9.0
Requires: python%{python3_pkgversion}-pkgconfig = 1.5.5
Requires: python%{python3_pkgversion}-pkginfo = 1.11.1
Requires: python%{python3_pkgversion}-platformdirs = 3.11.0
Requires: python%{python3_pkgversion}-pluggy = 1.5.0
Requires: python%{python3_pkgversion}-portalocker = 2.8.2
Requires: python%{python3_pkgversion}-priority = 1.3.0
Requires: python%{python3_pkgversion}-prometheus-client = 0.20.0
Requires: python%{python3_pkgversion}-prometheus-client+twisted = 0.20.0
Requires: python%{python3_pkgversion}-protobuf = 4.25.3
Requires: python%{python3_pkgversion}-psutil = 5.9.8
Requires: python%{python3_pkgversion}-psycopg = 3.1.18
Requires: python%{python3_pkgversion}-ptyprocess = 0.7.0
Requires: python%{python3_pkgversion}-pyasn1-modules = 0.5.1
Requires: python%{python3_pkgversion}-pycares = 4.4.0
Requires: python%{python3_pkgversion}-pycares+idna = 4.4.0
Requires: python%{python3_pkgversion}-pycparser = 2.21
Requires: python%{python3_pkgversion}-pydantic = 2.5.0
Requires: python%{python3_pkgversion}-pydantic-core = 2.14.1
Requires: python%{python3_pkgversion}-pygerduty = 0.38.3
Requires: python%{python3_pkgversion}-pygments = 2.18.0
Requires: python%{python3_pkgversion}-pyhamcrest = 2.1.0
Requires: python%{python3_pkgversion}-pyjwt = 2.8.0
Requires: python%{python3_pkgversion}-pyjwt+crypto = 2.8.0
Requires: python%{python3_pkgversion}-pyopenssl = 24.0.0
Requires: python%{python3_pkgversion}-pyparsing = 3.1.2
Requires: python%{python3_pkgversion}-pyproject-hooks = 1.1.0
Requires: python%{python3_pkgversion}-pyrad = 2.4
Requires: python%{python3_pkgversion}-pytest = 8.2.2
Requires: python%{python3_pkgversion}-pytest-runner = 6.0.1
Requires: python%{python3_pkgversion}-python3-openid = 3.2.0
Requires: python%{python3_pkgversion}-python3-saml = 1.16.0
Requires: python%{python3_pkgversion}-python-daemon = 3.0.1
Requires: python%{python3_pkgversion}-python-dateutil = 2.9.0.post0
Requires: python%{python3_pkgversion}-python-dsv-sdk = 1.0.4
Requires: python%{python3_pkgversion}-python-jose = 3.3.0
Requires: python%{python3_pkgversion}-python-ldap = 3.4.4
Requires: python%{python3_pkgversion}-python-ntlm = 1.1.0
Requires: python%{python3_pkgversion}-python-string-utils = 1.0.0
Requires: python%{python3_pkgversion}-pytz = 2024.1
Requires: python%{python3_pkgversion}-pyyaml = 6.0.1
Requires: python%{python3_pkgversion}-pyzstd = 0.16.0
Requires: python%{python3_pkgversion}-rapidfuzz = 3.9.3
Requires: python%{python3_pkgversion}-readme-renderer = 43.0
Requires: python%{python3_pkgversion}-receptorctl = 1.4.4
Requires: python%{python3_pkgversion}-redis = 5.0.1
Requires: python%{python3_pkgversion}-referencing = 0.33.0
Requires: python%{python3_pkgversion}-requests = 2.31.0
Requires: python%{python3_pkgversion}-requests-oauthlib = 1.3.1
Requires: python%{python3_pkgversion}-requests-oauthlib+rsa = 1.3.1
Requires: python%{python3_pkgversion}-requests+socks = 2.31.0
Requires: python%{python3_pkgversion}-requests-toolbelt = 1.0.0
Requires: python%{python3_pkgversion}-requirements-parser = 0.9.0
Requires: python%{python3_pkgversion}-resolvelib = 1.0.1
Requires: python%{python3_pkgversion}-rfc3986 = 2.0.0
Requires: python%{python3_pkgversion}-rfc3986+idna2008 = 2.0.0
Requires: python%{python3_pkgversion}-rich = 13.7.1
Requires: python%{python3_pkgversion}-rpds-py = 0.18.0
Requires: python%{python3_pkgversion}-rsa = 4.9
Requires: python%{python3_pkgversion}-s3transfer = 0.10.0
Requires: python%{python3_pkgversion}-scikit-build = 0.17.6
Requires: python%{python3_pkgversion}-secretstorage = 3.3.3
Requires: python%{python3_pkgversion}-semantic-version = 2.10.0
Requires: python%{python3_pkgversion}-service-identity = 24.1.0
Requires: python%{python3_pkgversion}-setuptools = 69.0.2
Requires: python%{python3_pkgversion}-setuptools-rust = 1.8.1
Requires: python%{python3_pkgversion}-setuptools_scm = 8.0.4
Requires: python%{python3_pkgversion}-setuptools_scm+toml = 8.0.4
Requires: python%{python3_pkgversion}-setuptools-twine = 0.1.3
Requires: python%{python3_pkgversion}-shellingham = 1.5.4
Requires: python%{python3_pkgversion}-simplejson = 3.19.2
Requires: python%{python3_pkgversion}-six = 1.16.0
Requires: python%{python3_pkgversion}-slack-sdk = 3.27.0
Requires: python%{python3_pkgversion}-smmap = 5.0.1
Requires: python%{python3_pkgversion}-social-auth-app-django = 5.4.0
Requires: python%{python3_pkgversion}-social-auth-core = 4.4.2
Requires: python%{python3_pkgversion}-social-auth-core+all = 4.4.2
Requires: python%{python3_pkgversion}-social-auth-core+allpy3 = 4.4.2
Requires: python%{python3_pkgversion}-social-auth-core+azuread = 4.4.2
Requires: python%{python3_pkgversion}-social-auth-core+openidconnect = 4.4.2
Requires: python%{python3_pkgversion}-social-auth-core+saml = 4.4.2
Requires: python%{python3_pkgversion}-sqlparse = 0.4.4
Requires: python%{python3_pkgversion}-swagger-spec-validator = 3.0.4
Requires: python%{python3_pkgversion}-tacacs-plus = 1.0
Requires: python%{python3_pkgversion}-tempora = 5.5.1
Requires: python%{python3_pkgversion}-tomli = 2.0.1
Requires: python%{python3_pkgversion}-tomlkit = 0.12.5
Requires: python%{python3_pkgversion}-trove-classifiers = 2024.7.2
Requires: python%{python3_pkgversion}-twilio = 8.13.0
Requires: python%{python3_pkgversion}-twine = 5.1.1
Requires: python%{python3_pkgversion}-twisted = 23.10.0
Requires: python%{python3_pkgversion}-twisted+http2 = 23.10.0
Requires: python%{python3_pkgversion}-twisted+tls = 23.10.0
Requires: python%{python3_pkgversion}-txaio = 23.1.1
Requires: python%{python3_pkgversion}-types-psutil = 6.0.0.20240621
Requires: python%{python3_pkgversion}-types-setuptools = 70.1.0.20240627
Requires: python%{python3_pkgversion}-typing-extensions = 4.9.0
Requires: python%{python3_pkgversion}-uritemplate = 4.1.1
Requires: python%{python3_pkgversion}-urllib3 = 1.26.18
Requires: python%{python3_pkgversion}-uwsgi = 2.0.26
Requires: python%{python3_pkgversion}-uwsgitop = 0.11
Requires: python%{python3_pkgversion}-versioneer = 0.29
Requires: python%{python3_pkgversion}-versioneer+toml = 0.29
Requires: python%{python3_pkgversion}-virtualenv = 20.26.3
Requires: python%{python3_pkgversion}-websocket-client = 1.7.0
Requires: python%{python3_pkgversion}-wrapt = 1.16.0
Requires: python%{python3_pkgversion}-xmlsec = 1.3.13
Requires: python%{python3_pkgversion}-yarl = 1.9.4
Requires: python%{python3_pkgversion}-zipp = 3.17.0
Requires: python%{python3_pkgversion}-zope-interface = 6.2
Requires: python%{python3_pkgversion}-pyasn1 python3.11-pip 

%{?systemd_requires}

%description
%{summary}

%prep
%setup -q -n awx
git checkout -f devel
git checkout -f %{version}
%patch0 -p0
%patch1 -p0
%patch2 -p0

%build

%install
mkdir translations/
mv awx/locale/en-us/LC_MESSAGES/django.po translations/
mv awx/ui/src/locales/en/messages.po translations/

echo 'node-options="--openssl-legacy-provider"' >> awx/ui/.npmrc
GIT_BRANCH=%{version} VERSION=%{version} python%{python3_pkgversion} -m build -s
make ui-next/src
cp %{_sourcedir}/awx-rpm-logo.svg-%{version} awx/ui_next/src/frontend/awx/main/awx-rpm-logo.svg
sed -i "s/awx-logo.svg/awx-rpm-logo.svg/g" awx/ui_next/src/frontend/awx/main/AwxMasthead.tsx
make ui-next
make ui-release

mkdir -p /var/log/tower
AWX_SETTINGS_FILE=awx/settings/production.py SKIP_SECRET_KEY_CHECK=yes SKIP_PG_VERSION_CHECK=yes python%{python3_pkgversion} manage.py collectstatic --noinput --clear

chmod +x tools/scripts/l18n/post_translation.sh
./tools/scripts/l18n/post_translation.sh

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
%attr(0755, root, root) /usr/lib/python%{python3_pkgversion}/site-packages/awx*
%attr(0755, awx, awx) %{_prefix}
%dir %attr(0750, %{service_user}, %{service_group}) %{service_homedir}
%dir %attr(0750, %{service_user}, %{service_group}) %{service_homedir}/venv
%{service_homedir}/.tower_version
%dir %attr(0770, %{service_user}, %{service_group}) %{service_logdir}
%config(noreplace) %{service_configdir}/settings.py
%config /etc/nginx/conf.d/awx-rpm.conf
/usr/lib/systemd/system/awx.target
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

%changelog
* Fri Jul 05 2024 01:04:10 PM CEST +0200 Martin Juhl <m@rtinjuhl.dk> 24.6.1
- New version build: 24.6.1
- (HEAD, tag: 24.6.1) Prevent assigning credential to user of other org (#15296)
- Add in missing read permissions for organization audit role (#15318)
- Added new OpenShift Virtualization inventory source to docs. (#15299)
- Add better 403 error message for Job template create (#15307)
- Add better error message for wfjt create 403 (#15309)
- Fix server error from DAB ValidationError with strings (#15312)
- Update ExecutionEnvironment model so object-level roles work with DAB RBAC system (#15289)
- Do not use cache in github image build action (#15308)
- Fix permissions that come from an external auditor role (#15291)
- LISTENER_DATABASES clobbers DATABASES OPTIONS (#15306)
- Add TASK_MANAGER_LOCK_TIMEOUT (#15300)
- Make attached user models adhere to new API assignments (#15298)
- Temporary workaround for CI failure (#15305)
- Added troubleshooting and tips tricks content (#15212)
- Various RBAC fixes related to managed RoleDefinitions (#15287)
