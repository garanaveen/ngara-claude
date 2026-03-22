/**
 * A lightweight HTTP API client with retry and timeout support.
 */

const DEFAULT_TIMEOUT_MS = 10_000;
const DEFAULT_RETRIES = 3;
const RETRY_DELAY_MS = 500;

class ApiError extends Error {
  constructor(message, status, body) {
    super(message);
    this.name = "ApiError";
    this.status = status;
    this.body = body;
  }
}

/**
 * Sleep helper.
 * @param {number} ms
 */
function sleep(ms) {
  return new Promise((r) => setTimeout(r, ms));
}

/**
 * Minimal fetch wrapper with timeout.
 * @param {string} url
 * @param {RequestInit} options
 * @param {number} timeoutMs
 */
async function fetchWithTimeout(url, options = {}, timeoutMs = DEFAULT_TIMEOUT_MS) {
  const controller = new AbortController();
  const id = setTimeout(() => controller.abort(), timeoutMs);
  try {
    return await fetch(url, { ...options, signal: controller.signal });
  } finally {
    clearTimeout(id);
  }
}

class ApiClient {
  /**
   * @param {string} baseUrl
   * @param {Object} [opts]
   * @param {number} [opts.timeout]
   * @param {number} [opts.retries]
   * @param {Object} [opts.headers]
   */
  constructor(baseUrl, { timeout = DEFAULT_TIMEOUT_MS, retries = DEFAULT_RETRIES, headers = {} } = {}) {
    this.baseUrl = baseUrl.replace(/\/$/, "");
    this.timeout = timeout;
    this.retries = retries;
    this.defaultHeaders = { "Content-Type": "application/json", ...headers };
  }

  /**
   * Core request method with automatic retry on 5xx / network errors.
   */
  async request(method, path, { body, headers = {}, params } = {}) {
    let url = `${this.baseUrl}${path}`;
    if (params) {
      url += "?" + new URLSearchParams(params).toString();
    }

    const options = {
      method,
      headers: { ...this.defaultHeaders, ...headers },
    };
    if (body !== undefined) {
      options.body = JSON.stringify(body);
    }

    let lastError;
    for (let attempt = 0; attempt <= this.retries; attempt++) {
      if (attempt > 0) await sleep(RETRY_DELAY_MS * attempt);
      try {
        const res = await fetchWithTimeout(url, options, this.timeout);
        if (!res.ok) {
          const text = await res.text().catch(() => "");
          if (res.status >= 500 && attempt < this.retries) {
            lastError = new ApiError(`HTTP ${res.status}`, res.status, text);
            continue;
          }
          throw new ApiError(`HTTP ${res.status}: ${text}`, res.status, text);
        }
        const contentType = res.headers.get("content-type") || "";
        return contentType.includes("application/json") ? res.json() : res.text();
      } catch (err) {
        if (err instanceof ApiError) throw err;
        lastError = err;
      }
    }
    throw lastError;
  }

  get(path, opts) { return this.request("GET", path, opts); }
  post(path, opts) { return this.request("POST", path, opts); }
  put(path, opts) { return this.request("PUT", path, opts); }
  patch(path, opts) { return this.request("PATCH", path, opts); }
  delete(path, opts) { return this.request("DELETE", path, opts); }
}

module.exports = { ApiClient, ApiError };
