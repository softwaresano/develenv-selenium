%define selenium_version 3.3.1
%define chromedriver_version 2.30
%define geckodriver_version 0.15.0
Name:        selenium
Version:     %{versionModule}
Release:     %{selenium_version}.%{releaseModule}
Epoch:       2
Summary:     Selenium automates browsers
Group:       develenv
License:     http://creativecommons.org/licenses/by/3.0/
Packager:    softwaresano.com
URL:         http://www.seleniumhq.org/
BuildArch:   x86_64
BuildRoot:   %{_topdir}/BUILDROOT
Requires:    ss-develenv-user >= 33 httpd jdk xorg-x11-server-Xvfb libXfont libXrandr libNX_Xtst google-chrome-stable firefox
Vendor:      softwaresano
AutoReqProv: no


%define target_dir /

%define package_name selenium
%define target_dir /opt/ss/develenv/platform/%{package_name}

%description
Selenium automates browsers. That's it. What you do with that power is entirely
up to you. Primarily it is for automating web applications for testing purposes,
 but is certainly not limited to just that. Boring web-based administration 
tasks can (and should!) also be automated as well.

Selenium has the support of some of the largest browser vendors who have taken
(or are taking) steps to make Selenium a native part of their browser. It is
also the core technology in countless other browser automation tools, 
APIs and frameworks.

# ------------------------------------------------------------------------------
# CLEAN
# ------------------------------------------------------------------------------
%clean
rm -rf $RPM_BUILD_ROOT

# ------------------------------------------------------------------------------
# POST-INSTALL
# ------------------------------------------------------------------------------
%post
systemctl daemon-reload

# ------------------------------------------------------------------------------
# INSTALL
# ------------------------------------------------------------------------------
%install
%{__mkdir_p} $RPM_BUILD_ROOT/%{target_dir}/drivers ${RPM_BUILD_ROOT}/usr/bin/

cp -R %{_sourcedir}/../../../target/artifacts/* $RPM_BUILD_ROOT/%{target_dir}
cp -R %{_sourcedir}/* ${RPM_BUILD_ROOT}/
ln -sf %{target_dir}/drivers/geckodriver ${RPM_BUILD_ROOT}/usr/bin/geckodriver
ln -sf %{target_dir}/drivers/chromedriver ${RPM_BUILD_ROOT}/usr/bin/chromedriver

%files
%defattr(-,develenv,develenv,-)
%{target_dir}/*
/opt/ss/etc/*
/usr/bin/*
/etc/systemd/system/*
