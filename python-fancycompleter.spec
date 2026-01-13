%define module fancycompleter

Name:		python-fancycompleter
Version:	0.11.1
Release:	1
Summary:	Colorful TAB completion for Python prompt
URL:		https://pypi.org/project/fancycompleter/
License:	BSD
Group:		Development/Python
Source0:	https://files.pythonhosted.org/packages/source/f/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(pyrepl)
BuildRequires:	python%{pyver}dist(wheel)

%description
Colorful TAB completion for Python prompt.

%prep
%autosetup -p1 -n %{module}-%{version}
# Remove bundled egg-info
rm -rf %{module}.egg-info

%files
%doc README.md
%license LICENSE
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}.dist-info
