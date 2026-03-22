/**
 * General-purpose utility functions.
 */

/**
 * Clamp a number between min and max (inclusive).
 */
function clamp(value, min, max) {
  return Math.min(Math.max(value, min), max);
}

/**
 * Deep-clone a plain object or array using JSON round-trip.
 */
function deepClone(obj) {
  return JSON.parse(JSON.stringify(obj));
}

/**
 * Chunk an array into sub-arrays of a given size.
 * @param {Array} arr
 * @param {number} size
 * @returns {Array[]}
 */
function chunk(arr, size) {
  if (size <= 0) throw new Error("Chunk size must be positive");
  const result = [];
  for (let i = 0; i < arr.length; i += size) {
    result.push(arr.slice(i, i + size));
  }
  return result;
}

/**
 * Debounce a function so it only fires after `delay` ms of inactivity.
 */
function debounce(fn, delay) {
  let timer;
  return function (...args) {
    clearTimeout(timer);
    timer = setTimeout(() => fn.apply(this, args), delay);
  };
}

/**
 * Return a promise that resolves after `ms` milliseconds.
 */
function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

/**
 * Group an array of objects by the value of a given key.
 * @param {Object[]} arr
 * @param {string} key
 * @returns {Object.<string, Object[]>}
 */
function groupBy(arr, key) {
  return arr.reduce((acc, item) => {
    const group = String(item[key] ?? "");
    (acc[group] = acc[group] || []).push(item);
    return acc;
  }, {});
}

/**
 * Capitalize the first letter of a string.
 */
function capitalize(str) {
  if (!str) return str;
  return str.charAt(0).toUpperCase() + str.slice(1);
}

/**
 * Convert a camelCase string to snake_case.
 */
function toSnakeCase(str) {
  return str.replace(/([A-Z])/g, "_$1").toLowerCase();
}

/**
 * Flatten a nested array one level deep.
 */
function flatten(arr) {
  return arr.reduce((acc, val) => acc.concat(val), []);
}

/**
 * Return unique elements of an array (shallow equality).
 */
function unique(arr) {
  return [...new Set(arr)];
}

module.exports = {
  clamp,
  deepClone,
  chunk,
  debounce,
  sleep,
  groupBy,
  capitalize,
  toSnakeCase,
  flatten,
  unique,
};
