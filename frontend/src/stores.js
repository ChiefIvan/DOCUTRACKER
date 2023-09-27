import { writable } from "svelte/store";

export const pageTransitionValue1 = writable(0);
export const pageTransitionValue2 = writable(0);
export const captchaAttemps = writable(3);
export const entryState = writable(false);
export const loaderState = writable(false);
export const captchaVerification = writable(false);
export const serverResponse = writable({});
export const fetchData = writable({});
export const location = writable("");
export const backendAddress = "http://127.0.0.1:5000/";
export const resetInput = writable();
