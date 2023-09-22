import { writable } from "svelte/store";

export const pageTransitionValue1 = writable(0);
export const pageTransitionValue2 = writable(0);
export const captchaAttemps = writable(3);
export const entryState = writable(false);
export const loaderState = writable(false);
export const captchaVerification = writable(false);
export const serverResponse = writable({});
export const userContent = writable({});
export const pageLocation = writable("");
export const resetInput = writable();
