<script>
  import { entryState, resetInput, serverResponse } from "../../stores";
  import { createEventDispatcher } from "svelte";

  export let userName = "";
  export let email = "";
  export let password = "";
  export let cnfrmPassword = "";
  export let api = "";

  const dispatch = createEventDispatcher();

  async function handleSubmit() {
    $entryState = true;
    $resetInput.blur();

    const userCredentials = {
      name: userName,
      email: email,
      password: password,
      confirm_password: cnfrmPassword,
    };

    try {
      const request = await fetch(api, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(userCredentials),
      });

      $serverResponse = await request.json();

      if (request.ok) {
        console.log("Data submitted successfully!");
      }
    } catch {
      $serverResponse = {
        error: "Error submitting data, please try again later.",
      };
    }

    dispatch("resetInput", "");
    setTimeout(() => {
      $serverResponse = {};
    }, 5000);
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
    row-gap: 1.3rem;
  }
</style>
