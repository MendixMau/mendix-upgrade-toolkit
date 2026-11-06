# Native Mobile Resources (Marketplace component 109513)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/109513)

| version | published | min Mendix |
|---|---|---|
| 12.5.0 | 2026-09-24 | 11.12.3 |
| 12.4.0 | 2026-09-02 | 11.12.3 |
| 12.3.0 | 2026-08-06 | 11.12.0 |
| 12.2.2 | 2026-07-21 | 11.12.0 |
| 12.2.1 | 2026-07-17 | 11.11.0 |
| 12.2.0 | 2026-07-03 | 11.11.0 |
| 12.1.0 | 2026-06-10 | 11.11.0 |
| 12.0.1 | 2026-06-01 | 11.10.0 |
| 12.0.0 | 2026-05-15 | 11.10.0 |
| 11.4.2 | 2026-05-28 | 11.7.0 |
| 11.4.1 | 2026-03-14 | 11.7.0 |
| 11.4.0 | 2026-03-05 | 11.7.0 |
| 11.3.13 | 2026-09-24 | 11.6.0 |
| 11.3.12 | 2026-09-02 | 11.6.0 |
| 11.3.11 | 2026-08-05 | 11.6.0 |
| 11.3.10 | 2026-07-02 | 11.6.0 |
| 11.3.9 | 2026-06-02 | 11.6.0 |
| 11.3.8 | 2026-05-28 | 11.6.0 |
| 11.3.7 | 2026-03-14 | 11.6.0 |
| 11.3.6 | 2026-03-05 | 11.6.0 |
| 11.3.5 | 2026-02-17 | 11.7.0 |
| 11.3.4 | 2026-02-17 | 11.3.0 |
| 11.3.3 | 2026-01-20 | 11.3.0 |
| 11.3.2 | 2025-12-23 | 11.3.0 |
| 11.3.1 | 2025-12-15 | 11.3.0 |
| 11.3.0 | 2025-12-15 | 11.3.0 |
| 11.2.1 | 2025-11-07 | 11.3.0 |
| 11.2.0 | 2025-10-17 | 11.3.0 |
| 11.1.1 | 2025-10-07 | 11.3.0 |
| 11.1.0 | 2025-10-02 | 11.3.0 |
| 11.0.3 | 2025-08-21 | 11.0.0 |
| 11.0.2 | 2025-08-11 | 11.0.0 |
| 11.0.0 | 2025-07-07 | 11.0.0 |
| 10.1.17 | 2026-05-12 | 10.24.0 |
| 10.1.16 | 2026-03-14 | 10.24.0 |
| 10.1.15 | 2026-03-04 | 10.24.0 |
| 10.1.14 | 2026-02-18 | 10.24.0 |
| 10.1.13 | 2026-01-20 | 10.24.0 |
| 10.1.11 | 2025-12-19 | 10.24.0 |
| 10.1.10 | 2025-12-11 | 10.24.0 |
| … 124 older versions | | |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 12.5.0 | breaking | Removed react-native-linear-gradient library in favor of react-native View with linear-gradient type background. | BackgroundGradient, react-native-linear-gradient |  |
| 12.5.0 | feature | Added On change event that triggers when Trigger attribute value changes, allowing detection of bottom sheet dismissal. | BottomSheet |  |
| 12.5.0 | breaking | Replaced deprecated prop containerHeight with containerLayoutState option. | BottomSheet, containerHeight | containerLayoutState |
| 12.5.0 | feature | Added direct image upload to System.Image object using type image with allowUpload set to true. | Signature, System.Image |  |
| 12.5.0 | breaking | Renamed onSave action to onSignEnd to match web signature widget naming convention. | Signature, onSave | onSignEnd |
| 12.4.0 | improvement | Updated react-native-animatable to 1.4.0. | Animation, react-native-animatable |  |
| 12.4.0 | improvement | Updated victory-native to 36.9.2. | BarChart, victory-native |  |
| 12.4.0 | improvement | Updated deprecated-react-native-prop-types to 4.2.3. | Carousel, deprecated-react-native-prop-types |  |
| 12.4.0 | improvement | Pinned react-native-snap-carousel to 3.9.1. | Carousel, react-native-snap-carousel |  |
| 12.4.0 | improvement | Pinned react-native-color to 0.0.10. | ColorPicker, react-native-color |  |
| 12.4.0 | improvement | Pinned react-native-slider to 0.11.0. | ColorPicker, react-native-slider |  |
| 12.4.0 | improvement | Updated tinycolor2 to 1.6.0. | ColorPicker, tinycolor2 |  |
| 12.4.0 | improvement | Pinned querystringify to 2.2.0. | Feedback, querystringify |  |
| 12.4.0 | breaking | Removed react-native-reanimated library and used Animated API of react native for animation. | FloatingActionButton, react-native-reanimated |  |
| 12.4.0 | improvement | Pinned prop-types to 15.8.1. | Maps, prop-types |  |
| 12.4.0 | improvement | Pinned react-native-material-menu to 1.2.0. | PopupMenu, react-native-material-menu |  |
| 12.4.0 | improvement | Pinned react-native-progress to 5.0.1. | ProgressBar, react-native-progress |  |
| 12.4.0 | improvement | Pinned @miblanchard/react-native-slider to 2.6.0. | RangeSlider, @miblanchard/react-native-slider |  |
| 12.4.0 | breaking | Removed @react-native-vector-icons/common and @react-native-vector-icons/get-image dependencies. | Rating, @react-native-vector-icons/common, @react-native-vector-icons/get-image |  |
| 12.4.0 | improvement | Added react-native-svg dependency and fixed rating icons not visible if user sets empty and selected star as none. | Rating, react-native-svg |  |
| 12.4.0 | improvement | Updated react-native-segmented-control-tab to 3.4.1. | ToggleButtons, react-native-segmented-control-tab |  |
| 12.3.0 | breaking | Replaced @notifee/react-native with react-native-notify-kit library. | @notifee/react-native, react-native-notify-kit | react-native-notify-kit |
| 12.3.0 | feature | Added support for QR of available remaining types including pdf417 in barcode scanner functionality. | BarcodeScanner |  |
| 12.2.1 | breaking | Switched to new sound library for Play sound action to support react-native 0.84+. | Play sound action |  |
| 12.2.1 | improvement | Play sound action now plays audio from online documents on Android by downloading to version-based cache. | Play sound action |  |
| 12.1.0 | requirement | Updated react-native from version 0.83.4 to 0.84.1. | react-native |  |
| 12.1.0 | improvement | Updated @sbaiahmed1/react-native-biometrics from version v0.10.0 to v0.15.0. | @sbaiahmed1/react-native-biometrics |  |
| 12.1.0 | improvement | Updated react-native-gesture-handler from version v2.30.0 to v2.31.2. | BottomSheet, react-native-gesture-handler |  |
| 12.1.0 | improvement | Updated react-native-reanimated from version v4.2.2 to v4.3.1. | BottomSheet, react-native-reanimated |  |
| 12.1.0 | improvement | Updated react-native-worklets from version v0.7.4 to v0.8.3. | BottomSheet, react-native-worklets |  |
| 12.1.0 | improvement | Updated @gorhom/bottom-sheet from version v5.2.8 to v5.2.14. | BottomSheet, @gorhom/bottom-sheet |  |
| 12.1.0 | improvement | Updated @shopify/flash-list from version v2.2.2 to v2.3.1. | BottomSheet, @shopify/flash-list |  |
| 12.1.0 | improvement | Updated react-native-view-shot from version v4.0.3 to 5.1.0. | Feedback, react-native-view-shot |  |
| 12.1.0 | breaking | Replaced react-native-action-button library with custom implementation using React Native Animated API. | FloatingActionButton, react-native-action-button |  |
| 12.1.0 | removal | Removed deprecated react-native-prop-types dependency. | FloatingActionButton, react-native-prop-types |  |
| 12.1.0 | improvement | Updated react-native-svg from version v15.15.3 to v15.15.4. | GalleryTextFilter, react-native-svg |  |
| 12.1.0 | improvement | Updated @react-native-vector-icons/common from version v12.4.0 to v12.4.2. | Image, @react-native-vector-icons/common |  |
| 12.1.0 | improvement | Updated react-native-video from version v6.19.0 to v6.19.2. | VideoPlayer, react-native-video |  |
| 12.0.1 | improvement | Updated @sbaiahmed1/react-native-biometrics from version v0.10.0 to v0.15.0. | @sbaiahmed1/react-native-biometrics |  |
| 12.0.0 | breaking | Replaced deprecated CameraRoll.saveToCameraRoll with CameraRoll.saveAsset in SaveToPictureLibrary activity. | SaveToPictureLibrary, CameraRoll.saveToCameraRoll | CameraRoll.saveAsset |
| 12.0.0 | improvement | Add await to API calls updated to async in recent update. |  |  |
| 12.0.0 | improvement | Updated @react-native-camera-roll/camera-roll from version v7.4.0 to v7.10.2. | @react-native-camera-roll/camera-roll |  |
| 12.0.0 | improvement | Updated @sbaiahmed1/react-native-biometrics from version v0.4.0 to v0.10.0. | @sbaiahmed1/react-native-biometrics |  |
| 12.0.0 | improvement | Updated @swan-io/react-native-browser from version v0.4.1 to v1.0.1. | @swan-io/react-native-browser |  |
| 12.0.0 | improvement | Updated react-native-blob-util from version v0.21.2 to v0.24.7. | react-native-blob-util |  |
| 12.0.0 | improvement | Updated react-native-device-info from version v14.0.4 to v15.0.2. | react-native-device-info |  |
| 12.0.0 | improvement | Updated react-native-file-viewer-turbo from version v0.6.0 to v0.7.4. | react-native-file-viewer-turbo |  |
| 12.0.0 | improvement | Updated react-native-localize from version v3.2.1 to v3.7.0. | react-native-localize |  |
| 12.0.0 | improvement | Updated react-native-permissions from version v5.4.2 to v5.5.1. | react-native-permissions |  |
| 12.0.0 | improvement | Updated @react-native-community/netinfo from version v11.4.1 to v11.5.2. | AppEvents, @react-native-community/netinfo |  |
| 12.0.0 | breaking | Replaced deprecated InteractionManager in Feedback widget. | Feedback, InteractionManager |  |
| 12.0.0 | feature | Translation support for all widget text through configurable properties in Studio Pro. | Feedback |  |
| 12.0.0 | improvement | Visible label above feedback input field to ensure WCAG compliance. | Feedback |  |
| 12.0.0 | improvement | Updated react-native-svg from version v15.12.1 to v15.15.3. | GalleryTextFilter, react-native-svg |  |
| 12.0.0 | improvement | Updated @d11/react-native-fast-image from version v8.11.1 to v8.13.0. | Image, @d11/react-native-fast-image |  |
| 12.0.0 | improvement | Updated react-native-gesture-handler from version v2.24.0 to v2.30.0. | ListViewSwipe, react-native-gesture-handler |  |
| 12.0.0 | improvement | Updated react-native-maps from version v1.14.0 to v1.20.1. | Maps, react-native-maps |  |
| 12.0.0 | improvement | Updated @react-navigation/bottom-tabs from version v6.6.1 to v7.15.2. | SafeAreaView, @react-navigation/bottom-tabs |  |
| 12.0.0 | improvement | Updated react-native-safe-area-context from version v5.2.0 to v5.7.0. | SafeAreaView, react-native-safe-area-context |  |
| 12.0.0 | improvement | Updated react-native-webview from version v13.13.2 to v13.16.1. | Signature, react-native-webview |  |
| 12.0.0 | improvement | Updated react-native-video from version v6.10.2 to v6.19.0. | VideoPlayer, react-native-video |  |
| 11.4.2 | improvement | BottomSheet now uses BottomSheetScrollView instead of BottomSheetView, enabling proper scrolling in expanded states. | BottomSheet |  |
| 11.4.2 | improvement | NativeBottomSheet explicitly calculates snapPoints with 90% screen height cap for predictable sizing. | BottomSheet |  |
| 11.4.2 | improvement | CustomModalSheet measures content height dynamically with 90% screen height cap, removing offscreen SafeAreaView measurement. | BottomSheet |  |
| 11.4.2 | improvement | Migrated from using native FlatList to @shopify/flash-list. | Gallery |  |
| 11.3.11 | fix | Fixed biometric authentication issue not working on Android and crashing on iOS. | biometric authentication |  |
| 11.3.11 | breaking | Replaced @notifee/react-native with react-native-notify-kit library. | @notifee/react-native, react-native-notify-kit | react-native-notify-kit |
| 11.3.10 | fix | Fixed flickering issue on Android when opening bottom sheet (both basic and custom render types). | BottomSheet |  |
| 11.3.9 | fix | Fixed the non-worklet function called on the UI thread error in bottom sheet from @gorhom/bottom-sheet usage. | BottomSheet, @gorhom/bottom-sheet |  |
| 11.3.8 | breaking | Migrated from using the native FlatList to @shopify/flash-list. | Gallery, @shopify/flash-list | @shopify/flash-list |
| 11.3.6 | fix | Fixed native file system module reference. | native file system module |  |
| 11.3.5 | requirement | Upgraded Native Mobile Resources to Studio Pro 11.7.0. |  |  |
| 11.3.3 | fix | Fixed an issue where the background-gradient-native widget would not render correctly with the new RN architecture upgrade. | BackgroundGradient |  |
| 11.3.2 | feature | Expanded the barcode-scanner configuration in Vision Camera to support all available CodeType formats, including QR, Aztec, Data Matrix, PDF-417, EAN, UPC, GS1 DataBar, ITF, and Code barcodes. | BarcodeScanner, Vision Camera |  |
| 11.3.2 | requirement | Updated react-native-vision-camera from version v4.7.1 to v4.7.3. | react-native-vision-camera |  |
| 11.3.1 | requirement | Updated react-native-reanimated to v3.17.5. Addresses compatibility issues with React Native 0.78 and later versions. | BottomSheet, react-native-reanimated |  |
| 11.3.1 | requirement | Updated react-native-svg to v15.12.1. Addresses compatibility issues with React Native 0.78 and later versions. | GalleryTextFilter, react-native-svg |  |
| 11.3.0 | breaking | Updated react-native-firebase to v20.1.0. Ensure Native Template and Native Builder are updated accordingly. | Notifications, react-native-firebase |  |
| 11.2.1 | breaking | Updated react-native-firebase to v20.1.0. Ensure Native Template and Native Builder are updated accordingly. | Notifications, react-native-firebase |  |
| 11.2.0 | requirement | Updated react-native-video version to 6.10.2. | VideoPlayer, react-native-video |  |
| 11.1.1 | breaking | Migrated to react-native-vision-camera from react-native-camera. | BarcodeScanner, react-native-camera, react-native-vision-camera | react-native-vision-camera |
| 11.1.0 | breaking | Migrated from react-native-sound to react-native-track-player. | react-native-sound, react-native-track-player | react-native-track-player |
| 11.1.0 | requirement | Updated react-native-permissions to 5.4.2. | react-native-permissions |  |
| 11.1.0 | removal | Removed react-native-schedule-exact-alarm-permission since it's no longer required. | react-native-schedule-exact-alarm-permission |  |
| 11.1.0 | requirement | Updated react-native from version 0.75.4 to 0.77.3. | react-native |  |
| 11.1.0 | breaking | Migrated from react-native-file-viewer to react-native-file-viewer-turbo for new architecture compatibility. | react-native-file-viewer, react-native-file-viewer-turbo | react-native-file-viewer-turbo |
| 11.1.0 | breaking | File viewer now uses modal to display content. | File viewer |  |
| 11.1.0 | breaking | Migrated from react-native-biometrics to @sbaiahmed1/react-native-biometrics for new architecture compatibility. | react-native-biometrics, @sbaiahmed1/react-native-biometrics | @sbaiahmed1/react-native-biometrics |
| 11.1.0 | requirement | Updated react-native-reanimated to v3.16.7. | BottomSheet, react-native-reanimated |  |
| 11.1.0 | breaking | Migrated from react-native-fast-image to @d11/react-native-fast-image for new architecture compatibility. | Image, react-native-fast-image, @d11/react-native-fast-image | @d11/react-native-fast-image |
| 11.1.0 | removal | Removed react-native-system-navigation-bar and deprecated-react-native-prop-types dependencies. Navigation bar visibility now handled by react-native-video package. | VideoPlayer, react-native-system-navigation-bar, deprecated-react-native-prop-types |  |
| 11.0.3 | requirement | Updated React Native from version 0.75.4 to 0.77.3. | React Native |  |
| 11.0.3 | requirement | Updated react-native-video to version 6.10.0. | VideoPlayer, react-native-video |  |
| 11.0.0 | requirement | Updated react-native-linear-gradient to latest version. | BackgroundGradient, react-native-linear-gradient |  |
| 11.0.0 | requirement | Updated react-native-device-info to latest version. | BottomSheet, react-native-device-info |  |
| 11.0.0 | breaking | The widget has been migrated to notifee. | Notifications |  |
| 11.0.0 | requirement | Updated react-native-webview from version v13.12.5 to latest. | Signature, react-native-webview |  |
| 11.0.0 | requirement | Updated react-native-webview from version v13.12.5 to latest to support react-native 0.77. | WebView, react-native-webview |  |
| 10.1.17 | breaking | Replaced the deprecated CameraRoll.saveToCameraRoll with CameraRoll.saveAsset in SaveToPictureLibrary activity. | SaveToPictureLibrary, CameraRoll | CameraRoll.saveAsset |
| 10.1.11 | feature | Expanded the barcode-scanner configuration in Vision Camera to support all available CodeType formats, including QR, Aztec, Data Matrix, PDF-417, EAN, UPC, GS1 DataBar, ITF, and Code barcodes. | BarcodeScanner, Vision Camera |  |
| 10.1.10 | requirement | Updated react-native-vision-camera from version v4.7.1 to v4.7.3. | BarcodeScanner, react-native-vision-camera |  |
| 10.1.9 | breaking | Migrated to react-native-vision-camera from react-native-camera. | BarcodeScanner, react-native-camera, react-native-vision-camera | react-native-vision-camera |
| 10.1.8 | breaking | Updated react-native-firebase to v20.1.0. Ensure Native Template and Native Builder are updated accordingly. | Notifications, react-native-firebase |  |
| 10.1.6 | requirement | Updated react-native-video version to 6.10.2. | VideoPlayer, react-native-video |  |
| 10.1.4 | fix | Fixed location permission issue on iOS. | react-native-community/geolocation |  |
| 10.1.1 | requirement | Updated react-native-video version from 6.4.5 to 6.10.0. | VideoPlayer, react-native-video |  |
| 10.1.0 | requirement | Updated react-native-webview to latest version to support react native 0.77. | Signature, react-native-webview |  |
| 10.0.0 | breaking | Migrated from react-native-inappbrowser-reborn to @swan-io/react-native-browser to prevent issues for next rn upgrade. | react-native-inappbrowser-reborn, @swan-io/react-native-browser | @swan-io/react-native-browser |
| 10.0.0 | breaking | Migrated from @react-native-community/cameraroll to @react-native-camera-roll/camera-roll to prevent issues for next rn upgrade. | @react-native-community/cameraroll, @react-native-camera-roll/camera-roll | @react-native-camera-roll/camera-roll |
| 10.0.0 | requirement | Updated several dependencies such as react-native-blob-util and react-native-image-picker to their latest version. | react-native-blob-util, react-native-image-picker |  |
| 10.0.0 | requirement | Updated @react-native-community/netinfo from version v5.9.7 to v11.4.1. | AppEvents, @react-native-community/netinfo |  |
| 10.0.0 | breaking | Rewrote all bottomsheet widgets (customModalSheet, ExpandingDrawer, and NativeBottomSheet) using @gorhom/bottom-sheet. | BottomSheet, @gorhom/bottom-sheet | @gorhom/bottom-sheet |
| 10.0.0 | requirement | Updated react-native-view-shot from version v3.1.2 to v4.0.3. | Feedback, react-native-view-shot |  |
| 10.0.0 | requirement | Updated react-native-gesture-handler from version v2.16.2 to 2.24.0. | ListViewSwipe, react-native-gesture-handler |  |
| 10.0.0 | requirement | Updated react-native-webview from version v9.0.0 to v10.15.0. | Signature, react-native-webview |  |
| 10.0.0 | requirement | Updated react-native-webview from version v11.26.1 to v13.13.2. | WebView, react-native-webview |  |
| 9.3.5 | improvement | Updated react-native-svg from 15.7.1 to 15.11.2. | gallery-text-filter-native, image-native, qr-code-native, react-native-svg |  |
| 9.3.4 | improvement | Started using react-native-safe-area-context to improve edge-to-edge boundaries on Android. | SafeAreaView, react-native-safe-area-context |  |
| 9.3.0 | improvement | Updated react-native-modal from v11.4.5 to v13.0.1 to fix random crashes in custom-bottom-sheet widget. | BottomSheet, react-native-modal |  |
| 9.2.0 | fix | Bumped react-native-progress version to fix black background issues. | ProgressBar, react-native-progress |  |
| 9.0.0 | improvement | Updated @mendix/pluggable-widgets-tools from v9.0.0 to v10.0.1. | @mendix/pluggable-widgets-tools |  |
| 9.0.0 | breaking | Updated react-native from 0.73.8 to 0.75.4. | react-native |  |
| 9.0.0 | breaking | Switched from @react-native-community/async-storage to @react-native-async-storage/async-storage. | @react-native-community/async-storage, @react-native-async-storage/async-storage | @react-native-async-storage/async-storage |
| 9.0.0 | feature | Upgraded React Native Permissions to 4.5.1. | React Native Permissions |  |
| 9.0.0 | breaking | Updated react-native-device-info from v11.1.0 to v13.0.0. | BottomSheet, react-native-device-info |  |
| 9.0.0 | breaking | Updated react-native-svg from v12.3.0 to v15.7.1. | GalleryTextFilter, react-native-svg |  |
| 9.0.0 | improvement | Updated react-native-vector-icons from v10.0.3 to v10.2.0. | Image, react-native-vector-icons |  |
| 9.0.0 | improvement | Updated react-native-maps version to 1.14.0. | Maps, react-native-maps |  |
| 9.0.0 | breaking | Renamed renderMode property to popupRenderMode to avoid conflicts with new renderMode system option. | PopupMenu, renderMode, popupRenderMode | popupRenderMode |
| 9.0.0 | migration-step | Update PopupMenu renderMode property to popupRenderMode in Studio Pro. | PopupMenu, renderMode, popupRenderMode |  |
| 9.0.0 | feature | Added support for device font size for responsive progress circle sizing. | ProgressCircle |  |
| 9.0.0 | improvement | Updated react-native-video version to 6.4.5. | VideoPlayer, react-native-video |  |
| 8.0.3 | feature | Upgraded React Native Permissions to 4.5.1. | React Native Permissions |  |
| 8.0.3 | improvement | Updated react-native-maps version to 1.14.0. | Maps, react-native-maps |  |
| 8.0.3 | feature | Added support for device font size for responsive progress circle sizing. | ProgressCircle |  |
| 8.0.3 | improvement | Updated react-native-video version to 6.4.5. | VideoPlayer, react-native-video |  |
| 8.0.2 | improvement | Updated react-native-maps version to 1.14.0. | Maps, react-native-maps |  |
| 8.0.2 | improvement | Updated react-native-video version to 6.4.5. | VideoPlayer, react-native-video |  |
| 8.0.1 | feature | Upgraded React Native Device Info to version 11.1.0. | BottomSheet, react-native-device-info |  |
| 8.0.1 | feature | Upgraded React Native Gesture Handler to version 2.16.2. | ListViewSwipe, react-native-gesture-handler |  |
| 8.0.1 | improvement | Updated Rating widget to replace AnimatableProps from react-native-animatable with AnimatableProperties. | Rating, react-native-animatable |  |
| 8.0.1 | breaking | Made Rating widget compatible with React Native 0.73.8. | Rating, react-native |  |
| 8.0.0 | breaking | Upgraded React Native to version 0.73.8. | react-native |  |
| 6.1.0 | fix | Added CheckGenericPermission and updated RequestGenericPermission to use SCHEDULE_EXACT_ALARM. | CheckGenericPermission, RequestGenericPermission, SCHEDULE_EXACT_ALARM |  |
| 6.0.0 | breaking | Upgraded React Native to version 0.72.7. | React Native |  |
| 6.0.0 | breaking | Made Image widget compatible with React Native 0.72.7. | Image |  |
| 6.0.0 | requirement | Updated react-native-vector-icons dependency from 9.1.0 to 10.0.3. | react-native-vector-icons |  |
| 6.0.0 | breaking | Made Rating widget compatible with React Native 0.72.7. | Rating |  |
| 6.0.0 | breaking | Upgraded react-native-system-navigation-bar to version 2.6.3. | VideoPlayer |  |
| 5.2.0 | breaking | Replaced @notifee/react-native with react-native-notify-kit library. | @notifee/react-native, react-native-notify-kit | react-native-notify-kit |
| 5.1.2 | improvement | Added push notification permission request support for Android API level>=33. | push notifications |  |
| 4.1.5 | requirement | Updated react-native-permissions to version 3.6.1. | react-native-permissions |  |
| 4.1.4 | requirement | Updated react-native-permissions to version 3.6.1. | react-native-permissions |  |
| 4.1.2 | fix | Fixed issue with missing react-native-schedule-exact-alarm-permission dependency. | react-native-schedule-exact-alarm-permission |  |
| 4.1.0 | improvement | Added CheckGenericPermission and updated RequestGenericPermission to use SCHEDULE_EXACT_ALARM. | CheckGenericPermission, RequestGenericPermission |  |
| 4.0.5 | improvement | Added push notification permission request support for Android API level>=33. | push notifications |  |
| 4.0.4 | requirement | Minimum Mendix version set to 9.24.1. | Mendix |  |
| 4.0.3 | fix | Updated react-native-device-info library. | react-native-device-info |  |
| 4.0.0 | breaking | Made AppEvents widget compatible with React Native 0.70.7. | AppEvents |  |
| 4.0.0 | breaking | Made BarChart widget compatible with React Native 0.70.7. | BarChart |  |
| 4.0.0 | breaking | Made BarcodeScanner widget compatible with React Native 0.70.7. | BarcodeScanner |  |
| 4.0.0 | breaking | Made Carousel widget compatible with React Native 0.70.7. | Carousel |  |
| 4.0.0 | breaking | Made ColorPicker widget compatible with React Native 0.70.7. | ColorPicker |  |
| 4.0.0 | breaking | Made ColumnChart widget compatible with React Native 0.70.7. | ColumnChart |  |
| 4.0.0 | breaking | Made FloatingActionButton widget compatible with React Native 0.70.7. | FloatingActionButton |  |
| 4.0.0 | breaking | Made LineChart widget compatible with React Native 0.70.7. | LineChart |  |
| 4.0.0 | breaking | Made ListViewSwipe widget compatible with React Native 0.70.7. | ListViewSwipe |  |
| 4.0.0 | breaking | Made Maps widget compatible with React Native 0.70.7. | Maps |  |
| 4.0.0 | breaking | Made Notifications widget compatible with React Native 0.70.7. | Notifications |  |
| 4.0.0 | breaking | Made PieDoughnutChart widget compatible with React Native 0.70.7. | PieDoughnutChart |  |
| 4.0.0 | breaking | Made PopupMenu widget compatible with React Native 0.70.7. | PopupMenu |  |
| 4.0.0 | improvement | Bumped react-native-progress dependency. | ProgressBar |  |
| 4.0.0 | breaking | Made Rating widget compatible with React Native 0.70.7. | Rating |  |
| 4.0.0 | breaking | Made Signature widget compatible with React Native 0.70.7. | Signature |  |
| 4.0.0 | breaking | Made Slider widget compatible with React Native 0.70.7. | Slider |  |
| 4.0.0 | breaking | Made VideoPlayer widget compatible with React Native 0.70.7. | VideoPlayer |  |
| 4.0.0 | breaking | Made WebView widget compatible with React Native 0.70.7. | WebView |  |
| 3.13.0 | breaking | Fixed Android 12 push notifications issue; native template must match module version. | Notifications |  |
| 3.11.1 | feature | Introduced new Download File action for Mendix document files to native device storage. | Download File |  |
| 3.11.1 | removal | Removed animated GIFs from README file. | Animation |  |
| 3.11.0 | feature | Introduced new RequestGenericPermission action for requesting any available device permission. | RequestGenericPermission |  |
| 3.10.0 | breaking | Added Atlas styling support; update Background gradient widgets design properties per Mendix Docs. | BackgroundGradient |  |
| 3.8.0 | fix | Fixed issue on Android devices when using Make it Native app to preview page containing Notifications widget. | Notifications |  |
| 3.7.1 | fix | Fixed issue on Android devices when using Make it Native app to preview page containing Notifications widget. | Notifications |  |
| 3.5.2 | fix | Reduced module size by removing unused dependencies to speed up Team Server interaction. |  |  |
| 3.5.1 | improvement | Updated the feedback API. | Feedback |  |
| 3.5.0 | fix | Updated action to prevent incorrect result when permission not yet requested on iOS due to hasPermission method change in react-native-firebase. |  |  |
| 3.4.3 | fix | Updated action to prevent incorrect result when permission not yet requested on iOS due to hasPermission method change in react-native-firebase. |  |  |
| 3.4.2 | fix | The version of react-native-vector-icons now matches that included in Native Template. | Image |  |
| 3.4.2 | fix | Widget refactored and now includes react-native-vector-icons version matching Native Template. | Rating |  |
| 3.1.4 | breaking | Version now stored in `themesource/.version` file instead of constant in Studio Pro Project Explorer. |  |  |
| 3.1.4 | fix | Fixed issue with some widget bundles erroneously including react-dom and being very large. |  |  |
| 3.1.4 | fix | Fixed issue with native release production bundles being mangled incorrectly, causing runtime errors. |  |  |
| 3.1.4 | fix | Fixed data source consistency check for MX 9.2 and above. | BarChart |  |
| 3.0.0 | breaking | TakePicture and TakePictureAdvanced no longer support 'either' as pictureSource parameter value. | TakePicture, TakePictureAdvanced |  |
| 3.0.0 | requirement | TakePicture and TakePictureAdvanced actions now support Android 11. | TakePicture, TakePictureAdvanced |  |
| 3.0.0 | fix | Fixed dynamic marker data source consistency check for Mendix 9.2 and above. | Maps |  |
| 2.0.0 | requirement | New native dependency management system. Every library now packaged with its dependencies. | Native dependency management system |  |
| 2.0.0 | security | Library updates and security fixes. |  |  |
| 2.0.0 | improvement | Updated WebView and Signature widgets. | WebView, Signature |  |
| 1.4.1 | fix | Added missing dependency to avoid bundling error. |  |  |
| 1.3.0 | breaking | TakePicture and TakePictureAdvanced no longer support 'either' as pictureSource parameter value. | TakePicture, TakePictureAdvanced |  |
| 1.3.0 | requirement | TakePicture and TakePictureAdvanced actions now support Android 11. | TakePicture, TakePictureAdvanced |  |
| 1.2.7 | improvement | Improved Native Webview widget's security measurements. | Native Webview |  |
| 1.2.0 | breaking | Renamed popup menu style property from containerStyle to container in basic and custom items. | Popup menu |  |
| 1.1.7 | breaking | Changed name from 'Popup menu' to 'Pop-up menu'. | Popup menu |  |
| 1.1.6 | security | Fixed security issue where captured image was saved instead of used temporarily. | TakePicture |  |
| 1.1.5 | fix | Fixed issue where some JS actions were not aligned with module name changes. |  |  |
| 1.1.4 | breaking | Removed extra arguments (widget & height attribute name) from TakePicture action. | TakePicture |  |
| 1.1.2 | breaking | Renamed module package name to Native Mobile Actions. |  |  |
| 1.1.1 | fix | Removed icon dependency on Nanoflow Commons added by mistake. | Nanoflow Commons |  |
| 1.1.0 | improvement | Updated widgets to be compatible with React Native upgrade to 0.61. |  |  |
| 1.0.10 | fix | Fixed DeviceInfo JS Action for compatibility with Studio Pro 8.6.3. | DeviceInfo |  |
| 1.0.8 | improvement | Updated Web view library. | Web view |  |
| 1.0.5 | fix | Fixed compatibility problem in GetDeviceInfo action. | GetDeviceInfo |  |
