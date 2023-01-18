Name: Hyprland
Version: v0.20.1beta
Release: 8%{?dist}
License: BSD
Summary: A dynamic tiling Wayland compositor that doesn't sacrifice on its looks.
Url: https://github.com/hyprwm/Hyprland

# Since tito support for submodules is iffy, we need to package manually.
# Sources can be obtained by:
# 	wget -c https://github.com/hyprwm/Hyprland/releases/download/v0.20.1beta/source-v0.20.1beta.tar.gz
# sha512sum source-v0.20.1beta.tar.gz
# 0aa98738702903ae49f020ad319c745e926a35732f6fe45efaede38582d76104936ac631d82940db2c70e8865d7a8fe04e1e726c6486b11dce5a0915160c3e9a 

Source0: https://github.com/hyprwm/Hyprland/releases/download/v0.20.1beta/source-%{version}.tar.gz

ExclusiveArch: x86_64

BuildRequires: ninja-build
BuildRequires: cmake
BuildRequires: meson
BuildRequires: gcc-c++
BuildRequires: jq
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
/usr/bin/hyprctl
/usr/bin/Hyprland
/usr/lib64/libwlroots.a
/usr/lib64/pkgconfig/wlroots.pc
/usr/share/hyprland/wall_8K.png
/usr/share/hyprland/hyprland.conf
/usr/share/hyprland/wall_2K.png
/usr/share/hyprland/wall_4K.png
/usr/share/wayland-sessions/hyprland.desktop
/usr/include/wlr/xcursor.h
/usr/include/wlr/util/region.h
/usr/include/wlr/util/addon.h
/usr/include/wlr/util/edges.h
/usr/include/wlr/util/log.h
/usr/include/wlr/util/box.h
/usr/include/wlr/config.h
/usr/include/wlr/xwayland.h
/usr/include/wlr/interfaces/wlr_buffer.h
/usr/include/wlr/interfaces/wlr_pointer.h
/usr/include/wlr/interfaces/wlr_touch.h
/usr/include/wlr/interfaces/wlr_tablet_pad.h
/usr/include/wlr/interfaces/wlr_switch.h
/usr/include/wlr/interfaces/wlr_output.h
/usr/include/wlr/interfaces/wlr_keyboard.h
/usr/include/wlr/interfaces/wlr_tablet_tool.h
/usr/include/wlr/types/wlr_xcursor_manager.h
/usr/include/wlr/types/wlr_primary_selection.h
/usr/include/wlr/types/wlr_output_power_management_v1.h
/usr/include/wlr/types/wlr_buffer.h
/usr/include/wlr/types/wlr_pointer.h
/usr/include/wlr/types/wlr_gamma_control_v1.h
/usr/include/wlr/types/wlr_compositor.h
/usr/include/wlr/types/wlr_touch.h
/usr/include/wlr/types/wlr_session_lock_v1.h
/usr/include/wlr/types/wlr_linux_dmabuf_v1.h
/usr/include/wlr/types/wlr_fullscreen_shell_v1.h
/usr/include/wlr/types/wlr_tablet_pad.h
/usr/include/wlr/types/wlr_matrix.h
/usr/include/wlr/types/wlr_input_inhibitor.h
/usr/include/wlr/types/wlr_switch.h
/usr/include/wlr/types/wlr_xdg_output_v1.h
/usr/include/wlr/types/wlr_pointer_constraints_v1.h
/usr/include/wlr/types/wlr_xdg_foreign_v2.h
/usr/include/wlr/types/wlr_output_damage.h
/usr/include/wlr/types/wlr_output.h
/usr/include/wlr/types/wlr_foreign_toplevel_management_v1.h
/usr/include/wlr/types/wlr_xdg_foreign_registry.h
/usr/include/wlr/types/wlr_xdg_decoration_v1.h
/usr/include/wlr/types/wlr_pointer_gestures_v1.h
/usr/include/wlr/types/wlr_surface.h
/usr/include/wlr/types/wlr_tablet_v2.h
/usr/include/wlr/types/wlr_idle_inhibit_v1.h
/usr/include/wlr/types/wlr_presentation_time.h
/usr/include/wlr/types/wlr_layer_shell_v1.h
/usr/include/wlr/types/wlr_subcompositor.h
/usr/include/wlr/types/wlr_output_management_v1.h
/usr/include/wlr/types/wlr_server_decoration.h
/usr/include/wlr/types/wlr_input_device.h
/usr/include/wlr/types/wlr_drm_lease_v1.h
/usr/include/wlr/types/wlr_scene.h
/usr/include/wlr/types/wlr_input_method_v2.h
/usr/include/wlr/types/wlr_xdg_foreign_v1.h
/usr/include/wlr/types/wlr_output_layout.h
/usr/include/wlr/types/wlr_keyboard.h
/usr/include/wlr/types/wlr_drm.h
/usr/include/wlr/types/wlr_keyboard_group.h
/usr/include/wlr/types/wlr_xdg_activation_v1.h
/usr/include/wlr/types/wlr_relative_pointer_v1.h
/usr/include/wlr/types/wlr_tablet_tool.h
/usr/include/wlr/types/wlr_data_device.h
/usr/include/wlr/types/wlr_primary_selection_v1.h
/usr/include/wlr/types/wlr_cursor.h
/usr/include/wlr/types/wlr_text_input_v3.h
/usr/include/wlr/types/wlr_keyboard_shortcuts_inhibit_v1.h
/usr/include/wlr/types/wlr_screencopy_v1.h
/usr/include/wlr/types/wlr_region.h
/usr/include/wlr/types/wlr_export_dmabuf_v1.h
/usr/include/wlr/types/wlr_viewporter.h
/usr/include/wlr/types/wlr_virtual_keyboard_v1.h
/usr/include/wlr/types/wlr_data_control_v1.h
/usr/include/wlr/types/wlr_seat.h
/usr/include/wlr/types/wlr_idle.h
/usr/include/wlr/types/wlr_virtual_pointer_v1.h
/usr/include/wlr/types/wlr_xdg_shell.h
/usr/include/wlr/backend/headless.h
/usr/include/wlr/backend/x11.h
/usr/include/wlr/backend/session.h
/usr/include/wlr/backend/libinput.h
/usr/include/wlr/backend/multi.h
/usr/include/wlr/backend/drm.h
/usr/include/wlr/backend/wayland.h
/usr/include/wlr/backend/interface.h
/usr/include/wlr/backend.h
/usr/include/wlr/version.h
/usr/include/wlr/render/drm_format_set.h
/usr/include/wlr/render/wlr_texture.h
/usr/include/wlr/render/gles2.h
/usr/include/wlr/render/allocator.h
/usr/include/wlr/render/egl.h
/usr/include/wlr/render/wlr_renderer.h
/usr/include/wlr/render/dmabuf.h
/usr/include/wlr/render/pixman.h
# /usr/include/wlr/render/vulkan.h
/usr/include/wlr/render/interface.h
/usr/include/wlr/types/wlr_damage_ring.h
/usr/include/wlr/types/wlr_single_pixel_buffer_v1.h
/usr/share/man/man1/Hyprland.1.gz
/usr/share/man/man1/hyprctl.1.gz

%changelog
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

