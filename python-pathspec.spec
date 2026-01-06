# Copyright 2026 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-pathspec
Epoch: 100
Version: 0.12.1
Release: 1%{?dist}
BuildArch: noarch
Summary: Utility library for gitignore style pattern matching of file paths
License: MPL-2.0
URL: https://github.com/cpburnz/python-pathspec/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-pip

%description
Path Specification (pathspec) is a utility library for pattern matching
of file paths. So far this only includes Git's wildmatch pattern
matching which itself is derived from Rsync's wildmatch. Git uses
wildmatch for its gitignore files.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
pip wheel \
    --no-deps \
    --no-build-isolation \
    --wheel-dir=dist \
    .

%install
pip install \
    --no-deps \
    --ignore-installed \
    --root=%{buildroot} \
    --prefix=%{_prefix} \
    dist/*.whl
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-pathspec
Summary: Utility library for gitignore style pattern matching of file paths
Requires: python3
Provides: python3-pathspec = %{epoch}:%{version}-%{release}
Provides: python3dist(pathspec) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pathspec = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pathspec) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pathspec = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pathspec) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-pathspec
Path Specification (pathspec) is a utility library for pattern matching
of file paths. So far this only includes Git's wildmatch pattern
matching which itself is derived from Rsync's wildmatch. Git uses
wildmatch for its gitignore files.

%files -n python%{python3_version_nodots}-pathspec
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-pathspec
Summary: Utility library for gitignore style pattern matching of file paths
Requires: python3
Provides: python3-pathspec = %{epoch}:%{version}-%{release}
Provides: python3dist(pathspec) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pathspec = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pathspec) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pathspec = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pathspec) = %{epoch}:%{version}-%{release}

%description -n python3-pathspec
Path Specification (pathspec) is a utility library for pattern matching
of file paths. So far this only includes Git's wildmatch pattern
matching which itself is derived from Rsync's wildmatch. Git uses
wildmatch for its gitignore files.

%files -n python3-pathspec
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
