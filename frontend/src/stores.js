import { writable } from "svelte/store";

export const pageTransitionValue1 = writable({});
export const pageTransitionValue2 = writable({});
export const serverResponse = writable({});
export const fetchData = writable({});

export const entryState = writable(false);
export const loaderState = writable(false);
export const winEvent = writable(false);
export const expand = writable(false);
export const captchaVerification = writable(false);
export const dark = writable(false);
export const openProfile = writable(false);
export const openVerSec = writable(false);

export const location = writable("");
export const backendAddress = "http://127.0.0.1:5000/";

export const captchaAttemps = writable(3);
export const resetInput = writable();
localStorage.getItem("mode") || localStorage.setItem("mode", "System");
