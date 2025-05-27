from dataclasses import dataclass


@dataclass
class TimeZone:
    time_zone: str                     # Time zone identifier // Intl.DateTimeFormat().resolvedOptions().timeZone
    timezone_offset: int               # Offset from UTC in minutes // new Date().getTimezoneOffset()
    languages: list[str] | None        # List of user preferred languages // navigator.languages

@dataclass
class Hardware:
    os: str                            # Operating system name + version // navigator.userAgent
    cpu_cores: int                     # Number of logical CPU cores // navigator.hardwareConcurrency
    device_memory: float               # Amount of RAM in gigabytes // navigator.deviceMemory
    device_architecture: str | None    # Inferred from userAgent (e.g., "arm", "x86_64") // navigator.userAgent

@dataclass
class Display:
    screen_height: int                 # The height of the screen in pixels // window.screen.height
    screen_width: int                  # The width of the screen in pixels // window.screen.width
    color_depth: int                   # Screen color depth in bits // screen.colorDepth
    device_pixel_ratio: float          # Ratio of physical pixels to CSS pixels // window.devicePixelRatio
    color_gamut: str | None            # Color gamut supported // const gamut = ['rec2020', 'p3', 'srgb'].find(g => window.matchMedia(`(color-gamut: ${g})`).matches); console.log(gamut); 

@dataclass
class HttpHeaderFingerprint:
    header_count: int                       # Total number of HTTP headers sent
    unusual_headers: list[str]              # List of uncommon headers present 
    header_order_hash: str                  # Hash of header names order
    http_version: str                       # HTTP version used 
    tls_protocol: str | None                # TLS protocol version 
    tls_cipher_suite: str | None            # TLS cipher suite 

@dataclass
class Behavioral:
    typing_speed: float | None                   # Average typing speed
    keystroke_dynamics: dict[str, float] | None  # Keystroke timing info
    mouse_entropy: float | None                  # Mouse movement randomness measure
    scroll_behavior: dict[str, float] | None     # Scroll event metrics
    time_of_visit_patterns: list[str] | None     # Behavioral time patterns
    url_changes: list[str] | None                # URLs visited during session

@dataclass
class Storage:
    indexeddb_dbs: list[str] | None            # List of IndexedDB databases // indexedDB.databases()
    cache_storage_keys: list[str] | None       # List of Cache Storage keys // caches.keys()
    cookies_enabled: bool                      # Whether cookies are enabled // navigator.cookieEnabled
    storage_estimate: dict[str, float] | None  # Storage usage and quota estimates // navigator.storage.estimate()
    service_workers: list[str] | None          # List of registered Service Worker URLs // navigator.serviceWorker.getRegistrations()

@dataclass
class CSSMediaFeature:
    prefers_dark_scheme: bool            # Dark mode preference // window.matchMedia('(prefers-color-scheme: dark)').matches
    font_smoothing: bool                 # Font smoothing enabled // TODO: Needs custom script
    reduced_motion: bool                 # Reduced motion preference // window.matchMedia('(prefers-reduced-motion: reduce)').matches
    reduced_data: bool                   # Reduced data usage preference // window.matchMedia('(prefers-reduced-data: reduce)').matches
    forced_colors: bool                  # Forced colors mode // window.matchMedia('(forced-colors: active)').matches

@dataclass
class PermissionsStatus:
    geolocation: str | None              # Permission status // navigator.permissions.query({ name: 'geolocation' })
    notifications: str | None            # Permission status // navigator.permissions.query({ name: 'notifications' })
    camera: str | None                   # Permission status // navigator.permissions.query({ name: 'camera' })
    microphone: str | None               # Permission status // navigator.permissions.query({ name: 'microphone' })
    midi: str | None                     # Permission status // navigator.permissions.query({ name: 'midi' })

@dataclass
class Graphics:
    webgl_renderer: str | None                # WebGL renderer // const gl = document.createElement('canvas').getContext('webgl') || document.createElement('canvas').getContext('experimental-webgl'); if (!gl) console.log("WebGL not supported"); else console.log("Renderer:", (gl.getExtension('WEBGL_debug_renderer_info') ? gl.getParameter(gl.getExtension('WEBGL_debug_renderer_info').UNMASKED_RENDERER_WEBGL) : gl.getParameter(gl.RENDERER)));
    webgl_vendor: str | None                  # WebGL vendor // const gl=document.createElement('canvas').getContext('webgl')||document.createElement('canvas').getContext('experimental-webgl');if(!gl)console.log("WebGL not supported");else{const debugInfo=gl.getExtension('WEBGL_debug_renderer_info');const vendor=debugInfo?gl.getParameter(debugInfo.UNMASKED_VENDOR_WEBGL):gl.getParameter(gl.VENDOR);console.log("Vendor:",vendor);}
    webgl_extensions: list[str] | None        # Supported WebGL extensions // const webgl_extensions = (gl => gl ? gl.getSupportedExtensions() : null)(document.createElement('canvas').getContext('webgl') || document.createElement('canvas').getContext('experimental-webgl'));
    webgpu_adapter: dict[str, object] | None  # TODO: Use WebGPU API

@dataclass
class NetworkConnection:
    effective_type: str | None           # Effective connection type // navigator.connection.effectiveType
    downlink: float | None               # Approximate downlink speed in Mbps // navigator.connection.downlink
    rtt: int | None                      # Round-trip time estimate in ms // navigator.connection.rtt
    webrtc_local_ips: list[str] | None   # Local IPs discovered via WebRTC

@dataclass
class Browser:
    vendor: str                              # Browser vendor name // navigator.vendor
    product_sub: str                         # Product sub-version identifier // navigator.productSub
    build_id: str | None                     # Browser build identifier // navigator.buildID
    private_mode: bool | None                # Private/incognito mode status

@dataclass
class Media:
    audio_codecs: list[str] | None              # Supported audio codecs // mediaCapabilities.decodingInfo()
    video_codecs: list[str] | None              # Supported video codecs // mediaCapabilities.decodingInfo()
    media_devices: list[dict[str, str]] | None  # Available media devices // navigator.mediaDevices.enumerateDevices()

@dataclass
class TouchPointer:
    max_touch_points: int                 # Maximum simultaneous touch points // navigator.maxTouchPoints
    pointer_fine: bool                    # Fine pointer input available // matchMedia
    standalone: bool                      # Standalone display-mode // matchMedia

@dataclass
class PerformanceTimings:
    timings: dict[str, float]                # Performance timing metrics // performance.timing
    memory: dict[str, float] | None          # Memory usage stats // performance.memory
    network_timing: dict[str, float] | None  # Network timing metrics // performance entries

@dataclass
class IP:
    ip_address: str | None                  # User's public IP address
    details: dict[str, object] | None       # Additional IP-related details

@dataclass
class Canvas:
    canvas_hash: str | None                 # 2D canvas fingerprint hash
    webgl_hash: str | None                  # WebGL canvas fingerprint hash

@dataclass
class MediaEncryption:
    eme_supported: bool | None              # Encrypted Media Extensions support
    cdm_list: list[str] | None              # Available Content Decryption Modules

@dataclass
class InstalledSoftware:
    mime_types: list[str] | None            # Supported MIME types by browser plugins

@dataclass
class Audio:
    audio_hash: str | None                  # Web Audio API fingerprint hash

@dataclass
class Fonts:
    installed_fonts: list[str] | None       # Installed system fonts

@dataclass
class Fingerprint:
    ip: IP
    media: Media
    audio: Audio
    canvas: Canvas
    behavioral: Behavioral
    hardware: Hardware
    graphics: Graphics
    timezone: TimeZone
    network: NetworkConnection
    touch_pointer: TouchPointer
    css_features: CSSMediaFeature
    performance: PerformanceTimings
    installed_software: InstalledSoftware
    http_header_fingerprint: HttpHeaderFingerprint

    fonts: Fonts | None = None
    display_info: Display | None = None
    browser_details: Browser | None = None
    storage_details: Storage | None = None
    media_encryption: MediaEncryption | None = None
    permissions_status: PermissionsStatus | None = None
