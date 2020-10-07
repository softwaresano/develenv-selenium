%define selenium_version 3.141.59
%define chromedriver_version 86.0.4240.75
%define geckodriver_version 0.24.0
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
Requires:    ss-develenv-user >= 33 httpd java-11-openjdk xorg-x11-server-Xvfb libXfont2 libXrandr nx-libs google-chrome-stable firefox
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
%{__mkdir_p} $RPM_BUILD_ROOT/%{target_dir}/grid/configs
%{__mkdir_p} $RPM_BUILD_ROOT/%{target_dir}/grid/log
%{__mkdir_p} $RPM_BUILD_ROOT/%{target_dir}/grid/shared
%{__mkdir_p} $RPM_BUILD_ROOT/%{target_dir}/grid/video_output
%{__mkdir_p} $RPM_BUILD_ROOT/%{target_dir}/hub/log/sessions_logs
%{__mkdir_p} $RPM_BUILD_ROOT/%{target_dir}/hub/shared/
%{__mkdir_p} $RPM_BUILD_ROOT/%{target_dir}/hub/video_output
%{__mkdir_p} $RPM_BUILD_ROOT/%{target_dir}/node/log

cp -R %{_sourcedir}/../../../target/artifacts/* $RPM_BUILD_ROOT/%{target_dir}
cp -R %{_sourcedir}/* ${RPM_BUILD_ROOT}/
ln -sf %{target_dir}/drivers/geckodriver ${RPM_BUILD_ROOT}/usr/bin/geckodriver
ln -sf %{target_dir}/drivers/chromedriver ${RPM_BUILD_ROOT}/usr/bin/chromedriver

%files
%defattr(-,develenv,develenv,-)
%{target_dir}/*
/opt/ss/etc/*
/opt/ss/develenv/platform/selenium
/usr/bin/*
/etc/systemd/system/*
