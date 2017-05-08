Name:           ros-indigo-pyros
Version:        0.4.1
Release:        1%{?dist}
Summary:        ROS pyros package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       python-mock >= 1.0.1
Requires:       ros-indigo-pyros-common >= 0.4.2
Requires:       ros-indigo-pyros-interfaces-ros >= 0.4.0
BuildRequires:  python-mock >= 1.0.1
BuildRequires:  ros-indigo-catkin >= 0.6.18
BuildRequires:  ros-indigo-catkin-pip >= 0.2.0
BuildRequires:  ros-indigo-pyros-common >= 0.4.2
BuildRequires:  ros-indigo-pyros-interfaces-ros >= 0.4.0

%description
Provides Python to ROS multiprocess API, useful for using ROS from different
multiprocess environment while keeping both isolated.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon May 08 2017 AlexV <asmodehn@gmail.com> - 0.4.1-1
- Autogenerated by Bloom

* Mon May 08 2017 AlexV <asmodehn@gmail.com> - 0.4.1-0
- Autogenerated by Bloom

* Mon May 08 2017 AlexV <asmodehn@gmail.com> - 0.4.0-3
- Autogenerated by Bloom

* Mon May 08 2017 AlexV <asmodehn@gmail.com> - 0.4.0-2
- Autogenerated by Bloom

* Mon May 08 2017 AlexV <asmodehn@gmail.com> - 0.4.0-1
- Autogenerated by Bloom

* Mon May 08 2017 AlexV <asmodehn@gmail.com> - 0.4.0-0
- Autogenerated by Bloom

* Fri Mar 24 2017 AlexV <asmodehn@gmail.com> - 0.3.2-0
- Autogenerated by Bloom

* Fri Jan 13 2017 AlexV <asmodehn@gmail.com> - 0.3.1-0
- Autogenerated by Bloom

* Wed Nov 16 2016 AlexV <asmodehn@gmail.com> - 0.3.0-2
- Autogenerated by Bloom

* Wed Nov 16 2016 AlexV <asmodehn@gmail.com> - 0.3.0-1
- Autogenerated by Bloom

* Mon Nov 14 2016 AlexV <asmodehn@gmail.com> - 0.3.0-0
- Autogenerated by Bloom

* Tue Oct 25 2016 AlexV <asmodehn@gmail.com> - 0.2.0-1
- Autogenerated by Bloom

* Thu Sep 01 2016 AlexV <asmodehn@gmail.com> - 0.2.0-0
- Autogenerated by Bloom

