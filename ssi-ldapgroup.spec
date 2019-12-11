Name:           ssi-ldapgroup
Summary:        scripts to interact with ldap groups for SSI
Version:        0.1.0
Release:        0%{?dist}
Group:          Applications/System
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Source0:        %{name}-%{version}-%{release}.tar.gz
BuildArch:      noarch

Requires:       python PyYAML
BuildRequires:  python python-setuptools
Vendor:         ECF-SSI
License:        Artistic 2.0
URL:            http://www.fnal.gov/

%description
Scripts to add/remove/list users in LDAP groups

%prep

%setup -c -q -n %{name}-%{version}-%{release}

%build

%install
if [[ $RPM_BUILD_ROOT != "/" ]]; then
    rm -rf $RPM_BUILD_ROOT
fi

python setup.py install --prefix=${RPM_BUILD_ROOT}/usr \
    --single-version-externally-managed --record=installed_files

%clean
# Adding empty clean section per rpmlint.  In this particular case, there is
# nothing to clean up as there is no build process

%files
%defattr(-,root,root)
/usr/bin/*
%{python_sitelib}/ldapgroup/*py*
%{python_sitelib}/*egg-info

%changelog
* Tue Dec 10 2019   Tim Skirvin <tskirvin@fnal.gov> 0.1.0-0
- initial version, forked from some Ed and Chris code
