# Created by pyp2rpm-3.3.5
%global module fuzzywuzzy

Name:		python-%{module}
Version:	0.18.0
Release:	3
Summary:	Fuzzy string matching in python
Group:		Development/Python
License:	GPL-2.0-only
URL:		https://github.com/seatgeek/fuzzywuzzy
Source0:	https://files.pythonhosted.org/packages/source/o/%{module}/%{module}-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	pkgconfig(python3)
BuildRequires:	python-levenshtein >= 0.12
BuildRequires:	python-setuptools
BuildRequires:	python-pycodestyle
BuildRequires:	python-pytest

%description
FuzzyWuzzy Fuzzy string matching like a boss. It uses Levenshtein Distance < to
calculate the differences between sequences in a simple-to-use
package.Requirements - Python 2.7 or higher - difflib - python-Levenshtein <
(optional, provides a 4-10x speedup in String Matching, though may result in
differing results for certain cases <

%prep
%autosetup -n %{module}-%{version}
# Remove shebangs
sed -i '1{/^#!/d}' fuzzywuzzy/*.py

%build
%py3_build

%install
%py3_install

%check
python test_fuzzywuzzy.py

%files -n python-%{module}
%{python3_sitelib}/%{module}/
%{python3_sitelib}/%{module}-%{version}-py%{python3_version}.egg-info
%doc README.rst
%license LICENSE.txt
