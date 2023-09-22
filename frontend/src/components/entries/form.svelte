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

  export let userName = "";
  export let email = "";
  export let password = "";
  export let cnfrmPassword = "";
  export let api = "";
  export let navigateUser = "";

  const dispatch = createEventDispatcher();

  async function handleSubmit() {
    $loaderState = true;
    $entryState = true;
    $captchaAttemps = 3;
    $resetInput.blur();

    const userCredentials = {
      name: userName,
      email: email,
      password: password,
      confirm_password: cnfrmPassword,
      captVerification: $captchaVerification,
    };

    try {
      const request = await fetch(api, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(userCredentials),
      });

      if (request.ok) {
        let response = await request.json();

        if (response.error) {
          $serverResponse = { error: response.error };
        } else {
          $serverResponse = { success: response.success };
        }

        if (response.remembered) {
          localStorage.setItem("remembered", response.remembered);
        }
      }
    } catch {
      $serverResponse = {
        error: "Server is down, please try again later.",
      };
    }

    if (String(Object.keys($serverResponse)) !== "error") {
      navigate("/login");
    }

    $loaderState = false;
    $captchaVerification = false;
    localStorage.setItem("userEmail", email.length != 0 ? email : "");
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
