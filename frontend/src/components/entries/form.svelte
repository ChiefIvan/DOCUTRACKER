<script>
  import {
    entryState,
    resetInput,
    serverResponse,
    loaderState,
    captchaVerification,
    captchaAttemps,
  } from "../../stores";
  import { createEventDispatcher } from "svelte";
  import { navigate } from "svelte-routing";

  export let requestBody = {};
  export let api = "";
  export let warnMessage = "";
  export let navigateUser = "";
  export let handleResetPassword = null;
  export let parentName = null;
  // export let disableResend = false;

  const dispatch = createEventDispatcher();

  async function handleSubmit() {
    updateStatesBeforeSubmit();

    try {
      const request = await sendRequest(requestBody);

      if (request.ok) {
        handleSuccessfulRequest(request);
      }
    } catch {
      $serverResponse = {
        error: "Server is down, please try again later.",
      };
    }

    updateStatesAfterSubmit();
  }

  function updateStatesBeforeSubmit() {
    $loaderState = true;
    $entryState = true;
    $captchaAttemps = 3;
    $resetInput.blur();
  }

  async function sendRequest(userCredentials) {
    return await fetch(api, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(userCredentials),
    });
  }

  async function handleSuccessfulRequest(request) {
    let response = await request.json();

    if (response.error) {
      $serverResponse = { error: response.error };
      return;
    }

    handleSuccessResponse(response);

    if (response.remembered) {
      localStorage.setItem("remembered", response.remembered);
    }
  }

  /**
   * @param {any} response
   */
  function handleSuccessResponse(response) {
    if (response.success) {
      $serverResponse = { success: response.success };
      if (parentName === "reset") {
        handleResetPassword();
      }
    }

    navigateUser !== "/home"
      ? navigate(navigateUser)
      : (window.location.href = navigateUser);

    if (warnMessage.length === 0) {
      return;
    }

    setTimeout(() => {
      alert(warnMessage);
    }, 1000);
  }

  function updateStatesAfterSubmit() {
    $loaderState = false;
    $captchaVerification = false;
    localStorage.setItem(
      "userEmail",
      requestBody.email.length != 0 ? requestBody.email : ""
    );
    dispatch("resetInput", "");
  }
</script>

<form on:submit|preventDefault={handleSubmit}>
  <slot />
</form>

<style>
  form {
    display: flex;
    justify-content: center;
    align-items: flex-start;
    flex-direction: column;
    row-gap: 1rem;
  }
</style>
