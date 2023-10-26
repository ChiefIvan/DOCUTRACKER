<script>
  // @ts-nocheck

  import { fade } from "svelte/transition";
  import {
    serverResponse,
    resetInput,
    captchaVerification,
    captchaAttemps,
    backendAddress,
  } from "../../stores";

  import Input from "./input.svelte";
  import Button from "./button.svelte";
  import Checkbox from "./checkbox.svelte";

  let bytesIO = {};
  let id = "";
  let byteValue = "";
  let userCaptGenVal = "";

  export let checkboxDisabled = true;

  const captchaAPI = `${backendAddress}captcha`;
  const checkboxName = "I am not a Robot";

  async function handleGETCaptcha() {
    $captchaAttemps--;

    if ($captchaAttemps < 0) {
      $serverResponse = {
        error: "Captcha Verification Failed!, Please Try Again.",
      };

      $captchaAttemps = 3;
      return;
    }

    await fetch(captchaAPI, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.json())
      .then((data) => (bytesIO = data.captcha))
      .catch(
        () =>
          ($serverResponse = {
            error: "Server is down, please try again later.",
          })
      );

    id = bytesIO[1];
    byteValue = bytesIO[0];

    localStorage.setItem("captchaId", id);
  }

  async function handlePOSTCaptcha() {
    $resetInput.blur();

    let userCaptCredentials = {
      captValue: userCaptGenVal,
      captchaId: localStorage.getItem("captchaId") || "",
    };

    try {
      const captAPIres = await fetch(captchaAPI, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(userCaptCredentials),
      });

      if (captAPIres.ok) {
        const data = await captAPIres.json();
        if (Object.keys(data) == "success") {
          $captchaVerification = data["success"];
          checkboxDisabled = $captchaVerification && true;
        } else {
          setTimeout(() => {
            handleGETCaptcha();
          }, 1000);
        }
      }
    } catch {
      $serverResponse = {
        error: "Server is down, please try again later.",
      };
    }

    byteValue = "";
    userCaptGenVal = "";
  }
</script>

{#if byteValue.length !== 0}
  <div class="capt-img-wrapper" transition:fade={{ delay: 100, duration: 400 }}>
    <form on:submit|preventDefault={handlePOSTCaptcha}>
      <!-- svelte-ignore a11y-img-redundant-alt -->
      <img src={`data:image/jpeg;base64,${byteValue}`} alt="Captcha Image" />
      <Input
        inputName={"Captcha"}
        inputType={"text"}
        inputAutocomplete={"off"}
        inputValue={userCaptGenVal}
        inputZ={true}
        inputSize={true}
        on:input={(e) => (userCaptGenVal = e.target.value)}
      />
      <div class="btn-wrapper">
        <Button btnName={"Verify"} btnSignupSize={true} btnTitle={"Verify"} />
      </div>
    </form>
  </div>
{/if}

<Checkbox
  on:change={handleGETCaptcha}
  {checkboxDisabled}
  {checkboxName}
  checkboxChecked={$captchaVerification}
/>

<style>
  div.capt-img-wrapper {
    z-index: 1;
    position: fixed;
    inset: 0;
    cursor: default;

    display: flex;
    justify-content: center;
    align-items: center;

    & form {
      display: flex;
      align-items: flex-start;
      justify-content: center;
      flex-direction: column;
      row-gap: 1rem;

      background-color: white;
      padding: 0.5rem;
      box-shadow: 5px 5px 25px var(--main-col-1);
      border-radius: 1rem;

      & div.btn-wrapper {
        width: 100%;
        display: flex;
        justify-content: flex-end;
      }
    }
  }
</style>
