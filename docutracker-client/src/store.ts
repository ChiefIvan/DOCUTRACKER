import { writable, type Writable } from "svelte/store";

export type LoginBind = {
  emailInput: boolean;
  passwordInput: boolean;
};

export type SignUpBind = LoginBind & {
  userNameInput: boolean;
  cnfrmPasswordInput: boolean;
};

export type RegisterBind = {
  firstNameInput: boolean;
  middleNameInput: boolean;
  lastNameInput: boolean;
};

export type Credentials = {
  email?: string;
  password?: string;
  btnDisabled?: boolean;
  userName?: string;
  cnfrmPassword?: string;
  captVerification?: boolean;
  captcha?: string;
  captchaID?: string | null;
  userImg?: string | null;
  firstName?: string;
  middleName?: string;
  lastName?: string;
};

export type RequestAPI = {
  method: string;
  address: string;
  credentials?: Credentials | undefined;
};

export type ResponseData = {
  error?: string;
  success?: string;
  remembered?: string;
  email?: string;
  user_name?: string;
  full_ver_val?: boolean;
  captchaGETValue?: string[];
  captchaPOSTValue?: boolean;
  userImg?: string;
  firstName?: string;
  middleName?: string;
  lastName?: string;
};

export const handleFetch = async (
  value: RequestAPI,
  token: null | string = ""
) => {
  const { method, address, credentials } = value;
  let request: any;

  if (!credentials) {
    console.warn("Credentials are empty");
  }

  if (method === "POST") {
    if (credentials === undefined) {
      console.warn("Credentials are undefined");
    }

    request = await handlePOST(address, credentials!, token);
  }

  if (method === "GET") {
    request = await handleGET(address, token);
  }

  if (request.ok) {
    return await request.json();
  } else {
    throw new Error(`Request failed with status ${request.status}`);
  }
};

const handlePOST = async (
  address: string,
  credentials: Credentials,
  token: null | string
) => {
  try {
    return await fetch(address, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        ...(token?.length && { Authorization: `Bearer ${token}` }),
      },
      body: JSON.stringify(credentials),
    });
  } catch (error) {
    showMessage.set({ error: "Server Unreachable" });
    console.error(error);
    throw error;
  }
};

const handleGET = async (address: string, token: null | string) => {
  try {
    return await fetch(address, {
      method: "GET",
      headers:
        token && token.length === 0
          ? {
              "Content-Type": "application/json",
            }
          : {
              Authorization: `Bearer ${token}`,
            },
    });
  } catch (error) {
    showMessage.set({ error: "Server Unreachable" });
    console.error(error);
    throw error;
  }
};

export const address = "http://127.0.0.1:8080";
export const location = writable("/");
export const showMessage: Writable<ResponseData> = writable({});

localStorage.getItem("mode") || localStorage.setItem("mode", "System");
export const modeExpand = writable(false);
export const profileExpand = writable(false);
export const navExpand = writable(true);
export const registrationExpand = writable(false);
export const dark = writable(false);
