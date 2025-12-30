%define module fancycompleter

Name:		python-fancycompleter
Version:	0.9.1
Release:	3
Summary:	Colorful TAB completion for Python prompt
URL:		https://pypi.org/project/fancycompleter/
License:	BSD
Group:		Development/Python
Source0:	https://files.pythonhosted.org/packages/source/f/fancycompleter/fancycompleter-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch

BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(pyrepl)
BuildRequires:	python%{pyver}dist(setupmeta)


%description
Colorful TAB completion for Python prompt.

%prep
%autosetup -p1 -n %{module}-%{version}

%build
%py_build

%install
%py3_install

%files
%{py_sitedir}/%{module}.py
%{py_sitedir}/%{module}-%{version}*.*-info
%doc README.md
