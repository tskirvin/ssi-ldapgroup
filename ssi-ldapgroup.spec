Name:           ssi-ldapgroup
Summary:        Python Scripts and libraries to interact with Service Now @ FNAL
Version:        0.1.0
Release:        0%{?dist}
Group:          Applications/System
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Source0:        %{name}-%{version}-%{release}.tar.gz
BuildArch:      noarch

Requires:       python2 python36-iso8601 python36-requests python36-PyYAML
# also pysnow, no rpm available for that yet
BuildRequires:  python36 python36-setuptools python3-rpm-macros rsync
Vendor:         ECF-SSI
License:        Artistic 2.0
URL:            http://www.fnal.gov/

%description
Installs scripts and tools that provide an interface to the Fermi Service
Now interface via the JSON API.

%prep

%setup -c -q -n %{name}-%{version}-%{release}

%build

%install
if [[ $RPM_BUILD_ROOT != "/" ]]; then
    rm -rf $RPM_BUILD_ROOT
fi

python3 setup.py install --prefix=${RPM_BUILD_ROOT}/usr \
    --single-version-externally-managed --record=installed_files

%clean
# Adding empty clean section per rpmlint.  In this particular case, there is
# nothing to clean up as there is no build process

%files
%defattr(-,root,root)
/usr/bin/*
%{python3_sitelib}/ldapgroup/*py*
%{python3_sitelib}/*egg-info

%changelog
* Tue Dec 10 2019   Tim Skirvin <tskirvin@fnal.gov> 0.1.0-0
- initial version, forked from some Ed and Chris code
