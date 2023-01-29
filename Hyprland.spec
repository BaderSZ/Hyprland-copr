Name: hyprland
Version: v0.21.0beta
Release: 12%{?dist}
License: BSD
Summary: A dynamic tiling Wayland compositor that doesn't sacrifice on its looks.
Url: https://github.com/hyprwm/Hyprland

# Since tito support for submodules is iffy, we need to package manually.
# Sources can be obtained by:
#    wget -c https://github.com/hyprwm/Hyprland/releases/download/v0.21.0beta/source-v0.21.0beta.tar.gz
# sha512sum source-v0.21.0beta.tar.gz
# 3afc495b0e7162b8a22cee56c008faba5b98c0bc0651a73f6ee742669b6993b52065afdfed85ac929e0ec35cfc3c85afddc541b323d01a29be743864deeaa5a2

Source0: https://github.com/hyprwm/Hyprland/releases/download/v0.21.0beta/source-%{version}.tar.gz

ExclusiveArch: x86_64

Requires: libwayland-server
Requires: libwayland-client
Recommends: kitty
Recommends: pipewire
Recommends: dunst
Recommends: qt5-qtwayland
Suggests: wofi
## TODO:
# Recommends: vulkan-renderer
BuildRequires: ninja-build
BuildRequires: cmake
BuildRequires: meson
BuildRequires: gcc-c++
BuildRequires: jq
BuildRequires: git
BuildRequires: hwdata-devel
BuildRequires: libxcb-devel
BuildRequires: libX11-devel
BuildRequires: pixman-devel
BuildRequires: wayland-protocols-devel
BuildRequires: cairo-devel
BuildRequires: pango-devel
BuildRequires: wayland-devel
BuildRequires: libdrm-devel
BuildRequires: libxkbcommon-devel
BuildRequires: systemd-devel
BuildRequires: libseat-devel
BuildRequires: mesa-libEGL-devel
BuildRequires: libinput-devel
BuildRequires: xcb-util-wm-devel
BuildRequires: xcb-util-renderutil-devel
BuildRequires: xcb-util-errors
BuildRequires: xorg-x11-server-Xwayland-devel
BuildRequires: mesa-libgbm-devel
BuildRequires: glslang-devel

%description
Hyprland is a dynamic tiling Wayland compositor based on wlroots that doesn't sacrifice on its looks.

%prep
%autosetup -n %{name}-source

%build
VERBOSE=1 meson -Dprefix=%{_prefix} _build
VERBOSE=1 ninja -C _build/

%install
export DESTDIR=%{buildroot}
VERBOSE=1 ninja -C _build/ install

%files
%license LICENSE
%{_bindir}/hyprctl
%{_bindir}/Hyprland

%{_libdir}/libwlroots.a
%{_libdir}/pkgconfig/wlroots.pc

%doc %{_mandir}/man1/hyprctl.1.gz
%doc %{_mandir}/man1/Hyprland.1.gz

%{_datadir}/hyprland/wall_2K.png
%{_datadir}/hyprland/wall_4K.png
%{_datadir}/hyprland/wall_8K.png
%config(noreplace) %{_datadir}/%{name}/%{name}.conf
%{_datadir}/pkgconfig/hyprland-protocols.pc
%{_datadir}/protocols/hyprland-toplevel-export-v1.xml
%{_datadir}/wayland-sessions/%{name}.desktop

%dir %{_includedir}/wlr
%{_includedir}/wlr/backend/drm.h
%{_includedir}/wlr/backend.h
%{_includedir}/wlr/backend/headless.h
%{_includedir}/wlr/backend/interface.h
%{_includedir}/wlr/backend/libinput.h
%{_includedir}/wlr/backend/multi.h
%{_includedir}/wlr/backend/session.h
%{_includedir}/wlr/backend/wayland.h
%{_includedir}/wlr/backend/x11.h
%{_includedir}/wlr/config.h
%{_includedir}/wlr/interfaces/wlr_buffer.h
%{_includedir}/wlr/interfaces/wlr_keyboard.h
%{_includedir}/wlr/interfaces/wlr_output.h
%{_includedir}/wlr/interfaces/wlr_pointer.h
%{_includedir}/wlr/interfaces/wlr_switch.h
%{_includedir}/wlr/interfaces/wlr_tablet_pad.h
%{_includedir}/wlr/interfaces/wlr_tablet_tool.h
%{_includedir}/wlr/interfaces/wlr_touch.h
%{_includedir}/wlr/render/allocator.h
%{_includedir}/wlr/render/dmabuf.h
%{_includedir}/wlr/render/drm_format_set.h
%{_includedir}/wlr/render/egl.h
%{_includedir}/wlr/render/gles2.h
%{_includedir}/wlr/render/interface.h
%{_includedir}/wlr/render/pixman.h
## {_includedir/wlr/render/vulkan.h
%{_includedir}/wlr/render/wlr_renderer.h
%{_includedir}/wlr/render/wlr_texture.h
%{_includedir}/wlr/types/wlr_buffer.h
%{_includedir}/wlr/types/wlr_compositor.h
%{_includedir}/wlr/types/wlr_content_type_v1.h
%{_includedir}/wlr/types/wlr_cursor.h
%{_includedir}/wlr/types/wlr_damage_ring.h
%{_includedir}/wlr/types/wlr_data_control_v1.h
%{_includedir}/wlr/types/wlr_data_device.h
%{_includedir}/wlr/types/wlr_drm.h
%{_includedir}/wlr/types/wlr_drm_lease_v1.h
%{_includedir}/wlr/types/wlr_export_dmabuf_v1.h
%{_includedir}/wlr/types/wlr_foreign_toplevel_management_v1.h
%{_includedir}/wlr/types/wlr_fullscreen_shell_v1.h
%{_includedir}/wlr/types/wlr_gamma_control_v1.h
%{_includedir}/wlr/types/wlr_idle.h
%{_includedir}/wlr/types/wlr_idle_inhibit_v1.h
%{_includedir}/wlr/types/wlr_idle_notify_v1.h
%{_includedir}/wlr/types/wlr_input_device.h
%{_includedir}/wlr/types/wlr_input_inhibitor.h
%{_includedir}/wlr/types/wlr_input_method_v2.h
%{_includedir}/wlr/types/wlr_keyboard_group.h
%{_includedir}/wlr/types/wlr_keyboard.h
%{_includedir}/wlr/types/wlr_keyboard_shortcuts_inhibit_v1.h
%{_includedir}/wlr/types/wlr_layer_shell_v1.h
%{_includedir}/wlr/types/wlr_linux_dmabuf_v1.h
%{_includedir}/wlr/types/wlr_matrix.h
%{_includedir}/wlr/types/wlr_output_damage.h
%{_includedir}/wlr/types/wlr_output.h
%{_includedir}/wlr/types/wlr_output_layout.h
%{_includedir}/wlr/types/wlr_output_management_v1.h
%{_includedir}/wlr/types/wlr_output_power_management_v1.h
%{_includedir}/wlr/types/wlr_pointer_constraints_v1.h
%{_includedir}/wlr/types/wlr_pointer_gestures_v1.h
%{_includedir}/wlr/types/wlr_pointer.h
%{_includedir}/wlr/types/wlr_presentation_time.h
%{_includedir}/wlr/types/wlr_primary_selection.h
%{_includedir}/wlr/types/wlr_primary_selection_v1.h
%{_includedir}/wlr/types/wlr_region.h
%{_includedir}/wlr/types/wlr_relative_pointer_v1.h
%{_includedir}/wlr/types/wlr_scene.h
%{_includedir}/wlr/types/wlr_screencopy_v1.h
%{_includedir}/wlr/types/wlr_seat.h
%{_includedir}/wlr/types/wlr_server_decoration.h
%{_includedir}/wlr/types/wlr_session_lock_v1.h
%{_includedir}/wlr/types/wlr_shm.h
%{_includedir}/wlr/types/wlr_single_pixel_buffer_v1.h
%{_includedir}/wlr/types/wlr_subcompositor.h
%{_includedir}/wlr/types/wlr_switch.h
%{_includedir}/wlr/types/wlr_tablet_pad.h
%{_includedir}/wlr/types/wlr_tablet_tool.h
%{_includedir}/wlr/types/wlr_tablet_v2.h
%{_includedir}/wlr/types/wlr_text_input_v3.h
%{_includedir}/wlr/types/wlr_touch.h
%{_includedir}/wlr/types/wlr_viewporter.h
%{_includedir}/wlr/types/wlr_virtual_keyboard_v1.h
%{_includedir}/wlr/types/wlr_virtual_pointer_v1.h
%{_includedir}/wlr/types/wlr_xcursor_manager.h
%{_includedir}/wlr/types/wlr_xdg_activation_v1.h
%{_includedir}/wlr/types/wlr_xdg_decoration_v1.h
%{_includedir}/wlr/types/wlr_xdg_foreign_registry.h
%{_includedir}/wlr/types/wlr_xdg_foreign_v1.h
%{_includedir}/wlr/types/wlr_xdg_foreign_v2.h
%{_includedir}/wlr/types/wlr_xdg_output_v1.h
%{_includedir}/wlr/types/wlr_xdg_shell.h
%{_includedir}/wlr/util/addon.h
%{_includedir}/wlr/util/box.h
%{_includedir}/wlr/util/edges.h
%{_includedir}/wlr/util/log.h
%{_includedir}/wlr/util/region.h
%{_includedir}/wlr/version.h
%{_includedir}/wlr/xcursor.h
%{_includedir}/wlr/xwayland.h
%{_includedir}/wlr/xwayland/server.h
%{_includedir}/wlr/xwayland/shell.h
%{_includedir}/wlr/xwayland/xwayland.h

%changelog
* Sun Jan 29 2023 Bader Zaidan <bader@zaidan.tech> v0.21.0beta-12
- push new version (bader@zaidan.tech)
- Add required and recommended packages (bader@zaidan.tech)

* Wed Jan 18 2023 Bader Zaidan <bader@zaidan.tech> v0.20.1beta-11
- remove macro warning (bader@zaidan.tech)
- Automatic commit of package [hyprland] minor release [v0.20.1beta-10].
  (bader@zaidan.tech)

* Wed Jan 18 2023 Bader Zaidan <bader@zaidan.tech> v0.20.1beta-10
- new package built with tito

* Wed Jan 18 2023 Bader Zaidan <bader@zaidan.tech> v0.20.1beta-9
- update hyprland version to v0.20.1beta (bader@zaidan.tech)

* Wed Oct 05 2022 Bader Zaidan <bader@zaidan.pw> v0.15.0beta-8
- update signature and checksum (bader@zaidan.pw)

* Wed Oct 05 2022 Bader Zaidan <bader@zaidan.pw> v0.15.0beta-7
- Add missing files and manpages to list (bader@zaidan.pw)
- fix package archive, spec comments (bader@zaidan.pw)

* Wed Oct 05 2022 Bader Zaidan <bader@zaidan.pw> v0.15.0beta-6
- update package to version v0.15.0beta (bader@zaidan.pw)
* Wed Oct 05 2022 Bader Zaidan <bader@zaidan.pw> v0.15.0beta-5
- add README (bader@zaidan.pw)

* Tue Jul 12 2022 Bader Zaidan <bader@zaidan.pw> v0.6.3beta-4
- 

* Tue Jul 12 2022 Bader Zaidan <bader@zaidan.pw> v0.6.3beta-3
- replace buildroot with prefix
- add DESTDIR
- comment out vulkan

* Mon Jul 11 2022 Bader Zaidan <bader@zaidan.pw> v0.6.3beta-2
- Uncomment vulkan

* Mon Jul 11 2022 Bader Zaidan <bader@zaidan.pw> v0.6.3beta-1
- new package built with tito

