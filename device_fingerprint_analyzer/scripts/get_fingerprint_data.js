async function getFingerprint() {
    // Time Zone
    const timeZone = Intl.DateTimeFormat().resolvedOptions().timeZone;
    const timezoneOffset = new Date().getTimezoneOffset();
    const languages = navigator.languages;

    // Hardware Info
    const cpuCores = navigator.hardwareConcurrency || null;
    const deviceMemory = navigator.deviceMemory || null;

    let deviceArchitecture = null;
    const ua = navigator.userAgent.toLowerCase();
    if (ua.includes('arm')) deviceArchitecture = 'arm';
    else if (ua.includes('x86_64') || ua.includes('win64') || ua.includes('wow64')) deviceArchitecture = 'x86_64';
    const systemUptime = performance.now() / 1000; 

    // Graphics Info - WebGL context
    const canvas = document.createElement('canvas');
    const gl = canvas.getContext('webgl') || canvas.getContext('experimental-webgl');
    let webglRenderer = null;
    let webglVendor = null;
    let webglExtensions = [];
    if (gl) {
        webglRenderer = gl.getParameter(gl.RENDERER);
        webglVendor = gl.getParameter(gl.VENDOR);
        webglExtensions = gl.getSupportedExtensions() || [];
    }

    // WebGPU adapter (if available)
    let webgpuAdapter = null;
    if (navigator.gpu) {
        try {
            webgpuAdapter = await navigator.gpu.requestAdapter();
        } catch (e) {
            webgpuAdapter = null;
        }
    }

    // Canvas Fingerprint - just a simple canvas.toDataURL hash placeholder (use actual hash for real)
    const ctx = canvas.getContext('2d');
    let canvasHash = null;
    if (ctx) {
        ctx.textBaseline = "top";
        ctx.font = "14px 'Arial'";
        ctx.fillText("Fingerprint test", 2, 2);
        canvasHash = canvas.toDataURL();
    } else {
        canvasHash = "canvas_context_unavailable";
    }


    // WebGL hash placeholder (in real case use pixel data and hash it)
    const webglHash = canvasHash;

    // Media Capabilities - simplified: just list some audio and video codecs
    const audioCodecs = ["audio/mp3", "audio/wav"];
    const videoCodecs = ["video/mp4", "video/webm"];
    // Media devices
    let mediaDevices = [];
    if (navigator.mediaDevices && navigator.mediaDevices.enumerateDevices) {
        try {
            mediaDevices = await navigator.mediaDevices.enumerateDevices();
            mediaDevices = mediaDevices.map(device => ({
                kind: device.kind,
                label: device.label,
                deviceId: device.deviceId
            }));
        } catch (e) {
            mediaDevices = [];
        }
    }

    // Touch Pointer
    const maxTouchPoints = navigator.maxTouchPoints || 0;
    const pointerFine = window.matchMedia('(any-pointer: fine)').matches;
    const standalone = window.matchMedia('(display-mode: standalone)').matches;

    // Network Connection
    const connection = navigator.connection || navigator.mozConnection || navigator.webkitConnection || {};
    const effectiveType = connection.effectiveType || null;
    const downlink = connection.downlink || null;
    const rtt = connection.rtt || null;

    // Battery Info
    let battery = null;
    if (navigator.getBattery) {
        try {
            battery = await navigator.getBattery();
        } catch (e) { }
    }

    return {
        timezone: { time_zone: timeZone, timezone_offset: timezoneOffset, languages },
        hardware: { cpu_cores: cpuCores, device_memory: deviceMemory, device_architecture: deviceArchitecture, system_uptime: systemUptime },
        graphics: { webgl_renderer: webglRenderer, webgl_vendor: webglVendor, webgl_extensions: webglExtensions, webgpu_adapter: webgpuAdapter },
        canvas_fp: { canvas_hash: canvasHash, webgl_hash: webglHash },
        media: { audio_codecs: audioCodecs, video_codecs: videoCodecs, media_devices: mediaDevices },
        touch_pointer: { max_touch_points: maxTouchPoints, pointer_fine: pointerFine, standalone },
        network: { effective_type: effectiveType, downlink, rtt },
        battery: battery ? { level: battery.level, charging_time: battery.chargingTime, discharging_time: battery.dischargingTime } : null,
    };
}

getFingerprint().then(console.log).catch(console.error);
